from variables import *
from imports import *
import discord
from discord.ext import commands
from commands.data import * 
from data import *


load_dotenv()
TOKEN = os.getenv("TOKEN")



intents = discord.Intents.default()
intents.message_content = True      
intents.members = True  
intents.messages = True 

bot = commands.Bot(command_prefix=prefix, intents=intents)

# COMMANDES DE DATA
server_commands(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Server ✅")
    
backup_commands(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Backup ✅")
    
infos_commands(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Infos ✅")
    
fetch_all_commands(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Fetch All ✅")
    
get_messages(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Catch Message ✅")

fetch_user_id_command(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande ID ✅")

# COMMANDE DE PERSONNALISATION
status_command(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Status ✅")

# COMMANDE CONTROL

start_control(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Start_control ✅")

stop_control(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Stop Control ✅")
# COMMANDE DIVERS / HELP
help_commands(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Help ✅")
    
ping_command(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Ping ✅")
    
quoi_command(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Quoi ✅")

source_code(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande code ✅")
    
assettocorsa(bot)
if DEBUG_MODE == True:
    print("Chargement de la commande Assettocorsa ✅")
# EVENEMENTS


if DEBUG_MODE == True:
    print("Anti Erreur Prêt ✅")


guild_update(bot)
member_join(bot)
member_remove(bot)
message_delete(bot)
on_message(bot)
if DEBUG_MODE == True:
    print("Fonctions d'événements prêtes ✅")

onload(bot)


Music(bot)
if DEBUG_MODE == True:
    print("Fonctions de Musiques prêtes ✅")


bot.run(TOKEN)
