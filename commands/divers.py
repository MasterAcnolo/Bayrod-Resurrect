import discord
from discord.ext import commands

def ping_command(bot):
    @bot.command()
    async def ping(ctx):
        latency = round(bot.latency * 1000)  # Latence en millisecondes
        await ctx.send(f"🏓** Pong ! Latence : {latency}ms**")
        

def quoi_command(bot):

    @bot.tree.command(name="quoi", description="Oui ?")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Feur")
