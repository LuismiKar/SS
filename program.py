import csv

datos = ''
diccionario = {}

with open('Mental disorder symptoms 2.csv', newline='') as f:
    data = csv.reader(f, delimiter=',')
    datos = list(data)

def getData(datos):
    for i in range(1, len(datos)):
        diccionario[i] = list(zip((datos[0]),datos[i]))

getData(datos)

for x, y in diccionario.items():
    print(str(x) + ': ' + str(y))
    print('')