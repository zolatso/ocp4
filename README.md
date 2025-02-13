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