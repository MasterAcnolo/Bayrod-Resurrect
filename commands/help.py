from discord.ext import commands
import discord
from variables import prefix

def help_commands(bot):
    @bot.command()
    async def commands(ctx):
        embed = discord.Embed(
            title="💻 **Menu des commandes** 💻",
            description=f"📂 Commandes Disponibles: XX\n♦️Le Préfix du Serveur est **{prefix}**\n☕️ En savoir plus avec : **{prefix}maj**" + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Fetch Info: \n ```infos[@member],fetchall, server,update, backup```",
            color=0x001eff
        )
        embed.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Divers",value="```ping, ```", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n Commandes Admin",value="```null, ```",inline=False)

        await ctx.send(embed=embed)