import re
from flask import render_template, request, redirect, url_for
from application import app

def string_check(string, pnum):
    pattern = {
       1: '[ÅÄÖA-Z][åäöa-z]{0,13}$',
       2: '[ÅÄÖA-Z][ÅÄÖA-Z][1-9]',
       3: '[ÅÄÖA-Zåäöa-z0-9]{1,8}$',
       4: '[ÅÄÖA-Zåäöa-z0-9]{1,15}$'  
       }
    syntax =  re.compile(pattern.get(pnum), flags=0)
    return re.match(syntax, string)

@app.route("/", methods = ["GET", "POST"])
def index():
   return render_template("index.html")



