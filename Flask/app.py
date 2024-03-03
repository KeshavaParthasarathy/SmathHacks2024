from flask import* 


app = Flask(__name__)

@app.route("/123")
def index123():
    s = """
<form method=post action="/suggestedRecipe"> 
<input type=text name=ingredient value="tomato">
<input type=submit>
</form>
"""
    return s

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/menu.html")    
def menu():
    return render_template("menu.html")

@app.route("/suggestedRecipe", methods=['GET', 'POST'])
def recipe():
    ingredient = request.form['ingredient']

    s = ingredient.upper()
    return s