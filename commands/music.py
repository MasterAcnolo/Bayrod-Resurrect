from imports import *
from variables import *


queue = []
def Music(bot):
    @bot.command()
    async def join(ctx):
        """Commande pour faire rejoindre le bot dans un salon vocal"""
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            if ctx.voice_client:
                await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()
        else:
            await ctx.send("Tu dois être dans un salon vocal pour utiliser cette commande !")


    @bot.command()
    async def play(ctx, *, search: str):
        """Commande pour jouer une musique"""
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            return await ctx.send("Tu dois être dans un salon vocal pour jouer une musique !")

        if not ctx.voice_client:
            await voice_channel.connect()

        async with ctx.typing():
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f"ytsearch:{search}", download=False)

                
                if 'entries' not in info or not info['entries']:
                    return await ctx.send("❌ Aucune musique trouvée pour cette recherche !")

                info = info['entries'][0]  
                url = info['url']
                title = info['title']
                queue.append((url, title))
                await ctx.send(f"🎵 Ajouté à la file d'attente : **{title}**")

        if not ctx.voice_client.is_playing():
            await play_next(ctx)



    async def play_next(ctx):
        """Joue la musique suivante dans la file d'attente"""
        if queue:
            url, title = queue.pop(0)
            source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
            ctx.voice_client.play(source, after=lambda _: asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop))
            await ctx.send(f"▶️ Lecture en cours : **{title}**")
        else:
            await ctx.send("📭 La file d'attente est vide !")


    @bot.command()
    async def skip(ctx):
        """Commande pour passer à la musique suivante"""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("⏭ Musique passée !")
        else:
            await ctx.send("Aucune musique en cours de lecture.")


    @bot.command()
    async def leave(ctx):
        """Commande pour déconnecter le bot du salon vocal"""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("👋 Déconnecté du salon vocal.")
        else:
            await ctx.send("Je ne suis pas dans un salon vocal.")

    @bot.command()
    async def queue_command(ctx):
        if not queue:  
            return await ctx.send("📭 La file d'attente est vide.")

       
        queue_text = "\n".join(f"{i+1}. {title}" for i, (_, title) in enumerate(queue))

        await ctx.send(f"🎶 **Musiques à venir**\n{queue_text}")
    @bot.commmand()
    async def shuffle(ctx):
        if queue:
            queue = queue.join()