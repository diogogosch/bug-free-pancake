from flask import Flask, request

import user_model

user_00 = user_model.User('Diogo', '04188442913', 'diogogosch@gmail.com', '41988880087')
user_01 = user_model.User('Ruy', '51459418972', 'rvieirag@gmail.com', '47984349315')
print(user_01.name)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
