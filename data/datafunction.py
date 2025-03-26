import json
import os
import discord


# Dossiers de stockage des bases de données
BASE_SERVERS_DIR = "data/servers"
BASE_USERS_DIR = "data/users"

# 📌 Charger les données d'un serveur
def load_server_data(guild_id):
    server_file = os.path.join(BASE_SERVERS_DIR, f"{guild_id}.json")
    
    if os.path.exists(server_file):
        with open(server_file, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# 💾 Sauvegarder les données d'un serveur
def save_server_data(guild_id, data):
    os.makedirs(BASE_SERVERS_DIR, exist_ok=True)  # Assure que le dossier existe
    server_file = os.path.join(BASE_SERVERS_DIR, f"{guild_id}.json")

    with open(server_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 📊 Récupérer ou mettre à jour les infos d'un serveur
def fetch_server_data(guild: discord.Guild):
    guild_id = str(guild.id)
    data = load_server_data(guild_id)

    data = {
        "id": guild.id,
        "name": guild.name,
        "owner": guild.owner.name if guild.owner else "Inconnu",
        "member_count": guild.member_count,
        "created_at": str(guild.created_at),
        "text_channels": len(guild.text_channels),
        "voice_channels": len(guild.voice_channels),
        "roles_count": len(guild.roles),
        "preferred_locale": guild.preferred_locale,
        "icon_url": str(guild.icon.url) if guild.icon else "Aucun",
        "verification_level": guild.verification_level.name,
        "security_settings": {
            "explicit_content_filter": guild.explicit_content_filter.name,
            "default_message_notifications": guild.default_notifications.name
        }
    }

    save_server_data(guild_id, data)
    return data

# 📌 Charger les données d'un utilisateur
def load_user_data(user_id):
    user_file = os.path.join(BASE_USERS_DIR, f"{user_id}.json")
    
    if os.path.exists(user_file):
        with open(user_file, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# 💾 Sauvegarder les données d'un utilisateur
def save_user_data(user_id, data):
    os.makedirs(BASE_USERS_DIR, exist_ok=True)  # Assure que le dossier existe
    user_file = os.path.join(BASE_USERS_DIR, f"{user_id}.json")

    with open(user_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 🧑‍💻 Récupérer ou mettre à jour les infos d'un utilisateur
def fetch_user_data(member: discord.Member):
    data = load_user_data()
    user_id = str(member.id)

    if "users" not in data:
        data["users"] = {}

    if user_id not in data["users"]:
        data["users"][user_id] = {}

    avatar_url = str(member.avatar.url) if member.avatar else "Aucune"

    # Récupérer les serveurs où l'utilisateur est présent
    mutual_guilds = [guild.name for guild in member.mutual_guilds]

    data["users"][user_id] = {
        "id": member.id,
        "name": member.name,
        "nickname": member.nick or "Aucun",
        "created_at": str(member.created_at),
        "joined_at": str(member.joined_at) if member.joined_at else "Inconnu",
        "roles": [role.name for role in member.roles if role.name != "@everyone"],
        "avatar_url": avatar_url,
        "servers": mutual_guilds,  # Ajout de la liste des serveurs
    }

    save_user_data(data)
    return data["users"][user_id]