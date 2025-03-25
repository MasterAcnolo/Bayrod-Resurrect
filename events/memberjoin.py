import discord
from data.datafunction import *
from variables import WELCOME_CHANNEL_ID

def member_join(bot):
    @bot.event
    async def on_member_join(member):
        fetch_server_data(member.guild)
        fetch_user_data(member)
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Bienvenue {member.mention} sur {member.guild.name} !")
