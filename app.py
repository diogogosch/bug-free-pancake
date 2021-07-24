import os

from flask import Flask

import user

user_00 = user.User('Diogo', '04188442913', 'diogogosch@gmail.com', '41988880087')
user_01 = user.User('Ruy', '51459418972', 'rvieirag@gmail.com', '47984349315')

app = Flask(__name__)

if __name__ == '__main__':
    print('app.py sendo executado')