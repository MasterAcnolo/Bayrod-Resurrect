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
get_messages(bot)
print("Chargement de la commande Catch Message ✅")
# COMMANDE DE PERSONNALISATION
status_command(bot)
print("Chargement de la commande Status ✅")

# COMMANDE DIVERS / HELP
help_commands(bot)
print("Chargement de la commande Help ✅")

ping_command(bot)
print("Chargement de la commande Ping ✅")

quoi_command(bot)
print("Chargement de la commande Quoi ✅")
# EVENEMENTS


antierror(bot)
print("Anti Erreur Prêt ✅")


guild_update(bot)
member_join(bot)
member_remove(bot)
message_delete(bot)
print("Fonctions d'événements prêtes ✅")

onload(bot)



bot.run(TOKEN)