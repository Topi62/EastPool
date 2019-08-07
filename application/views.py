from flask import render_template, request, redirect, url_for
from application import app

@app.route("/", methods = ["GET", "POST"])
def index():
   return render_template("index.html")



