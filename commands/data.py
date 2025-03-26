from imports import *
from variables import *
from data.datafunction import fetch_server_data, fetch_user_data
import discord
from discord.ext import commands
from datetime import datetime
import shutil

def server_commands(bot):
    @bot.command()
    async def server(ctx):
            server_data = fetch_server_data(ctx.guild)

            embed = discord.Embed(title=f"Infos du serveur {ctx.guild.name}", color=discord.Color.gold())
            embed.set_thumbnail(url=server_data["icon_url"])
            embed.add_field(name="ID", value=server_data["id"], inline=False)
            embed.add_field(name="Propriétaire", value=server_data["owner"], inline=True)
            embed.add_field(name="Membres", value=server_data["member_count"], inline=True)
            embed.add_field(name="Créé le", value=server_data["created_at"], inline=False)
            embed.add_field(name="Nombre de rôles", value=server_data["roles_count"], inline=True)
            embed.add_field(name="Salons textuels", value=server_data["text_channels"], inline=True)
            embed.add_field(name="Salons vocaux", value=server_data["voice_channels"], inline=True)
            embed.add_field(name="Langue préférée", value=server_data["preferred_locale"], inline=False)

            await ctx.send(embed=embed)
            


def infos_commands(bot):
    @bot.command()
    async def infos(ctx, member: discord.Member = None):
        if not member:
            member = ctx.author  

        user_data = fetch_user_data(member)

        embed = discord.Embed(title=f"Infos de {member.name}", color= COULEUR_EMBED_INFO)   #discord.Color.blue())
        embed.set_thumbnail(url=user_data["avatar_url"])
        embed.add_field(name="ID", value=user_data["id"], inline=False)
        embed.add_field(name="Pseudo Global", value=user_data["name"], inline=True)
        #embed.add_field(name="Discriminateur", value=user_data["discriminator"], inline=True) Ca sert plus à rien le #
        embed.add_field(name="Pseudo de Serveur", value=user_data["nickname"], inline=False)
        embed.add_field(name="Compte créé le", value=user_data["created_at"], inline=False)
        embed.add_field(name="A rejoint le", value=user_data["joined_at"], inline=False)
        embed.add_field(name="Rôles Sur le Serveur" , value=", ".join(user_data["roles"]) if user_data["roles"] else "Aucun", inline=False)
            
        await ctx.send(embed=embed)
        
        
# def backup_commands(bot):
#     @bot.command()
#     async def backup(ctx):
#         if ctx.author.id == AUTHORIZED_USER_ID:
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             backup_file = f"database_backup_{timestamp}.json"
#             shutil.copy(DATA_FILE, backup_file)
#             await ctx.send(f"Base de données sauvegardée sous le nom {backup_file}.")
        
#         else: 
#             await ctx.send("Désolé, tu n'es pas autorisé à exécuter cette commande.")

def fetch_all_commands(bot):
    @bot.command()
    async def fetchall(ctx):
        if ctx.author.id == AUTHORIZED_USER_ID:
            guild = ctx.guild
            members = guild.members  
            total = len(members)
            if DEBUG_MODE == True:
                print(f"Nombre total de membres à traiter: {total}")  

            
            updated_count = 0

            if DEBUG_MODE == True:
                for member in members:
                    print(f"Traitement de {member.name} ({member.id})")  
                    result = fetch_user_data(member)  
                    if result:
                        updated_count += 1  

                
            await ctx.send(f"✅ {updated_count} utilisateurs sur {total} ont été mis à jour dans la base de données !")
        else:
            await ctx.send("Désolé, tu n'es pas autorisé à exécuter cette commande.")
            

def fetch_user_id_command(bot):
    @bot.command()
    async def id(ctx, user_id: str):
        username = get_username_by_id(user_id)
        
        if username:
            await ctx.send(f"🔎 L'utilisateur avec l'ID `{user_id}` est <@{user_id}>.", 
                           allowed_mentions=discord.AllowedMentions(users=False))
        else:
            await ctx.send(f"❌ Aucun utilisateur trouvé pour l'ID `{user_id}`.")