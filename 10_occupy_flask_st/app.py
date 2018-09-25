# Imad Belkebir, Tina Wong - Team random
# SoftDev1 pd7
# K10 -- Jinja Turning
# 2018-09-24

from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask


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

@app.route("/") #assign fxn to route
def home():
    return "<a href=/occupations>Occupation Table</a>" # provides a link to the occupations route

# returns the template and values that will replace the Jinja2 in the template
@app.route("/occupations") #assign fxn to route
def table():
    return render_template("occupations.html",
                            title = "Occupations Table",
                            heading = "Table-ified Data",
                            var1 = random_occupation(),
                            items = occDict.keys(),
                            dict = occDict)

if __name__ == "__main__":
    app.debug = True
    app.run()
