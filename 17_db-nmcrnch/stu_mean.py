# Team Cyber - Amit N & Tina W
# SoftDev1 pd7
# K #17: Average
# 10-5-18


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

# Creates a cursor and the database
db = sqlite3.connect("discobandit.db")
c = db.cursor()

def lookup_grades(name):
    c.execute("SELECT code, mark FROM courses, peeps WHERE peeps.id=courses.id AND name = \"{}\"".format(name))
    string = '';
    for data in c.fetchall():
        string += 'Course: {} Grade: {}\n'.format(data[0], data[1])
    string = string.rstrip()
    return string

def get_avg():
    # c.execute("ALTER TABLE peeps ADD average INTEGER")
    for i in (range(10)):
        d = i + 1
        temp = 0
        #val = c.execute("SELECT mark FROM courses WHERE id = {}".format(str(d)))
        cnt = 0
        for j in c.execute("SELECT mark FROM courses WHERE id = {}".format(str(d))):
            # print(j)
            temp += j[0]
            cnt +=1
        temp = temp/cnt
        # temp  == Average
        c.execute("UPDATE peeps SET average = {} WHERE id = {}".format(str(temp), str(d)))
        # print(temp)

def display_info():
    string = ''
    c.execute("SELECT name, id, average FROM peeps")
    for data in c.fetchall():
        string += 'Student: {} ID: {} GPA: {}\n'.format(data[0], data[1], data[2])
    string = string.rstrip()
    return string

get_avg()
print (lookup_grades("kruder"))
print (display_info())

db.commit() #save changes
db.close()  #close database