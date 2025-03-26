import discord

def quoi(bot):
    @bot.tree.command(name="quoi", description="Oui ?")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Feur")
