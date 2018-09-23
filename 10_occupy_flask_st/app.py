# Imad Belkebir, Tina Wong - Team random
# SoftDev1 pd7
# K10 -- Jinja Turning
# 2018-09-24

from flask import Flask, render_template
app = Flask(__name__)

import csv
import random
occDict = {}

def handle_csv():
    data = open("data/occupations.csv", 'rt')
    occCsvReader = csv.reader( data)
    next(occCsvReader)
    for row in occCsvReader:
        if row[0] != "Total":
            occDict[row[0]] = float(row[1])
handle_csv()

def random_occupation():
    occupation = []
    for key in occDict:
        occupation = occupation + [key] * int(occDict[key] * 10)
    return random.choice(occupation)

@app.route("/")
def home():
    return "<a href=/occupations>Occupation Table</a>"

@app.route("/occupations")
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
