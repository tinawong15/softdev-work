# Tina Wong
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2019-09-20

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__) #where will this go?
    return "hello world!"

@app.route("/dog") #assign fxn to route
def dog():
    return "this is a page for dogs but ducks are always welcome!"

@app.route("/cat") #assign fxn to route
def cat():
    return "this is a page for cats because my ducky's name is Cat"

@app.route("/dolphin") #assign fxn to route
def dolphin():
    return "because dolphins are cool"

if __name__ == "__main__":
    app.debug = True
    app.run()
