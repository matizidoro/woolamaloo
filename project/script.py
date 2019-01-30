import numpy as np
import pandas as pd

# /home/izidoro/Área de Trabalho/marotage.txt

while True:
    try:
        directory = input('Insert the directory of the simplified file:')
        simplified_file = pd.read_csv(directory, delimiter=',')
        break
    except IOError as e:
        # 'No such file or directory'
        if e.errno == 2:
            print("Arquivo ou diretório não encontrado")
            # handle one way

while True:
    try:
        directory = input('Insert the directory of the csv file:')
        csv_file = pd.read_csv(directory, delimiter=',')
        break
    except IOError as e:
        # 'No such file or directory'
        if e.errno == 2:
            print("Arquivo ou diretório não encontrado")
            # handle one way

print(simplified_file.sort_values(by=['id']))
print(csv_file.sort_values(by=['employeeNumber']))
