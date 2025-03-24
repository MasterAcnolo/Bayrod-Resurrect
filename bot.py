from variables import *
from imports import * # Importations de tous ce qu'il y à dans imports.py
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True      
intents.members = True  
intents.messages = True 
   
bot = commands.Bot(command_prefix=prefix, intents=intents)

# COMMANDES DE DATA
server_commands(bot)
print("Chargement de la commande Server ✅")
backup_commands(bot)
print("Chargement de la commande Backup ✅")
infos_commands(bot)
print("Chargement de la commande Infos ✅")
fetchall_commands(bot)
print("Chargement de la commande Fetch All ✅")

# COMMANDE DE PERSONNALISATION
status_command(bot)
print("Chargement de la commande Status ✅")

# COMMANDE DIVERS / HELP
help_commands(bot)
print("Chargement de la commande Help ✅")

ping_command(bot)
print("Chargement de la commande Ping ✅")

# EVENEMENTS

message_delete(bot)
antierror(bot)
print("Anti Erreur Prêt ✅")
onload(bot)



bot.run(TOKEN)