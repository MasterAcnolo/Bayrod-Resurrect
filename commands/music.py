from imports import *
from variables import *


queue = []
loop = False

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


    @bot.command()
    async def loop(ctx):
        """Commande pour activer/désactiver la boucle"""
        global loop
        loop = not loop
        status = "activé 🔁" if loop else "désactivé ❌"
        await ctx.send(f"🔄 Mode boucle {status}")
    @bot.command()
    async def play_next(ctx):
        """Joue la musique suivante ou répète la musique si le mode boucle est activé"""
        global loop
        if ctx.voice_client and ctx.voice_client.is_playing():
            return  # Empêche de jouer une nouvelle musique si déjà en cours

        if queue:
            url, title = queue[0] if loop else queue.pop(0)
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
    @bot.command()
    async def shuffle(ctx):
        """Commande pour mélanger la file d'attente"""
        if queue:
            random.shuffle(queue)
            await ctx.send("🔀 La file d'attente a été mélangée !")
        else:
            await ctx.send("📭 La file d'attente est vide.")
            
    @bot.command()
    async def nowplaying(ctx):
        """Commande pour afficher la musique en cours"""
        if ctx.voice_client and ctx.voice_client.is_playing():
            await ctx.send(f"🎵 Actuellement en train de jouer : **{queue[0][1]}**")
        else:
            await ctx.send("Aucune musique en cours de lecture.")
            
    @bot.command()
    async def clear(ctx):
            """Commande pour vider complètement la file d'attente"""
            global queue
            queue.clear()
            await ctx.send("🗑 La file d'attente a été vidée.")
            
    @bot.command()
    async def remove(ctx, index: int):
        """Commmande pour retirer une musique dans la file d'attente"""
        if 1 <= index <= len(queue):
            removed_song = queue.pop(index - 1)
            await ctx.send(f'Musique Retirée: **{removed_song[1]}**')
        else:
            await ctx.send("Numéro Invalide, Vérifie la fille d'attente avec" + prefix + "queue_commands")
            
    @bot.command()
    async def pause(ctx):
        """Commande pour mettre la musique en pause"""
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("⏸ Musique mise en pause.")
        else:
            await ctx.send("Aucune musique en cours de lecture.")

    @bot.command()
    async def resume(ctx):
        """Commande pour reprendre la musique en pause"""
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("▶️ Musique reprise.")
        else:
            await ctx.send("Aucune musique en pause.")