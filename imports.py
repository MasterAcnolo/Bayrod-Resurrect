# Les Différentes libs

import os                                         
import discord

from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound 

from dotenv import load_dotenv #Pour charger le token du .env

import shutil #Utiliser pour la BDD
import json

from datetime import datetime


# IMPORTATION DES FICHIERS EXTERNES 

# Le Format d'importation est dossier.fichier import LES FONCTIONS
from data.datafunction import fetch_server_data, fetch_user_data, save_data, load_data
from commands.datacommands import * 
from commands.help import *