from flask import* 


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    s = """
<form method=post action="recipe.html"> 
<input type=text name=ingredient value="tomato">
<input type=submit>
</form>
"""
    return s

@app.route("/recipe.html", methods=['GET', 'POST'])
def recipe():
    ingredient = request.form['ingredient']

    s = ingredient.upper()
    return s