from imports import *


# Le Format d'importation est dossier.fichier import LES FONCTIONS


load_dotenv()
TOKEN = os.getenv("TOKEN")

# ICI ON ACTIVE LES INTENTS (Autorisation du bot)
intents = discord.Intents.default()
intents.message_content = True  
intents.members = True  

prefix = ';'
WELCOME_CHANNEL_ID = 1347277296788177037 # <-- Sur 'SERVEUR DE TEST' ACTUELLEMENT
DATA_FILE = "database.json" # <-- PATH DE LA BASE DE DONNEES

COULEUR_EMBED_INFO = 0xff1100
AUTHORIZED_USER_ID = 724954095042953246

bot = commands.Bot(command_prefix=prefix, intents=intents) # <-- Le Nom du bot c'est 'bot'. Si on veut le modifier faut changer tous le code pour remplacer bot --> NOM DU BOT


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


bot.run("TOKEN")
    