import discord
from discord.ext.commands.errors import CommandNotFound

def antierror(bot):
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send(f"Commande inconnue : **{ctx.message.content}**.\nFaîtes **;commands** pour obtenir la liste des commandes")
            