from variables import * # Importations de tous ce qu'il y à dans variables.py

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

from events.messagedelete import *
from events.onload import *
from events.guildupdate import *
from events.memberjoin import *
from events.memberremove import *
from data.getmessage import *

from commands.data import *
from commands.help import *
from commands.statut import * 
from commands.divers import *
from commands.error import *
