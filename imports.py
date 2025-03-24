import os                                         
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import shutil
from datetime import datetime
from discord.ext.commands.errors import CommandNotFound 


from data.function import fetch_server_data, fetch_user_data
