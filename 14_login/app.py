# Tina Wong
# SoftDev1 pd7
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__) #create instance of class Flask
app.secret_key = os.urandom(32)

users = {'test' : '123'}

# home page that links to the form
@app.route("/") #assign fxn to route
def home():
    # print("testing")
    if 'test' not in session:
        return render_template('login.html')
    else:
        user = 'test'
        return render_template("welcome.html",user=user)

# a route that receives the form and returns a template with user's information
@app.route("/auth", methods=["POST"]) #assign fxn to route
def authenticate():
    if request.form['username'] not in users.keys():
        return render_template("login.html", error = "Username invalid")
    elif users[request.form['username']] != request.form['password']:
        return render_template('login.html', error = "Password invalid")
    else:
        session['test'] = '123'
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('test')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
