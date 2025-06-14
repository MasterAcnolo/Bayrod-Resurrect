prefix = ';'
DEBUG_MODE = True


FFMPEG_OPTIONS = {'options': "-vn"}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}

COULEUR_EMBED_INFO = 0xff1100
AUTHORIZED_USER_ID = 724954095042953246


BASE_SERVERS_DIR = "data/servers"
BASE_USERS_DIR = "data/users"
DIRECTORY_FILE = "data/user_directory.json"
DATA_FILE = "data\database.json" # <-- PATH DE LA BASE DE DONNEES

CONTROL_OUTPUT_CHANNEL_ID = 1308806097880088668
CONTROL_INPUT_CHANNEL_ID = 1354693761313013902 
WELCOME_CHANNEL_ID = 1347277296788177037 # <-- Sur 'SERVEUR DE TEST' ACTUELLEMENT

ascii_art = """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*=====+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@#++**=-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*-=====#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*-+##*=-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*=======#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+@@@@@@@@@@@@@@@@=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+=-+@@@@@@@@@@@@@@@@+-=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=*#-#@@@@@@@@@@@@@@@@#-#*=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==*@@*-%@@@@@@@@@@@@@@@@%-*@@#==#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@*++%@@@@@@@@@#==#@@@@==@@@@@@@@@@@@@@@@@@==@@@@#==#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@+---*@@@@@@@%+=#@@@*#@-+@@@@@@@@@@@@@@@@@@+-@#*@@@#=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@+-++=#@@@@@@@==%@@%+-@#-#@@@@@@@@@@@@@@@@@@#-#@:+%@@%==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@%=--===#@@@@@@%-*@@#=:+@+-%@@@@@@%#++#%@@@@@@%-+@=:+#@@*-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@#==*##+-*@@@@@@%-*@%==:#@==@@@@#*==+##+==*#@@@@==@#:==%@*-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@%%@@@@@%@@@@@@@%-*@#==:%@-*@@*=+*%@@%%@@%*+=*@@*-@%:==#@*-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-*@#==:@#-#@+=%%#*++++++*#%%=+@#-#%:==#@*-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-%@%==:%%-**-%%++++****++++%%-**-%%:==%@%-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=@%@*=:+@*--#@+*#+******+#*+@#--*@=:=*@%@=+@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+@##@*-.+@**@**@@%@%**%@%@@*#@**@+.-*@##@+=@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@+=*@#=+@@@@@@@@=+@@+*@%=:=%@@+#@*#@***#@#*@#+@@%-:=%@*+@@+=@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@%-=%=-#@@@@@@@@*-%@%==#%*-:*%*%=-#@%**%@#-+%*%*:-#%#=+@@%-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@+-=-+@@@@@@@@@+-#@@@#=-=+=--#@*++%@##@%++#@#--=+=-=#@@@#-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@%==-%@@@@@@@@*-#@%%@@%#=:::::-#%%*****#%%#-:::::+#%@@%@@#-*@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@*-+@@@@@@@@%-+@@*+#%@%##*-:.:%%+*####**%%:.:-*##%@%*+*@@+-%@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@==%@@@@@@@@%-*@%+++#%%@%@@#=+@*+@*..*@+*@=+#@@%@%%*+++%@*-%@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@=+@%++**%%#%@@@%%@*+##==%#+#@%%@@@%#%#**++%@+=@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@==@%+++#%@%*%@@@%##*+*##*+*##%@@@%*@@%#+++%@==@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@==@@%#*#%@##@@@@@%**********@@@@@@##@%#*#%@%=+@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*=*+==%@@@@@@@*==#@@@%%##@@@--=*@@#*++*#@@*=--@@@##%%@@@#==*@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*-+%##%@@@@@@@%=+@@@@@##%@@%:.::-+#@@@@#*#-:.:%@@%##@@%@@+=%@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*-*@@@@@@@@%#+=*@@%*#@@%**@@:.=+*+*++++***#=.:@@+*%@@#*%@@*=+#%@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*-+@@@@@@@@#-+@@@%**+*%@@#@*....:-+-::-+=++...*@#@@#+***%@@@+-#@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@%#%@@@@@@@@@*-#@%****++%@@@#--==+=+-..-+=+*=--#@@@%++****%@#-*@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@*-#@#*+++*@%=--:-=+**#*##*#**+=-:--=%@+++**#@#-*@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@+=%@#*++#@@@%==+=+**#%%%%#*++=+==%@@@#++*#@%=+@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=%@#++@@@@@-:*+::---==--:::+*:-@@@@@++#@%=+@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@#*****#@@@@@@@@@==@@##@@#@@#.:+*:-=++++=-:*+:.#@@#@@##@@==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@+++++++@@@@@@@@@%=+@@@@%=@@+ .-+++=----=+++-. +@@=%@@@@+=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@==@@@==%@@@@@@@@@%-+@@@*-#@#:...::------::...:#@#-*@@@+-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@%==%@%==%@@@@@@@@@@#-*@@=-=@@@%+: ::....:-.:+%@@@=-=@@*-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@=-===-=@@@@@@@@@@@@#-**-*+=+#@@@%#%=..=%#%@@@#+=+*-**-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@%#####%@@@@@@@@@@@@@*-==@@%*+=+#@@@@@@@@@@#+=+*%@@==-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-#@@@@@@#+=+*%@@%*+=+#@@@@@@#-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@%*====*%@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@*-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@*+++=-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@++**++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@%==@@*=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@%=-++=-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@#*****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"""
text_art = """$$$$$$$\                                                $$\       $$$$$$$\             $$\           
$$  __$$\                                               $$ |      $$  __$$\            $$ |          
$$ |  $$ | $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$$ |      $$ |  $$ | $$$$$$\ $$$$$$\         
$$$$$$$\ | \____$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$ |      $$$$$$$\ |$$  __$$\\_$$  _|        
$$  __$$\  $$$$$$$ |$$ |  $$ |$$ |  \__|$$ /  $$ |$$ /  $$ |      $$  __$$\ $$ /  $$ | $$ |          
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\       
$$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$ |      \$$$$$$  |\$$$$$$$ |      $$$$$$$  |\$$$$$$  | \$$$$  |      
\_______/  \_______| \____$$ |\__|       \______/  \_______|      \_______/  \______/   \____/       
                    $$\   $$ |                                                                       
                    \$$$$$$  |                                                                       
                     \______/                                                        """

debug_ascii = """ /$$$$$$$            /$$                                 /$$      /$$                 /$$          
| $$__  $$          | $$                                | $$$    /$$$                | $$          
| $$  \ $$  /$$$$$$ | $$$$$$$  /$$   /$$  /$$$$$$       | $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$ 
| $$  | $$ /$$__  $$| $$__  $$| $$  | $$ /$$__  $$      | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$      | $$  $$$| $$| $$  \ $$| $$  | $$| $$$$$$$$
| $$  | $$| $$_____/| $$  | $$| $$  | $$| $$  | $$      | $$\  $ | $$| $$  | $$| $$  | $$| $$_____/
| $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/|  $$$$$$$      | $$ \/  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$
|_______/  \_______/|_______/  \______/  \____  $$      |__/     |__/ \______/  \_______/ \_______/
                                         /$$  \ $$                                                 
                                        |  $$$$$$/                                                 
                                         \______/                                                  """
                                         

MESSAGE_ASSETTO = """# Comment Installer Des Mods Sur Assetto Corsa

## Installer Content Manager

Rendez vous sur le [Drive](https://drive.google.com/drive/folders/11kvgbI9qiIeyqIjophSnKUyVubxRhJMN?usp=sharing) et télécharger** Content Manager** ainsi que le **VPN**. C'est **Radmin VPN** et celui ci nous sera utile pour la suite.
Téléchargez donc le Fichier *Content Manager.zip* puis décompressez le. Et executer le .exe et suivez les instructions.
Téléchargez le fichier **VPN.exe** (qui correspond à Radmin VPN.exe) puis executez le programme. Suivez les instructions encore une fois. 

## Installez les mods 

Une fois une **clé de licence obtenue et rentré dans CM**, vous n'avez cas **glisser déposer** les mods sous le format ZIP **dans la fenêtre de Content Manager**. 
Une petite** icône verte apparaîtra en haut à droite**, **cliquez** dessus et cliquez sur **installer les mods**. Si il n'y a pas d'erreur de décrite les mods fonctionneront nickel !

## Rejoindre Un Serveur

Pour rejoindre un serveur cela se fait en deux étapes:

- Ouvrez **Radmin VPN** et cliquez sur rejoindre un réseau et **renseigner l'ID ainsi que le mot de passe** de la session. Cela vous connaitre a une sorte de réseau LAN permettant ensuite de rejoindre le serveur Assetto Corsa 
- Dans Assetto Corsa. Allez dans **En Ligne** >> ** Favourites ** >> Chercher en bas à gauche l'icône **+** >>  et renseignez l'IP que l'Hôte vous donnera.


# Liens Ressources:

## [Drive](https://drive.google.com/drive/folders/11kvgbI9qiIeyqIjophSnKUyVubxRhJMN?usp=sharing)"""