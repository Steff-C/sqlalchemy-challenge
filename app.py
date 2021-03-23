import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# # Database Setup
# engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# Base = automap_base()

# Base.prepare(engine, reflect=True)


# Measurement = Base.classes.measurement
# Station = Base.classes.station



# Set up Flask in app
app = Flask(__name__)


# Routes

@app.route("/")
def welcome():
    return (
        f"Welcome to the SQL-Alchemy APP API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )



if __name__ == "__main__":
    app.run(debug=True)