import csv
from helper import *
from presenteer import *
inkomsten = {
    "Aardbeien-ijs-totaal" : int(1000),
    "Vanilla-ijs-totaal" : int(2000),
    "Chocolade-ijs-totaal" : int(1500),
    "Water-ijs-totaal" : int(750)
}

totaal_inkomsten = som(inkomsten)

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])
    