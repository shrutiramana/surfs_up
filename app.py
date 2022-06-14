import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

#Reflect the table
Base.prepare(engine, reflect=True)

# Save references to each of the tabls.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link.
session = Session(engine)

# Defien flask app.
app = Flask(__name__)
# define welcome route.

@app.route("/")
# Adding the routing information.

def welcome():
    return(
    '''
        Welcome to the Climate Analysis API!
        Available Routes: 
        /api/v1.0/precipitation \n
        /api/v1.0/stations \n
        /api/v1.0/tobs \n
        /api/v1.0/temp/start/end \n
    ''')

# definfing Precipitaion Route
@app.route("/api/v1.0/precipitation")

#create precipitation function.
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# defining Station Route
@app.route("/api/v1.0/stations")

# create the stations function.
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# defining Monthly Temperature Route
@app.route("/api/v1.0/tobs")

# create the monthly temperature function.

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)



@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)