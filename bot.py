import discord
from discord.ext import commands
import logging
from utils.secret_manager import get_secret

logging.basicConfig(level=logging.DEBUG)

try:
    BOT_TOKEN = get_secret("bot_token", "us-east-2")
except Exception as e:
    logging.error(f"Failed to retrieve BOT_TOKEN: {e}")
    raise

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    await bot.load_extension('cogs.update_notifier')
    await bot.load_extension('cogs.update_commands')

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name} ({bot.user.id})")
    await load_extensions()

bot.run(BOT_TOKEN)
