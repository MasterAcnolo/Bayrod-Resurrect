# database_handler.py

import json
import os
import discord

DATA_FILE = "data/data.json"

# Fonction pour récupérer les données de la base
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Fonction pour sauvegarder les données dans la base
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Fonction pour récupérer ou mettre à jour les infos d'un serveur
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
        "icon_url": str(guild.icon.url) if guild.icon else "Aucun",
        "verification_level": guild.verification_level.name,
        "security_settings": {
            "explicit_content_filter": guild.explicit_content_filter.name,
            "default_message_notifications": guild.default_notifications.name
        }
    }

    save_data(data)
    return data["servers"][guild_id]

# Fonction pour récupérer ou mettre à jour les infos d'un utilisateur
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
        "nickname": member.nick or "Aucun",
        "created_at": str(member.created_at),
        "joined_at": str(member.joined_at) if member.joined_at else "Inconnu",
        "roles": [role.name for role in member.roles if role.name != "@everyone"],
        "avatar_url": avatar_url,
    }

    save_data(data)
    return data["users"][user_id]
