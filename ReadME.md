# Bayrod Resurrect

Ce projet est une conversion d'un bot Discord à l'origine en JS et aujourd'hui traduit et réalisé entièrement en Python. En utilisant la bibliothèque **discord.py**. 

## Installation
```
git clone https://github.com/MasterAcnolo/Bayrod-Resurrect
```

Ensuite une fois que vous avez cloné le dépôt, vous pouvez installer les dépendances nécessaires. À savoir: 

- `pip install python-dotenv`


Après avoir installé les dépendances, créez un fichier `.env` dans le **dossier racine du projet**. Dans ce fichier créez une variable TOKEN et donnez-lui comme valeur votre token de bot. Pour récupérer votre token rendez-vous sur le site **Discord Developper Portal** > applications > et récupérer le token associé à votre bot. Attention ! Ne partagez surtout pas le token de votre bot ! 

## Explication du fonctionnement

Ce bot fonctionne non pas avec un index mais avec un handler. C'est à dire que chaque fonction est appelée par un fichier externe depuis le fichier principal : **bot.py**. Regardez et essayez de comprendre comment le code est constitué et vous comprendrez vite comment tout fonctionne. Le code est assez bien divisé en dossiers et fichiers nommés de façon explicite. 
Vous retrouverez dans le fichier `variables.py` différentes variables que vous pourrez personnaliser. Toute façon,si vous lisez ceci, c'est que vous savez ce que vous voulez ou ce que vous cherchez. Vous aurez par conséquzent assez de jugeote pour pouvoir modifier le code selon vos besoins.

## Licences

**Copyright 2025 MasterAcnolo**

Globalement, faites ce que vous voulez avec le code. Créditez-moi si vous êtes bons. J'espère surtout qu'il vous servira pour vos propres projets ! :)
