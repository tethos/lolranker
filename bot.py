import os
import discord
from discord import Intents
from dotenv import load_dotenv
from discord.commands import Option
from app.utils.cog_loader import CogLoader

COGS_DIR = 'app/cogs'
load_dotenv()

DISCORD_GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

intents: Intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=[DISCORD_GUILD_ID]
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


if __name__ == '__main__':
    CogLoader.load_cogs(bot, COGS_DIR)
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
