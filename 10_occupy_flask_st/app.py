# Imad Belkebir, Tina Wong - Team random
# SoftDev1 pd7
# K10 -- Jinja Turning
# 2018-09-24

from flask import Flask, render_template
from util import randomOccupation

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def home():
    return "<a href=/occupations>Occupation Table</a>" # provides a link to the occupations route

# returns the template and values that will replace the Jinja2 in the template
@app.route("/occupations") #assign fxn to route
def table():
    return render_template("occupations.html",
                            title = "Occupations Table",
                            heading = "Table-ified Data",
                            var1 = randomOccupation.random_occupation(),
                            items = randomOccupation.dict_keys(),
                            dict = randomOccupation.dict())

if __name__ == "__main__":
    app.debug = True
    app.run()
