import discord

def message_delete(bot):
    @bot.event
    async def on_message_delete(message):
       
        print(f"Message supprimé par {message.author.name}: {message.content} sur le serveur {message.guild.name}")