#python bot 
import os

import discord
from dontenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD TOKEN')

client = discord.Client()

@client.event 
async def on_ready():
    for guild in client.guilds:
        in guild.name == GUILD:
        break 
    print(
        f'{client.user} is connected'
    )
client.run(TOKEN)