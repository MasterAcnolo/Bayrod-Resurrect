# Bayrod Resurrect

Ce projet est une conversion d'un bot discord à l'origine en JS et aujourd'hui traduit et réalisé entièrement en Python. En utilisant la lib discord.py. 

1. Installation
```
git clone https://github.com/MasterAcnolo/Bayrod-Resurrect
```

Ensuite une fois que vous avez cloner le dépot. Vous pouvez ensuite installer les dépendances nécessaires. A savoir: 

- `pip install python-dotenv`

Après avoir installer les dépendances, créer un fichier `.env` dans le **dossier racine du projet**. Dans ce fichiers créez une variable TOKEN et donner lui comme valeur votre token de bot. Pour récuperer votre token rendez vous sur le site **Discord Developper Portal** > applications > et récupérer le token associé a votre bot. Attention ! Ne partagez surtout pas le token de votre bot ! 

2. Explication du fonctionnement

Ce bot fonctionne non pas avec un index mais avec un handler. C'est à dire que chaque fonction est appeler d'un fichier externe par le fichier principal : **bot.py**. Regardez et essayez de comprendre comment le code est constitué et vous comprendez vite comment tout fonctionne. Le code est assez bien divisé en dossiers et fichiers nommés de façon explicite. 
Vous retrouverez dans le fichier `variables.py` différentes variables que vous pourrez personnaliser. Toute façon si vous lisez ceci, c'est que vous savez ce que vous voulez ou ce que vous chercher. Donc vous aurez assez de jugeote pour pouvoir modifier le code selon vos besoins.