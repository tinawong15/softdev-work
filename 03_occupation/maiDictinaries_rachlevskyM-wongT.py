# Team MaiDictinaries - Mai Rachlevsky, Tina Wong
# SoftDev1 pd7
# K06 -- StI/O: Divine your Destiny!
# 2018-09-14

import csv
import random
occDict = {}


# reads the csv and each row is added into the dictionary,
# with its "Job Class" as the key and the "Percentage" as the value
def handle_csv():
    data = open("occupations.csv", 'rt')
    occCsvReader = csv.reader( data)
    next(occCsvReader)
    for row in occCsvReader:
        if row[0] != "Total":
            occDict[row[0]] = float(row[1])
    #print (occDict)

handle_csv()


# maintains the proportion between the occupation percentages by adding them to a list of size 998
# returns a random occupation
def random_occupation():
    occupation = []
    for key in occDict:
        occupation = occupation + [key] * int(occDict[key] * 10)
    # print (occupation)
    # print (len(occupation))
    return random.choice(occupation)


print ("The random occupation you selected was: " + random_occupation())
