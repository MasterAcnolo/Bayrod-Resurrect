import discord

def get_messages(bot):
    @bot.command()
    async def catchmessage(ctx):
        async for message in ctx.channel.history(limit=10, before=ctx.message):
            print(f"{message.author}: {message.content}")
            
        await ctx.send(f"**Messages Fetch** ✅")
