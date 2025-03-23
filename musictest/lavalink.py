import discord
import wavelink
from discord.ext import commands

# Configuration du bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

    # Connexion au serveur Lavalink
    await bot.wait_until_ready()
    
    # Créer un node Lavalink
    node = await wavelink.Node.connect(
        bot=bot,
        host='localhost',  # Lavalink local
        port=2333,
        password='your_password',  # Le mot de passe configuré dans application.yml
        identifier="your_identifier",  # Identifiant du node
        region="us_east"  # La région de ton serveur Lavalink
    )
    print(f"Node connecté : {node}")

@bot.command()
async def join(ctx):
    """Faire rejoindre le bot dans le canal vocal"""
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx, *, search: str):
    """Jouer une chanson depuis YouTube"""
    player = await wavelink.Player.get_player(ctx.guild)

    # Rechercher et jouer la chanson
    track = await wavelink.YouTubeTrack.search(search)
    await player.play(track)
    await ctx.send(f"Je joue : {track.title}")

@bot.command()
async def stop(ctx):
    """Arrêter la musique"""
    player = await wavelink.Player.get_player(ctx.guild)
    await player.stop()
    await ctx.send("La musique a été arrêtée.")

@bot.command()
async def leave(ctx):
    """Faire quitter le bot du canal vocal"""
    player = await wavelink.Player.get_player(ctx.guild)
    await player.disconnect()
    await ctx.send("Le bot a quitté le canal vocal.")

bot.run('TOKEN')
