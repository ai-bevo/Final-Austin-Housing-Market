# final project  
# install for connecting with postgresql
#pip install psycopg2-binary
import pandas as pd
import psycopg2 as pg
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, render_template
from config import pw

connection_string = f"postgres:{pw}@localhost:5432/Seattle_Housing_Market"
engine = create_engine(f'postgresql://{connection_string}')

Base = automap_base()

Base.prepare(engine, reflect=True)

shm = Base.classes.seattle_sales

session = Session(engine)


# flask setup

seattle_housing_app = Flask(__name__)


@seattle_housing_app.route("/")
def welcome():
    # List all available api routes.

    return render_template("index.html")
  
@seattle_housing_app.route("/api/v1.0/seattle_real_estate")
def seattle_data():
    session = Session(engine)
    
    results = session.query(shm.id, shm.sale_id, shm.sale_date, shm.sale_price, shm.sale_nbr, shm.join_status, shm.latitude, shm.longitude, shm.city, shm.zoning, shm.subdivision, shm.present_use,
                            shm.land_val, shm.imp_val, shm.year_built, shm.year_reno, shm.sqft_lot, shm.sqft)
        
                      
    session.close()
    
    seattle_data = []
    for id, sale_id, sale_date, sale_price, sale_nbr, join_status, latitude, longitude, city, zoning, subdivision, present_use, land_val, imp_val, year_built, year_reno, sqft_lot, sqft in results:
        shm_dict = {}
        shm_dict["id"] = id
        shm_dict["sale_id"] = sale_id
        shm_dict["sale_date"] = sale_date
        shm_dict["sale_price"] = sale_price
        shm_dict["sale_nbr"] = sale_nbr
        shm_dict["join_status"] = join_status
        shm_dict["latitude"] = latitude
        shm_dict["longitude"] = longitude
        shm_dict["city"] = city
        shm_dict["zoning"] = zoning
        shm_dict["subdivision"] = subdivision
        shm_dict["present_use"] = present_use
        shm_dict["land_val"] = land_val
        shm_dict["imp_val"] = imp_val
        shm_dict["year_built"] = year_built
        shm_dict["year_reno"] = year_reno
        shm_dict["sqft_lot"] = sqft_lot
        shm_dict["sqft"] = sqft
        seattle_data.append(shm_dict)
    return jsonify(seattle_data)
     
if __name__ == '__main__':
    seattle_housing_app.run(debug=True)

