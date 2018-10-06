# Team Cyber - Amit Narang & Tina Wong
# SoftDev1 pd7
# K #17: Average
# 2018-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

# Creates a cursor and the database
db = sqlite3.connect("discobandit.db") #open if file exists, otherwise create
c = db.cursor() #facilitate db ops

def lookup_grades(name):
    c.execute("SELECT code, mark FROM courses, peeps WHERE peeps.id=courses.id AND name = \"{}\"".format(name))
    string = '';
    # fetchall() fetches data from the result set
    for data in c.fetchall():
        string += 'Course: {} Grade: {}\n'.format(data[0], data[1])
    string = string.rstrip() # removes last \n
    return string

# adds average as a column of peeps
def get_avg():
    c.execute("ALTER TABLE peeps ADD average FLOAT")
    for i in (range(10)):
        d = i + 1
        temp = 0
        cnt = 0
        for j in c.execute("SELECT mark FROM courses WHERE id = {}".format(str(d))):
            # print(j)
            temp += j[0]
            cnt +=1
        temp = float(temp)/cnt
        # temp  == Average
        c.execute("UPDATE peeps SET average = {} WHERE id = {}".format(str(temp), str(d)))
        # print(temp)

def compute_avg(name):
    c.execute("SELECT average FROM peeps WHERE name = \"{}\"".format(name))
    string = '';
    for data in c.fetchall():
        string += name+"'s Average: {}".format(data[0])
    return string

def display_info():
    string = ''
    c.execute("SELECT name, id, average FROM peeps")
    for data in c.fetchall():
        string += 'Student: {} ID: {} GPA: {}\n'.format(data[0], data[1], data[2])
    string = string.rstrip()
    return string

# adds peeps_avg table
def table():
    c.execute("CREATE TABLE peeps_avg (id INTEGER, average FLOAT)")
    c.execute("SELECT id, average FROM peeps")
    for data in c.fetchall():
        c.execute("INSERT INTO peeps_avg VALUES ( \"{}\" , \"{}\" )".format(data[0] , data[1]) ) #run SQL statement

def addInfo(name1,age1,id1,average1):
    #  THE SQLITE3 WAY OF STRING FORMATTING
    params =(name1,age1,id1,average1)
    c.execute("INSERT INTO peeps VALUES (?, ?, ?, ?)",params)

get_avg()
print (compute_avg("kruder"))
print "======================"
print (lookup_grades("kruder"))
print "======================"
print (display_info())
print "======================"
addInfo('ally',16,11,39.1)
print (display_info())
print "======================"
table()

db.commit() #save changes
db.close()  #close database
