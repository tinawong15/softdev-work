from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return "Hello!"

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
