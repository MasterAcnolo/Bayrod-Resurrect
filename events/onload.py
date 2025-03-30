import discord
from data.datafunction import * 
from variables import * 

def onload(bot):
    @bot.event
    async def on_ready():
        for guild in bot.guilds:
            fetch_server_data(guild)
        if DEBUG_MODE == True:        
            print("Infos des serveurs mises à jour ! ✅")
        
        await bot.change_presence(activity=discord.Game(name="Getting Better Every Day")) 
        if DEBUG_MODE == True:
            print(f'Statut chargé ✅')
            await bot.change_presence(activity=discord.Game(name="DEBUG MODE")) #Getting Better Every Day
            print(debug_ascii)
        else:
            print(text_art)
        print(f'Bonjour Maître, {bot.user} Est prêt a vous servir')
        
        
    