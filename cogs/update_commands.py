import discord
from discord.ext import commands
from .update_notifier import UpdateNotifier

class UpdateCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_notifier: UpdateNotifier = bot.get_cog('UpdateNotifier')

    @commands.command(name="toggle_updates")
    @commands.has_permissions(administrator=True)
    async def toggle_updates(self, ctx):
        server_id = str(ctx.guild.id)
        config = self.update_notifier.config_manager.get_server_config(server_id)

        config["is_checking_updates"] = not config["is_checking_updates"]
        self.update_notifier.config_manager.update_server_config(server_id, config)
        
        status = "on" if config["is_checking_updates"] else "off"
        await ctx.send(f"Update checking is now {status}.")

        if config["is_checking_updates"]:
            await self.update_notifier.check_updates()

    @commands.command(name="subscribe_role")
    @commands.has_permissions(administrator=True)
    async def subscribe_role(self, ctx, role: discord.Role):
        server_id = str(ctx.guild.id)
        config = self.update_notifier.config_manager.get_server_config(server_id)

        if role.id not in config["subscribed_roles"]:
            config["subscribed_roles"].append(role.id)
            self.update_notifier.config_manager.update_server_config(server_id, config)
            await ctx.send(f"Role {role.name} has been subscribed to updates.")
        else:
            await ctx.send(f"Role {role.name} is already subscribed.")

    @commands.command(name="unsubscribe_role")
    @commands.has_permissions(administrator=True)
    async def unsubscribe_role(self, ctx, role: discord.Role):
        server_id = str(ctx.guild.id)
        config = self.update_notifier.config_manager.get_server_config(server_id)

        if role.id in config["subscribed_roles"]:
            config["subscribed_roles"].remove(role.id)
            self.update_notifier.config_manager.update_server_config(server_id, config)
            await ctx.send(f"Role {role.name} has been unsubscribed from updates.")
        else:
            await ctx.send(f"Role {role.name} is not subscribed.")

    @commands.command(name="set_channel")
    @commands.has_permissions(administrator=True)
    async def set_channel(self, ctx, channel: discord.TextChannel):
        server_id = str(ctx.guild.id)
        config = self.update_notifier.config_manager.get_server_config(server_id)

        config["post_channel_id"] = channel.id
        self.update_notifier.config_manager.update_server_config(server_id, config)
        await ctx.send(f"Updates will now be posted in {channel.mention}.")

async def setup(bot):
    await bot.add_cog(UpdateCommands(bot))
