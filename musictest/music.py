import discord
from discord.ext import commands
import wavelink

TOKEN = "TON_BOT_TOKEN"  # Remplace par le token de ton bot
LAVALINK_HOST = "localhost"
LAVALINK_PORT = 2333
LAVALINK_PASSWORD = "1234"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="bayrod", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    await connect_lavalink()


async def connect_lavalink():
    """Connecte Lavalink au bot."""
    node = wavelink.Node(uri=f"http://{LAVALINK_HOST}:{LAVALINK_PORT}", password=LAVALINK_PASSWORD)
    await wavelink.Pool.connect(client=bot, nodes=[node])


@bot.command()
async def join(ctx):
    """Fait rejoindre le bot dans le salon vocal."""
    if ctx.author.voice is None:
        return await ctx.send("Tu dois être dans un salon vocal !")

    vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    return await ctx.send(f"Connecté à **{ctx.author.voice.channel.name}** !")


@bot.command()
async def play(ctx, *, search: str):
    """Joue une musique à partir d'une recherche YouTube."""
    if not ctx.voice_client:
        await ctx.invoke(join)

    vc: wavelink.Player = ctx.voice_client

    tracks = await wavelink.Playable.search(search)
    if not tracks:
        return await ctx.send("Aucun résultat trouvé.")

    track = tracks[0]  # Prend le premier résultat
    await vc.play(track)
    await ctx.send(f"🎵 Lecture : **{track.title}**")


@bot.command()
async def skip(ctx):
    """Passe à la musique suivante."""
    vc: wavelink.Player = ctx.voice_client
    if not vc or not vc.playing:
        return await ctx.send("Aucune musique en cours.")

    await vc.stop()
    await ctx.send("⏭️ Musique passée !")


@bot.command()
async def stop(ctx):
    """Arrête la musique et quitte le salon vocal."""
    vc: wavelink.Player = ctx.voice_client
    if not vc:
        return await ctx.send("Je ne suis pas dans un salon vocal.")

    await vc.disconnect()
    await ctx.send("👋 Déconnecté du salon vocal !")


@bot.command()
async def pause(ctx):
    """Met en pause la musique."""
    vc: wavelink.Player = ctx.voice_client
    if vc.is_playing():
        await vc.pause()
        await ctx.send("⏸️ Musique en pause.")


@bot.command()
async def resume(ctx):
    """Reprend la musique."""
    vc: wavelink.Player = ctx.voice_client
    if vc.is_paused():
        await vc.resume()
        await ctx.send("▶️ Reprise de la musique.")


bot.run("TOKEN")
