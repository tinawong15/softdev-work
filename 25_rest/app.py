# Tina Wong
# SoftDev1 pd7
# K25 -- Getting More REST
# 2018-11-14

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def index():
    API_KEY = "fdee2887-3859-483e-ac98-a54c35ea2016"
    URL_STUB = "https://api.thecatapi.com/v1/images/search?size=full&mime_types=jpg&format=json&order=RANDOM&page=0&limit=10&category_ids&x-api-key="
    URL = URL_STUB + API_KEY
    u = urllib.request.urlopen(URL)
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)
    return render_template("index.html", pic=data[0]['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
