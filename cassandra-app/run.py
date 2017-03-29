from flask import Flask
from os import environ

from database import cdb
from models.ExampleModel import ExampleModel

# Allows the python driver to perform CQL management tasks
environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = 'True'

# Initialise the app
app = Flask(__name__)
app.config.from_object('config')

# Use the app details to connect to a cassandra database,
# set up a table using a model defined in python and
# push some example data
cdb.init_app(app)
cdb.connect()
cdb.sync_table(ExampleModel)
cdb.add(ExampleModel)
