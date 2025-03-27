import discord
from variables import *
from imports import *

control_mode = False

def start_control(bot):
    @bot.command()
    async def start_control(ctx):
        """Active le mode de contrôle"""
        global control_mode
        control_mode = True
        await ctx.send("✅ Mode contrôle activé !")

def stop_control(bot):
    @bot.command()
    async def stop_control(ctx):
        """Désactive le mode de contrôle"""
        global control_mode
        control_mode = False
        await ctx.send("❌ Mode contrôle désactivé !")

def on_message(bot):
    @bot.event
    async def on_message(message):
        global control_mode
        
        
        if message.author == bot.user:
            return

        
        if control_mode and message.channel.id == CONTROL_INPUT_CHANNEL_ID:
            target_channel = bot.get_channel(CONTROL_OUTPUT_CHANNEL_ID)
            if target_channel:
                await target_channel.send(f" {message.content}") #📢 **{message.author}:**
        
        
        await bot.process_commands(message)
