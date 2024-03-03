from flask import Flask 

app = Flask(__name__)


# Just an empty format for how our code should be input
@app.route('/api/route')
def predict():
    return 'hello'

