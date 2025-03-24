import discord
from discord.ext import commands
from dotenv import load_dotenv

from imports import * # Importations de tous ce qu'il y à dans imports.py
from variables import * # Importations de tous ce qu'il y à dans variables.py


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True  

bot = commands.Bot(command_prefix=prefix, intents=intents)

server_commands(bot)
help_commands(bot)
infos_commands(bot)


bot.run(TOKEN)

