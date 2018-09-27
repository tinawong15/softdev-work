# Tina Wong
# SoftDev1 pd7
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    # print(app)
    return "Hello! Navigate to <a href=/form>this form</a>!"

@app.route("/form")
def forms():
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return render_template("authenticate.html",
                               user=request.args['username'],
                               method=request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
