from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_friend'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///inventory.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()

from Prasanna_Project.project import app