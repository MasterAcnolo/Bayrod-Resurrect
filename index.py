import os
from dotenv import load_dotenv
import discord
# Importations des Librairies

load_dotenv() #Charge le Fichier du Token 

intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)


prefix = ';' #Changement du Préfixe

@client.event
async def on_ready():
    print(f'Connecté en tant que: {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Le Retour de Bayrod"))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith(prefix + "Spicy"):
        await message.channel.send("Fire ! ")
        
    if message.content.startswith(prefix + "ping"):
        await message.channel.send(f'Ping de **{round(client.latency * 1000)}ms**')

#Connection au bot avec le Token dans le fichier env

token = os.getenv("TOKEN")  
print(f"Mon token est : {token}")  

client.run(token)