from flask import Flask, jsonify

import numpy as np
import datetime as dt

import sqlalchemy as sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

app = Flask(__name__)

engine = create_engine('sqlite:///Resources/hawaii.sqlite')
session = Session(bind = engine)
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# latest_date_str = session.query(Measurement).order_by(Measurement.date.desc())#.date
# latest_date = dt.datetime.strptime(latest_date_str, '%Y-%m-%d')
# one_year_ago_date = latest_date - dt.timedelta(days = 365)

@app.route('/')
def index():
    return ('Usage of this website:<br/>'
    '/api/v1.0/precipitation<br/>'
    '/api/v1.0/stations<br/>'
    '/api/v1.0/tobs<br/>'
    '/api/v1.0/<start><br/>'
    '/api/v1.0/<start>/<end>'
    )
    
@app.route('/api/v1.0/precipitation')
def precipitation():
    # latest_date_str = session.query(Measurement).order_by(Measurement.date.desc())#.date
    # latest_date = dt.datetime.strptime(latest_date_str, '%Y-%m-%d')
    one_year_ago_date = dt.date(2017,8,23) - dt.timedelta(days = 365)    
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago_date).all()
    prec = {result[0]:result[1] for result in results}
    return jsonify(prec)

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations_results = list(np.ravel(results))
    return jsonify(stations_results)

@app.route('/api/v1.0/tobs')
def tobs():
    one_year_ago_date = dt.date(2017,8,23) - dt.timedelta(days = 365)    
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= one_year_ago_date).all()
    tobs_results = list(np.ravel(results))
    return jsonify(tobs_results)

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def stats(start = None, end = None):
    stat = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*stat).filter(Measurement.date >= start).all()
        stat_results = list(np.ravel(results))
        return jsonify(stat_results)
    results = session.query(*stat).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    stat_results = list(np.ravel(results))
    return jsonify(stat_results)


if __name__ == "__main__":
    app.run(debug=True)