# Tina Wong
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def index():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=M28pE64z543Z5HEA9ommZK9RxgQRXGEs5szzuyJv")
    response = u.read() # reads url
    # print(response)
    data = json.loads(response) # turns a JSON object string into a Python dictionary
    # print(data)
    return render_template("index.html", pic=data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
