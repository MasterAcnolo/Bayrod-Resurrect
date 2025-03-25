import discord
from data.datafunction import *

def guild_update(bot):
    @bot.event
    async def on_guild_update(before, after):
        fetch_server_data(after)
        print(f"🔄 Mise à jour du serveur {after.name} ({after.id})")
        
