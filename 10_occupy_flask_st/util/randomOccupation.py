import csv
import random

occDict = {}

# takes in a csv file and adds each row into the dictionary,
# with its "Job Class" as the key and the "Percentage" as the value
def handle_csv():
    data = open("data/occupations.csv", 'rt')
    occCsvReader = csv.reader( data)
    next(occCsvReader)
    for row in occCsvReader:
        if row[0] != "Total":
            occDict[row[0]] = float(row[1])
handle_csv()

# maintains the proportion between the occupation percentages by adding them to a list of size 998
# selects and returns a random occupation
def random_occupation():
    occupation = []
    for key in occDict:
        occupation = occupation + [key] * int(occDict[key] * 10)
    return random.choice(occupation)

def dict_keys():
    return occDict.keys()

def dict():
    return occDict
