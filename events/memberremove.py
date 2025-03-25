import discord
from data.datafunction import *

def member_remove(bot):
        
    @bot.event
    async def on_member_remove(member):
        fetch_server_data(member.guild)
            