import discord
from discord.ext import commands

def ping_command(bot):
    @bot.command()
    async def ping(ctx):
        latency = round(bot.latency * 1000)  # Latence en millisecondes
        await ctx.send(f"🏓** Pong ! Latence : {latency}ms**")
        
        