from flask import* 
import numpy as np 
import pandas as pd 
import functions


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/menu.html")    
def menu():
    return render_template("menu.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/menu.html", methods=['GET', 'POST'])
def recipe():

    if request.method == "POST":

        ingredient = request.form['ingredient']

        s = ingredient.upper()

        result = functions.search_recipes_by_ingredients(s)

        return render_template("menu.html", result = result)
    