import os
import discord
from dotenv import load_dotenv
from discord.commands import Option
from app.Utils.CogLoader import CogLoader

COGS_DIR = './app/Cogs'
load_dotenv()

DISCORD_GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

intents = discord.Intents.default()
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
