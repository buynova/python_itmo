from flask import Flask
from flask_pony import Pony

app = Flask(__name__)
app.config.from_json("../config.json")

pony = Pony(app)

db = pony.get_db()

from . import views, models

db.generate_mapping(create_tables=True)
