import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import shutil
from datetime import datetime

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

# ID du canal de bienvenue
WELCOME_CHANNEL_ID = 1347277296788177037

# Fichier de la base de données
DATA_FILE = "database.json"

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

# 🔄 Fonction pour récupérer/mettre à jour les données d'un utilisateur
def fetch_user_data(member: discord.Member):
    data = load_data()
    user_id = str(member.id)

    # Si l'utilisateur n'est pas enregistré, on ajoute tout
    if user_id not in data:
        data[user_id] = {}

    # Ajout/Mise à jour des informations
    data[user_id]["id"] = member.id
    data[user_id]["name"] = member.name
    data[user_id]["discriminator"] = member.discriminator
    data[user_id]["nickname"] = member.nick or "Aucun"
    data[user_id]["created_at"] = str(member.created_at)
    data[user_id]["joined_at"] = str(member.joined_at) if member.joined_at else "Inconnu"
    data[user_id]["roles"] = [role.name for role in member.roles if role.name != "@everyone"]

    save_data(data)  # Sauvegarde après mise à jour
    return data[user_id]

# ➜ Commande pour afficher les infos (et fetch si manquantes)
@bot.command()
async def infos(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author  # Si aucun membre n'est précisé, utiliser l'auteur

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

# ➜ Commande pour mettre à jour les infos d'un utilisateur
@bot.command()
async def update(ctx, member: discord.Member):
    user_data = fetch_user_data(member)
    await ctx.send(f"Les informations de {member.name} ont été mises à jour !")

# ➜ Commande pour lister tous les utilisateurs enregistrés
@bot.command()
async def list_users(ctx):
    data = load_data()
    if not data:
        await ctx.send("Aucun utilisateur enregistré.")
        return
    
    user_list = "\n".join([f"{user_data['name']}#{user_data['discriminator']} ({user_id})" for user_id, user_data in data.items()])
    await ctx.send(f"**Utilisateurs enregistrés :**\n{user_list}")

# ➜ Commande pour supprimer un utilisateur de la base
@bot.command()
async def delete(ctx, member: discord.Member):
    data = load_data()
    user_id = str(member.id)

    if user_id in data:
        del data[user_id]
        save_data(data)
        await ctx.send(f"Les informations de {member.name} ont été supprimées de la base.")
    else:
        await ctx.send(f"{member.name} n'est pas dans la base de données.")

# ➜ Commande pour faire une sauvegarde de la base
@bot.command()
async def backup(ctx):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"database_backup_{timestamp}.json"
    shutil.copy(DATA_FILE, backup_file)
    await ctx.send(f"Base de données sauvegardée sous le nom {backup_file}.")

# ➜ Événement quand un membre rejoint
@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"Bienvenue {member.mention} sur {member.guild.name} !")

    # Mise à jour des infos du membre
    user_data = fetch_user_data(member)
    print(f"📌 Données mises à jour pour {member.name} : {user_data}")


# Commande pour afficher un embed avec des infos personnalisées
@bot.command()
async def stats(ctx):
    # Paramètres personnalisés
    server_name = ctx.guild.name
    member_count = ctx.guild.member_count
    owner_name = ctx.guild.owner.name
    preferred_locale = ctx.guild.preferred_locale  # Remplacement de la région
    created_at = ctx.guild.created_at.strftime("%d/%m/%Y")
    description = "Voici les informations du serveur."

    # Création de l'embed
    embed = discord.Embed(
        title=f"Statistiques du serveur {server_name}",
        description=description,
        color=discord.Color.blue()  # Vous pouvez aussi utiliser discord.Color.green(), .red(), etc.
    )

    # Ajout des champs personnalisés
    embed.add_field(name="Nom du serveur", value=server_name, inline=False)
    embed.add_field(name="Propriétaire", value=owner_name, inline=True)
    embed.add_field(name="Locale préférée", value=preferred_locale, inline=True)
    embed.add_field(name="Nombre de membres", value=member_count, inline=True)
    embed.add_field(name="Créé le", value=created_at, inline=False)

    # Envoi de l'embed dans le canal où la commande a été tapée
    await ctx.send(embed=embed)

# Liste des commandes

@bot.command()
async def commands(ctx):
    # Création de l'embed
    embed = discord.Embed(
        title="**📂 Commandes Disponibles: XX**",  # Titre de l'embed
        description="💻 **Menu des commandes** 💻 \nLe Préfix du Serveur est **" + prefix + "**",  # Description de l'embed
        color=0x001eff  # Couleur de l'embed
    )

    embed.set_author(name="Bayrod")
    #embed.set_thumbnail(url=) <-- Icone de Bayrod a rajouter
    #embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Le Préfix du Serveur est **" + prefix + "**",value="",inline=False)
    embed.add_field(name ="☕️ En savoir plus sur la mise à jour avec : **" + prefix + "maj**", value="",inline=False)

    # Envoi de l'embed dans le canal où la commande a été tapée
    await ctx.send(embed=embed)

    
# ➜ Démarrer le bot
bot.run(TOKEN)
