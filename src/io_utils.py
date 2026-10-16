    ### Läser data från CSV filen. Hämtar både kolumnnamn och data. Returnerar en tuple med kolumnnamn och data.

import csv

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    return header, data