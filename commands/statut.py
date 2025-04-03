import discord
from discord.ext import commands
from variables import *

def status_command(bot):
    @bot.command()
    async def status(ctx, *, new_status: str):
        if ctx.author.id == AUTHORIZED_USER_ID:
            
            await bot.change_presence(activity=discord.Game(name=new_status))
            await ctx.send(f"Le statut a été changé en: {new_status}")
        else:
            await ctx.send("Désolé, tu n'es pas autorisé à exécuter cette comamande")
            
            
            