from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.sqlite3"
db = SQLAlchemy()
db.init_app(app)

from project import routes
