import pandas as pd

# /home/izidoro/Área de Trabalho/marotage.txt

# find the path to the simplified file
while True:
    try:
        directory = '/home/izidoro/Área de Trabalho/marotage.txt'
        # input('Insert the directory of the simplified file:')
        simplified_file = pd.read_csv(directory, delimiter=',') # convert the file into a DataFrame
        break
    except IOError as e:
        # 'No such file or directory'
        if e.errno == 2:
            print("Arquivo ou diretório não encontrado")
            # handle one way

# find the path to the csv file
while True:
    try:
        directory = '/home/izidoro/Área de Trabalho/marotagb.csv'
        # input('Insert the directory of the csv file:')
        csv_file = pd.read_csv(directory, delimiter=',')        # convert the file into a DataFrame
        break
    except IOError as e:
        # 'No such file or directory'
        if e.errno == 2:
            print("Arquivo ou diretório não encontrado")
            # handle one way

# sort both dataframes by id
simplified_file = simplified_file.sort_values(by=['id'])
csv_file = csv_file.sort_values(by=['employeeNumber'])

# reindex dataframes's rows
simplified_file = simplified_file.reset_index(drop=True)
csv_file = csv_file.reset_index(drop=True)

print(simplified_file)
print(csv_file)

print(' Woolamaloo Synchronization Report  ')
print('------------------------------------')
print("\nID     Name              Status  ")
print('----- ------------------ --------')

# compares data 'till the end of the dataframes
i = j = 0
while (i < len(simplified_file.index) or j < len(csv_file.index)):
    if i >= len(simplified_file.index) or simplified_file.loc[i].at['id'] > csv_file.loc[j].at['employeeNumber']:
        # new employees
        _id = csv_file.loc[j].at['employeeNumber']
        _name = csv_file.loc[j].at['cn']
        _status = "New Employee on Web Auth"
        j += 1
    elif j >= len(csv_file.index) or simplified_file.loc[i].at['id'] < csv_file.loc[j].at['employeeNumber']:
        # missing employees
        _id = simplified_file.loc[i].at['id']
        _name = simplified_file.loc[i].at['name']
        _status = "Missed Employee on Web Auth"
        if str(simplified_file.loc[i].at['demission_date']) != 'nan':
            _status += "; Worked with the Woolamaloo from " + str(simplified_file.loc[i].at['admission_date']) + " until " + str(simplified_file.loc[i].at['demission_date'])
        i += 1
    else:
        # both rows match
        # old employees
        _id = simplified_file.loc[i].at['id']
        _name = simplified_file.loc[i].at['name']

        if str(simplified_file.loc[i].at['demission_date']) != 'nan':
            _status = "Worked with the Woolamaloo from " + str(simplified_file.loc[i].at['admission_date']) + " until " + str(simplified_file.loc[i].at['demission_date'])
        else:
            _status = "Regularized Employee"

        if simplified_file.loc[i].at['department'] != csv_file.loc[j].at['department']:
            _status += "; Changed department from " + simplified_file.loc[i].at['department'] + " to " + csv_file.loc[j].at['department']
        if simplified_file.loc[i].at['position'] != csv_file.loc[j].at['position']:
            _status += "; Changed position from " + simplified_file.loc[i].at['position'] + " to " + csv_file.loc[j].at['position']


        i += 1
        j += 1

    print('%d   %-18s %s' % (_id, _name, _status))

