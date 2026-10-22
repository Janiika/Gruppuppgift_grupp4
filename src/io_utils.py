    ### Läser data från CSV filen mha DictReader

import csv

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data