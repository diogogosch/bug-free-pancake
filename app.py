from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
engine = create_engine('mysql://root:password@bug-free-pancake_serasa-db_1/my-db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def load_key():
    # Loads the secret key
    return open("secret.key", "rb").read()


from controller.route_controller import *

if __name__ == '__main__':
    if not os.path.isfile('secret.key'):  # all code below runs if key is not yet created, so on the first run
        engine.execute("CREATE SCHEMA IF NOT EXISTS `my-db`;")  # create db
        engine.execute("USE `my-db`;")  # SET my-db as current schema

        def generate_key():
            # Generates key and saves to file
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
        generate_key()
    app.run(host="0.0.0.0", debug=True)
