##################################################
                                                      
import os                                         
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import shutil
from datetime import datetime

#################################################


# Charger le fichier .env contenant le TOKEN
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Activer les intents nécessaires
intents = discord.Intents.default()
intents.message_content = True  
intents.members = True  

# Initialiser le bot
prefix = ';'
bot = commands.Bot(command_prefix=prefix, intents=intents)

#################################################

# ID du canal de bienvenue
WELCOME_CHANNEL_ID = 1347277296788177037

# Fichier de la base de données
DATA_FILE = "database.json"


#################################################

# 📂 Charger les données existantes
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# 💾 Sauvegarder les données mises à jour
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 🔄 Fonction pour récupérer/mettre à jour les infos du serveur
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
        "preferred_locale": guild.preferred_locale
    }

    save_data(data)
    return data["servers"][guild_id]

# 🔄 Fonction pour récupérer/mettre à jour les données d'un utilisateur
def fetch_user_data(member: discord.Member):
    data = load_data()
    user_id = str(member.id)

    if "users" not in data:
        data["users"] = {}

    if user_id not in data["users"]:
        data["users"][user_id] = {}

    data["users"][user_id] = {
        "id": member.id,
        "name": member.name,
        "discriminator": member.discriminator,
        "nickname": member.nick or "Aucun",
        "created_at": str(member.created_at),
        "joined_at": str(member.joined_at) if member.joined_at else "Inconnu",
        "roles": [role.name for role in member.roles if role.name != "@everyone"]
    }

    save_data(data)
    return data["users"][user_id]

# ➜ Commande pour afficher les infos du serveur
@bot.command()
async def server(ctx):
    server_data = fetch_server_data(ctx.guild)

    embed = discord.Embed(title=f"Infos du serveur {ctx.guild.name}", color=discord.Color.gold())
    embed.add_field(name="ID", value=server_data["id"], inline=False)
    embed.add_field(name="Propriétaire", value=server_data["owner"], inline=True)
    embed.add_field(name="Membres", value=server_data["member_count"], inline=True)
    embed.add_field(name="Créé le", value=server_data["created_at"], inline=False)
    embed.add_field(name="Nombre de rôles", value=server_data["roles_count"], inline=True)
    embed.add_field(name="Salons textuels", value=server_data["text_channels"], inline=True)
    embed.add_field(name="Salons vocaux", value=server_data["voice_channels"], inline=True)
    embed.add_field(name="Langue préférée", value=server_data["preferred_locale"], inline=False)

    await ctx.send(embed=embed)

# ➜ Commande pour afficher les infos d'un membre
@bot.command()
async def infos(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author  

    user_data = fetch_user_data(member)

    embed = discord.Embed(title=f"Infos de {member.name}", color=discord.Color.blue())
    embed.add_field(name="ID", value=user_data["id"], inline=False)
    embed.add_field(name="Nom", value=user_data["name"], inline=True)
    embed.add_field(name="Discriminateur", value=user_data["discriminator"], inline=True)
    embed.add_field(name="Pseudo", value=user_data["nickname"], inline=False)
    embed.add_field(name="Compte créé le", value=user_data["created_at"], inline=False)
    embed.add_field(name="A rejoint le", value=user_data["joined_at"], inline=False)
    embed.add_field(name="Rôles", value=", ".join(user_data["roles"]) if user_data["roles"] else "Aucun", inline=False)

    await ctx.send(embed=embed)

# ➜ Mise à jour automatique des infos serveur au démarrage
@bot.event
async def on_ready():
    for guild in bot.guilds:
        fetch_server_data(guild)
    print("✅ Infos des serveurs mises à jour !")

# ➜ Mise à jour des infos serveur lors d'un changement
@bot.event
async def on_guild_update(before, after):
    fetch_server_data(after)
    print(f"🔄 Mise à jour du serveur {after.name} ({after.id})")

# ➜ Mise à jour quand un membre rejoint ou quitte
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

# ➜ Commande pour faire une sauvegarde de la base
@bot.command()
async def backup(ctx):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"database_backup_{timestamp}.json"
    shutil.copy(DATA_FILE, backup_file)
    await ctx.send(f"Base de données sauvegardée sous le nom {backup_file}.")
    
# Commande pour fetch les datas de tout le monde
@bot.command()
async def fetchall(ctx):
    """Met à jour tous les utilisateurs du serveur"""
    guild = ctx.guild
    members = guild.members  # Récupère tous les membres du serveur
    total = len(members)

    for member in members:
        fetch_user_data(member)  # Met à jour les données de chaque membre

    await ctx.send(f"✅ {total} utilisateurs mis à jour dans la base de données !")


# ➜ Commande pour afficher les commandes
@bot.command()
async def commands(ctx):
    embed = discord.Embed(
        title="💻 **Menu des commandes** 💻",
        description=f"📂 Commandes Disponibles: XX\n♦️Le Préfix du Serveur est **{prefix}**\n☕️ En savoir plus avec : **{prefix}maj**" + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Publiques: \n ```test```",
        color=0x001eff
    )
    await ctx.send(embed=embed)

#commande de ping
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latence en millisecondes
    await ctx.send(f"🏓** Pong ! Latence : {latency}ms**")
    
    
# ➜ Démarrer le bot
bot.run(TOKEN)
