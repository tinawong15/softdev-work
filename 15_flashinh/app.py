# Ryan Aday, Tina Wong - team TL;DR
# SoftDev1 pd7
# K15 -- Oh yes, perhaps I do...
# 2018-10-02

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__) #create instance of class Flask
app.secret_key = os.urandom(32) #creates random key of 32 bytes

users = {'test' : '123'} # key and value in dict

# home page that either renders the welcome page or the login page
@app.route("/") #assign fxn to route
def home():
    # print("testing")
    if 'test' not in session:
        return render_template('login.html')
    else:
        user = 'test'
        return render_template("welcome.html",user=user)

# a route that receives the login form and checks if the login information is correct
@app.route("/auth", methods=["POST"]) #assign fxn to route
def authenticate():
    if request.form['username'] not in users.keys():
        flash("Username invalid, is not "+request.form['username'])
        return render_template("login.html")
    elif users[request.form['username']] != request.form['password']:
        flash("Password invalid, is not "+request.form['password'])
        return render_template('login.html')
    else:
        session['test'] = '123'
        return redirect(url_for('home'))

# a route that removes the current user from the session and redirects the user back to the login page from home
@app.route('/logout')
def logout():
    session.pop('test') # ends session
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
