import shutil
import os
from datetime import datetime
import zipfile
from variables import AUTHORIZED_USER_ID

def backup_commands(bot):
    @bot.command()
    async def backup(ctx):
        if ctx.author.id == AUTHORIZED_USER_ID:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_filename = f"database_backup_{timestamp}.zip"
            
            # 📂 Créer un dossier temporaire pour la sauvegarde
            backup_folder = f"backup_temp_{timestamp}"
            os.makedirs(backup_folder, exist_ok=True)

            # 📀 Copier les fichiers de data/servers et data/users
            for folder in ["data/servers", "data/users"]:
                if os.path.exists(folder):
                    for file in os.listdir(folder):
                        file_path = os.path.join(folder, file)
                        if file.endswith(".json"):
                            shutil.copy(file_path, backup_folder)

            # 🗜️ Créer un fichier ZIP contenant toutes les données
            with zipfile.ZipFile(backup_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                for file in os.listdir(backup_folder):
                    zipf.write(os.path.join(backup_folder, file), file)

            # 🗑️ Supprimer le dossier temporaire
            shutil.rmtree(backup_folder)

            await ctx.send(f"📦 Base de données sauvegardée sous `{backup_filename}`.")
        
        else: 
            await ctx.send("❌ Désolé, tu n'es pas autorisé à exécuter cette commande.")
