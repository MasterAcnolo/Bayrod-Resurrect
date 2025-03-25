import discord
from data.datafunction import fetch_server_data, fetch_user_data


def onload(bot):
    @bot.event
    async def on_ready():
        for guild in bot.guilds:
            fetch_server_data(guild)
                
        print("Infos des serveurs mises à jour ! ✅")
        
        await bot.change_presence(activity=discord.Game(name="Fetch des datas")) #Getting Better Every Day
        print(f'Statut chargé ✅')
        print(f'Bonjour Maître, {bot.user} Est prêt a vous servir')
        
        
