import json
import pprint

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        json_file = open("data.json", "r")
        cont = json_file.read()
        data = json.loads(cont)

except FileExistsError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    status = 'Файл не найден'


#pprint.pprint(data)

print('\n' + '<-'*13 + ' ¯\_(ツ)_/¯ ' + '->'*13 + '\n\n')
for item in data:
    print(" Company: " + str(item['company']))
    print(" Email: " + str(item['email']))
    print(" Phone: " + str(item['phone']))
    print(" Address: " + str(item['address']) + '\n')
    print(' ' + '-*-*'*16 + '\n')
