import discord
from discord.ext import commands, tasks
from server_config_manager import ServerConfigManager
from utils.sqs_handler import receive_sqs_messages, delete_sqs_message, process_sqs_message
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

class UpdateNotifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_manager = ServerConfigManager()
        self.check_updates.start()

    def get_full_url(self, base_url, chapter_url):
        return urljoin(base_url, chapter_url)

    @tasks.loop(minutes=5)
    async def check_updates(self):
        """
        Polls SQS for updates and sends notifications to servers
        where `is_checking_updates` is True
        """
        
        messages = receive_sqs_messages()
        if not messages:
            return

        for message in messages:
            chapter_no, chapter_title, chapter_url = process_sqs_message(message)
            if not chapter_no:
                continue

            for guild in self.bot.guilds:
                server_id = str(guild.id)
                config = self.config_manager.get_server_config(server_id)

                # check if updates is toggled
                if not config.get("is_checking_updates", False):
                    logger.info(f"Skipping updates for server {server_id}, updates are disabled.")
                    continue

                # check if channel is set
                channel_id = config.get("post_channel_id")
                if not channel_id:
                    continue

                # send chapter update to channel
                channel = self.bot.get_channel(channel_id)
                if channel:
                    full_chapter_url = self.get_full_url(config["URL"], chapter_url)
                    mentions = " ".join([f"<@&{role_id}>" for role_id in config["subscribed_roles"]])

                    embed = discord.Embed(
                        title=f"New Chapter Released: {chapter_title}",
                        url=full_chapter_url,
                        description=f"Daily addiction injection: **{chapter_title}**",
                        color=discord.Color.blue()
                    )
                    embed.add_field(name="Chapter Number", value=chapter_no, inline=True)
                    embed.add_field(name="Read Now", value=f"[Click here to read chapter]({full_chapter_url})", inline=False)
                    embed.set_footer(text="Chapter updates")
                    embed.set_image(url="https://i.imgur.com/UPfOqLm.jpeg")

                    await channel.send(content=mentions, embed=embed)

            delete_sqs_message(message['ReceiptHandle'])

    @check_updates.before_loop
    async def before_check_updates(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(UpdateNotifier(bot))
