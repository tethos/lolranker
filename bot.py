import os
import discord
from dotenv import load_dotenv
from discord.commands import Option

load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=[os.getenv('DEBUG_GUILD_ID')],
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
