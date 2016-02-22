import sys

import csv

class Csv():
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, newline='') as csvfile:    #csv File oeffnen
            txt = ""
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')  #csv-File einlesen
            for row in spamreader: #jede reihe durchgehen
                txt += str(', '.join(row)) + "\n"   #jede spalte der reihe auslesen
        return txt

if __name__ == "__main__":
    test = Csv('tc.csv')
    print(test.read())