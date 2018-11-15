# Tina Wong
# SoftDev1 pd7
# K26 -- Getting More REST
# 2018-11-15

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def index():
    URL = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400"
    u = urllib.request.urlopen(URL)
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    API_KEY = "5bece9dce863c78720d230251f7f0b2b"
    latitude = "40.718"
    longitude = "-74.014"
    URL_STUB = "https://api.darksky.net/forecast/"
    URL = URL_STUB+API_KEY+"/"+latitude+","+longitude
    u = urllib.request.urlopen(URL)
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)
    timezone = data["timezone"]

    URL_STUB = "https://api.darksky.net/forecast/"
    URL = URL_STUB+API_KEY+"/"+latitude+","+longitude
    u = urllib.request.urlopen(URL)
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)

    URL = "https://restcountries.eu/rest/v2/name/united%20states%20of%20america"
    u = urllib.request.urlopen(URL)
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)
    name = data[0]["name"]
    translations = []
    for translation in data[0]["translations"]:
        translations.append(data[0]["translations"][translation])
    # print(translations)
    return render_template("index.html", sunrise=sunrise, sunset=sunset, timezone=timezone, name=name, translations=translations)

if __name__ == "__main__":
    app.debug = True
    app.run()
