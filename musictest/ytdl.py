import discord
from discord.ext import commands
import yt_dlp as youtube_dl
from discord import FFmpegPCMAudio
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="ba", intents=intents)

# Paramètres de youtube-dl/yt-dlp
ytdl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioquality': 1,
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,  # Désactive les playlists
    'quiet': True
}

ffmpeg_opts = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

# Commande pour jouer de la musique
@bot.command()
async def play(ctx, *, search: str):
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()

    # Rechercher l'URL de la chanson
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)
        url2 = info['entries'][0]['url']
        song = FFmpegPCMAudio(url2, **ffmpeg_opts)
        voice_client.play(song, after=lambda e: print('done', e))

    await ctx.send(f"Je joue maintenant : {info['entries'][0]['title']}")

# Commande pour arrêter la musique
@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    await voice_client.disconnect()

# Commande pour faire une pause
@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.pause()

# Commande pour reprendre la musique
@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_paused():
        voice_client.resume()

# Lancer le bot
bot.run('TOKEN')
