######### IMPORTATIONS DES LIBRAIRIES ##########################################################

import os                                         
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import shutil
from datetime import datetime

##################################################################################################

#FAUT IMPORTER LE FICHIER ENV OU YA LE TOKEN 
load_dotenv()
TOKEN = os.getenv("TOKEN")

# ICI ON ACTIVE LES INTENTS (Autorisation du bot)
intents = discord.Intents.default()
intents.message_content = True  
intents.members = True  

##################################################################################################

#VARIABLES DE PERSONNALISATION

prefix = ';'
WELCOME_CHANNEL_ID = 1347277296788177037 # <-- Sur 'SERVEUR DE TEST' ACTUELLEMENT
DATA_FILE = "database.json" # <-- PATH DE LA BASE DE DONNEES

COULEUR_EMBED_INFO = 0xff1100
##################################################################################################
bot = commands.Bot(command_prefix=prefix, intents=intents) # <-- Le Nom du bot c'est 'bot'. Si on veut le modifier faut changer tous le code pour remplacer bot --> NOM DU BOT
##################################################################################################

#Commandes de Listings des commandes

@bot.command()
async def commands(ctx):
    embed = discord.Embed(
        title="💻 **Menu des commandes** 💻",
        description=f"📂 Commandes Disponibles: XX\n♦️Le Préfix du Serveur est **{prefix}**\n☕️ En savoir plus avec : **{prefix}maj**" + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Fetch Info: \n ```infos[@member],fetchall, server,update, backup```",
        color=0x001eff
    )
    embed.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Divers",value="```ping, ```", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Admin",value="```null, ```",inline=False)

    await ctx.send(embed=embed)

##################################################################################################
# FONCTIONS SANS COMMANDE

# FETCH LES DONNES DANS LA BDD 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

#SAVE LES UPDATES

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# FETCH / UPDATE LES INFOS D'UN SERVEUR
def fetch_server_data(guild: discord.Guild):
    data = load_data()
    guild_id = str(guild.id)

    if "servers" not in data:
        data["servers"] = {}

     
    data["servers"][guild_id] = {
        "id": guild.id,
        "name": guild.name,
        "owner": guild.owner.name if guild.owner else "Inconnu",
        "member_count": guild.member_count,
        "created_at": str(guild.created_at),
        "text_channels": len(guild.text_channels),
        "voice_channels": len(guild.voice_channels),
        "roles_count": len(guild.roles),
        "preferred_locale": guild.preferred_locale,
        "icon_url": str(guild.icon.url) if guild.icon else "Aucun",  # URL de l'icône
        "verification_level": guild.verification_level.name,  # Niveau de vérification
        "security_settings": {
            "explicit_content_filter": guild.explicit_content_filter.name,  # Filtrage de contenu explicite
            "default_message_notifications": guild.default_notifications.name  # Paramètres de notifications
        }
        
    }

    save_data(data)
    return data["servers"][guild_id]

# FETCH / UPDATE LES INFOS D'UN USER
def fetch_user_data(member: discord.Member):
    data = load_data()
    user_id = str(member.id)

    if "users" not in data:
        data["users"] = {}

    if user_id not in data["users"]:
        data["users"][user_id] = {}

    avatar_url = str(member.avatar.url) if member.avatar else "Aucune"
    
    data["users"][user_id] = {
        "id": member.id,
        "name": member.name,
        #"discriminator": member.discriminator,
        "nickname": member.nick or "Aucun",
        "created_at": str(member.created_at),
        "joined_at": str(member.joined_at) if member.joined_at else "Inconnu",
        "roles": [role.name for role in member.roles if role.name != "@everyone"],
        "avatar_url": avatar_url,
        
    }

    save_data(data)
    return data["users"][user_id]

##################################################################################################
                #COMMANDES DATA

#  PRINT SERVER INFO
@bot.command()
async def server(ctx):
    server_data = fetch_server_data(ctx.guild)

    embed = discord.Embed(title=f"Infos du serveur {ctx.guild.name}", color=discord.Color.gold())
    embed.set_thumbnail(url=server_data["icon_url"])
    embed.add_field(name="ID", value=server_data["id"], inline=False)
    embed.add_field(name="Propriétaire", value=server_data["owner"], inline=True)
    embed.add_field(name="Membres", value=server_data["member_count"], inline=True)
    embed.add_field(name="Créé le", value=server_data["created_at"], inline=False)
    embed.add_field(name="Nombre de rôles", value=server_data["roles_count"], inline=True)
    embed.add_field(name="Salons textuels", value=server_data["text_channels"], inline=True)
    embed.add_field(name="Salons vocaux", value=server_data["voice_channels"], inline=True)
    embed.add_field(name="Langue préférée", value=server_data["preferred_locale"], inline=False)

    await ctx.send(embed=embed)

#  PRINT USER INFO
@bot.command()
async def infos(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author  

    user_data = fetch_user_data(member)

    embed = discord.Embed(title=f"Infos de {member.name}", color= COULEUR_EMBED_INFO)   #discord.Color.blue())
    embed.set_thumbnail(url=user_data["avatar_url"])
    embed.add_field(name="ID", value=user_data["id"], inline=False)
    embed.add_field(name="Pseudo Global", value=user_data["name"], inline=True)
    #embed.add_field(name="Discriminateur", value=user_data["discriminator"], inline=True)
    embed.add_field(name="Pseudo de Serveur", value=user_data["nickname"], inline=False)
    embed.add_field(name="Compte créé le", value=user_data["created_at"], inline=False)
    embed.add_field(name="A rejoint le", value=user_data["joined_at"], inline=False)
    embed.add_field(name="Rôles Sur le Serveur" , value=", ".join(user_data["roles"]) if user_data["roles"] else "Aucun", inline=False)
    
    await ctx.send(embed=embed)

# ➜ FAIRE BACKUP
@bot.command()
async def backup(ctx):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"database_backup_{timestamp}.json"
    shutil.copy(DATA_FILE, backup_file)
    await ctx.send(f"Base de données sauvegardée sous le nom {backup_file}.")
    
# FETCH ALL
@bot.command()
async def fetchall(ctx):
    """Met à jour tous les utilisateurs du serveur"""
    guild = ctx.guild
    members = guild.members  # Récupère tous les membres du serveur
    total = len(members)

    for member in members:
        fetch_user_data(member)  # Met à jour les données de chaque membre

    await ctx.send(f"✅ {total} utilisateurs mis à jour dans la base de données !")
##################################################################################################

#               COMMANDES DE GESTION 

@bot.command()
async def status(ctx, *, new_status: str):
    await bot.change_presence(activity=discord.Game(name=new_status))
    await ctx.send(f"Le statut a été changé en: {new_status}")
    
##################################################################################################

                #COMMANDES DIVERS

#PING

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latence en millisecondes
    await ctx.send(f"🏓** Pong ! Latence : {latency}ms**")
    
    

##################################################################################################

#               EVENT DU  BOT

# ➜ Mise à jour automatique des infos serveur au démarrage
@bot.event
async def on_ready():
    for guild in bot.guilds:
        fetch_server_data(guild)
            
    print("✅ Infos des serveurs mises à jour !")
    
    await bot.change_presence(activity=discord.Game(name=""))
    print(f'Bot {bot.user} Est prêt a tout défonder')
    

# ➜ Mise à jour des infos serveur lors d'un changement
@bot.event
async def on_guild_update(before, after):
    fetch_server_data(after)
    print(f"🔄 Mise à jour du serveur {after.name} ({after.id})")
    

# ➜ Mise à jour quand un membre rejoint
@bot.event
async def on_member_join(member):
    fetch_server_data(member.guild)
    fetch_user_data(member)
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"Bienvenue {member.mention} sur {member.guild.name} !")

@bot.event
async def on_member_remove(member):
    fetch_server_data(member.guild)

##################################################################################################

#GESTION DES ERREURS 
#@bot.event
#async def on_command_error(ctx, error):
 #   if isinstance(error, commands.CommandNotFound):
  #      await ctx.send("Cette commande n'existe pas.")
        
##################################################################################################
bot.run(TOKEN) # Faut Démarrer le bot quand même zebi
##################################################################################################