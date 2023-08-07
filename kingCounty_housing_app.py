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

kc = Base.classes.king_county_sales

session = Session(engine)


# flask setup

kingCounty_housing_app = Flask(__name__)


@kingCounty_housing_app.route("/")
def welcome():
    # List all available api routes.

    return render_template("index.html")
  
@kingCounty_housing_app.route("/api/v1.0/king_county_realestate")
def king_county_data():
    session = Session(engine)
    
    results = session.query(kc.id, kc.sale_id, kc.sale_date, kc.sale_price, kc.sale_nbr, kc.join_status, kc.latitude, kc.longitude, kc.city, kc.zoning, kc.subdivision, kc.present_use,
                            kc.land_val, kc.imp_val, kc.year_built, kc.year_reno, kc.sqft_lot, kc.sqft)
        
                      
    session.close()
    
    king_county_data = []
    for id, sale_id, sale_date, sale_price, sale_nbr, join_status, latitude, longitude, city, zoning, subdivision, present_use, land_val, imp_val, year_built, year_reno, sqft_lot, sqft in results:
        kc_dict = {}
        kc_dict["id"] = id
        kc_dict["sale_id"] = sale_id
        kc_dict["sale_date"] = sale_date
        kc_dict["sale_price"] = sale_price
        kc_dict["sale_nbr"] = sale_nbr
        kc_dict["join_status"] = join_status
        kc_dict["latitude"] = latitude
        kc_dict["longitude"] = longitude
        kc_dict["city"] = city
        kc_dict["zoning"] = zoning
        kc_dict["subdivision"] = subdivision
        kc_dict["present_use"] = present_use
        kc_dict["land_val"] = land_val
        kc_dict["imp_val"] = imp_val
        kc_dict["year_built"] = year_built
        kc_dict["year_reno"] = year_reno
        kc_dict["sqft_lot"] = sqft_lot
        kc_dict["sqft"] = sqft
        king_county_data.append(kc_dict)
    return jsonify(king_county_data)
     
if __name__ == '__main__':
    kingCounty_housing_app.run(debug=True)

