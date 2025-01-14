import json
import random
import datetime
import os

first_names = ["Guillaume", "Peter", "Sheila", "Josephine", "Michael", "Roisin", "David","Loic", "Remy", "Angus",
                "Nicholas", "Hortense", "Betty", "William"]

last_names = ["Baker", "Smith", "Hodgson", "Saunders", "Peterson", "Johanson", "Mingus", "Collins", "Rowntree",
              "Turner", "Constable", "Bacon", "Picasso"]

def create_person():
    person = [random.choice(first_names), random.choice(last_names)]
    return person

def generate_random_date():
    year = random.randint(1930, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.datetime(year, month, day)

def create_list_of_people(n):
    prelim_list = []
    i = 0
    while i < n:
        person = create_person()
        if not person in prelim_list:
            person.append(generate_random_date().date().strftime("%d/%m/%Y"))
            prelim_list.append(person)
            i += 1
    return prelim_list

def create_dir(name):
    current_folder = os.getcwd()
    new_folder = name
    new_path = os.path.join(current_folder, new_folder)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    return new_path

if __name__ == '__main__':

    list_of_people = create_list_of_people(32)

    json_save_folder = create_dir('data/players')

    json_file_path = os.path.join(json_save_folder, 'players.json')
    with open(json_file_path, 'w') as f:
        json.dump(list_of_people, f, indent = 4)
    

