# ocp4
Projet 4 du programme de formation Développeur Python d’OpenClassrooms  

## Installation  
1. Clonez le dépôt : 
```bash
 git clone https://github.com/yourusername/yourproject.git
``` 

2. Créez et activez l’environnement virtuel (depuis le dossier racine du projet) :  
```bash
python -m venv env
```
```bash
source env/bin/activate
```
3. Installez les dépendances :  
```bash
pip install -r requirements.txt
 ```

## Exécuter le script  
4. Exécutez le script :  
```bash
python main.py
 ```

Une fois en cours d’exécution, l’application propose 4 options principales.  
Vous pouvez créer un tournoi, générer des paires/saisir les scores d’un tournoi existant, créer un nouveau joueur et consulter les rapports (des joueurs et des tournois).  

Le script vérifie que les entrées sont au bon format.  
À chaque création d’un nouveau joueur ou tournoi, les données sont enregistrées dans un fichier JSON.  
Tous les joueurs sont sauvegardés dans un seul fichier JSON, tandis que chaque tournoi possède son propre fichier JSON.  

5. Pour générer un rapport Flake8 (les dépendances sont déjà installées) :  
```bash
flake8 --format=html --htmldir=flake8_rapport
```
Le rapport Flake8 sera disponible sous forme de plusieurs fichiers HTML dans le dossier que nous avons spécifié (flake8_rapport). Il suffit d'ouvrir index.html dans un navigateur pour le consulter.

---
# ocp4
Project 4 for the OpenClassrooms Python Developer Training Program

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/yourusername/yourproject.git
```

2. Create and activate virtual environment (from root folder of project):
```bash
python -m venv env
```
```bash
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
 ```

## Run script
4. Run script:
```bash
python main.py
 ```

Once running, the application has 4 primary options.
You can create a tournament, create pairs/input scores for an existing tournament,
create a new player, and look at reports (of both players and tournaments).
The script will check that inputs are in the correct format.
Any time a new player or tournament is created, it is saved as a json file.
All players are saved in one json file, while each tournament has its own json file.

5. To generate a flake 8 report (the dependecies have already been installed):
```bash
flake8 --format=html --htmldir=flake8_rapport
```
The flake8 report will be available as various html file inside the folder we specified (flake8_report). Simply open index.html in a browser to consult it.