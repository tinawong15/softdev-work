# Tina Wong
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def index():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic=data['url'])
    
if __name__ == "__main__":
    app.debug = True
    app.run()
