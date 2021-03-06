# Tina Wong
# SoftDev1 pd7
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

# home page that links to the form
@app.route("/") #assign fxn to route
def home():
    # print(app)
    return "Hello! Navigate to <a href=/form>this form</a>!"

# a route to the form
@app.route("/form") #assign fxn to route
def forms():
    return render_template("form.html")

# a route that receives the form and returns a template with user's information
@app.route("/auth", methods=["GET", "POST"]) #assign fxn to route
def authenticate():
    if request.method == "GET":
        user = request.args['usernameViaGet']
        print(app)
        print(request)
        print(request.args)
        print(request.args['usernameViaGet'])
        print(request.headers)
    else:
        user = request.form['usernameViaPost']
    return render_template("authenticate.html",
                                   user=user,
                                   method=request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
