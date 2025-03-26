import json
import os
from data.datafunction import * 

DIRECTORY_FILE = "data/user_directory.json"


def load_user_directory():
    if os.path.exists(DIRECTORY_FILE):
        with open(DIRECTORY_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Erreur de décodage JSON dans l'annuaire.")
                return {}
    else:
        print("Aucun fichier d'annuaire trouvé.")
    return {}

def save_user_directory(data):
    os.makedirs("data", exist_ok=True)  # Crée le dossier s'il n'existe pas
    with open(DIRECTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_user_to_directory(user_id, username):
    directory = load_user_directory()
   
    if user_id not in directory:
        directory[user_id] = username
        save_user_directory(directory)
        print(f"Utilisateur {username} ajouté à l'annuaire.")  # Debug
    else:
        print(f"L'utilisateur {username} existe déjà dans l'annuaire.")  # Debug


def update_user_in_directory(user_id, username):
    directory = load_user_directory()

    if user_id in directory:
        directory[user_id] = username
        save_user_directory(directory)
        print(f"Utilisateur {username} mis à jour dans l'annuaire.")  # Debug
    else:
        print(f"L'utilisateur {username} n'existe pas dans l'annuaire.")  # Debug



def get_username_by_id(user_id):
    directory = load_user_directory()
    username = directory.get(user_id, None)
    
    if username:
        return username
    else:
        print(f"Aucun utilisateur trouvé pour l'ID {user_id}.")  # Debug
        return None
