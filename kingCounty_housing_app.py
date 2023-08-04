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

# annual_sales = Base.classes.annual_sales
# monthly_sales = Base.classes.monthly_sales
# price_distribution = Base.classes.price_distribution
kc = Base.classes.king_county_sales

session = Session(engine)


# example query from annual sales table
# session.query(annual_sales.median_price).all()


# flask setup

austin_housing_app = Flask(__name__)
#cors = CORS(austin_housing_app)
#cors = CORS(austin_housing_app, origins=["http://127.0.0.1:5000"])
#Check port number 5000 or 5500
#pip install flask-cors

@austin_housing_app.route("/")
def welcome():
    # List all available api routes.

    return render_template("index.html")
  
# @austin_housing_app.route("/index2.html")
# def welcome_again():
#     # List all available api routes.
#     return render_template("index2.html")
  
  
# @austin_housing_app.route("/api/v1.0/annual_sales_table")
# def annual_sales_data():
#     # session link to annual sales table
#     session = Session(engine)
#     # query annual sales table
#     results = session.query(annual_sales.year, annual_sales.sales, annual_sales.dollar_volume, 
#                             annual_sales.average_price, annual_sales.median_price, 
#                             annual_sales.total_listings, annual_sales.months_inventory).all()
    
#     session.close()
#     # create a dictionary from the row data and append to a list of annual sales
#     annual_sales_data = []
#     for year, sales, dollar_volume, average_price, median_price, total_listings, months_inventory in results:
#         annual_sales_dict = {}
#         annual_sales_dict["year"] = year
#         annual_sales_dict["sales"] = sales
#         annual_sales_dict["dollar_volume"] = dollar_volume
#         annual_sales_dict["average_price"] = average_price
#         annual_sales_dict["median_price"] = median_price
#         annual_sales_dict["total_listings"] = total_listings
#         annual_sales_dict["months_inventory"] = months_inventory
#         annual_sales_data.append(annual_sales_dict)
        
#     #return render_template('index.html', json_data = sales_data)
#     return jsonify(annual_sales_data)

# @austin_housing_app.route("/api/v1.0/monthly_sales_table")
# def monthly_sales_data():
#     session = Session(engine)
    
#     results = session.query(monthly_sales.dates, monthly_sales.sales, monthly_sales.dollar_volume, monthly_sales.average_price, 
#                             monthly_sales.median_price, monthly_sales.total_listings, monthly_sales.months_inventory).all()
    
#     session.close()
    
#     monthly_sales_data = []
#     for dates, sales, dollar_volume, average_price, median_price, total_listings, months_inventory in results:
#         monthly_sales_dict = {}
#         monthly_sales_dict["dates"] = dates
#         monthly_sales_dict["sales"] = sales 
#         monthly_sales_dict["dollar_volume"] = dollar_volume
#         monthly_sales_dict["average_price"] = average_price
#         monthly_sales_dict["median_price"] = median_price
#         monthly_sales_dict["total_listings"] = total_listings
#         monthly_sales_dict["months_inventory"] = months_inventory
#         monthly_sales_data.append(monthly_sales_dict)
    
#     return jsonify(monthly_sales_data)


# @austin_housing_app.route("/api/v1.0/price_distribution_table")
# def price_distribution_data():
#     session = Session(engine)
    
#     results = session.query(price_distribution.price_distribution, price_distribution.year_2011, price_distribution.year_2012, price_distribution.year_2013,
#                             price_distribution.year_2014, price_distribution.year_2015, price_distribution.year_2016, price_distribution.year_2017,
#                             price_distribution.year_2018, price_distribution.year_2019, price_distribution.year_2020, price_distribution.year_2021,
#                             price_distribution.year_2022).all()

#     session.close()
    
#     price_distribution_data = []
#     for price_distribution_col, y2011, y2012, y2013, y2014, y2015, y2016, y2017, y2018, y2019, y2020, y2021, y2022 in results:
#         price_distribution_dict = {}
#         price_distribution_dict["price_distribution"] = price_distribution_col
#         price_distribution_dict["2011"] = y2011
#         price_distribution_dict["2012"] = y2012
#         price_distribution_dict["2013"] = y2013
#         price_distribution_dict["2014"] = y2014
#         price_distribution_dict["2015"] = y2015
#         price_distribution_dict["2016"] = y2016
#         price_distribution_dict["2017"] = y2017
#         price_distribution_dict["2018"] = y2018
#         price_distribution_dict["2019"] = y2019
#         price_distribution_dict["2020"] = y2020
#         price_distribution_dict["2021"] = y2021
#         price_distribution_dict["2022"] = y2022
#         price_distribution_data.append(price_distribution_dict)
        
#     return jsonify(price_distribution_data)
        

@austin_housing_app.route("/api/v1.0/king_county_realestate")
def king_county_data():
    session = Session(engine)
    
    results = session.query(kc.id, kc.sale_id, kc.sale_date, kc.sale_price, kc.sale_nbr, kc.join_status, kc.latitude, kc.longitude, kc.city, kc.zoning, kc.subdivision, kc.present_use,
                            kc.land_val, kc.imp_val, kc.year_built, kc.year_reno, kc.sqft_lot, kc.sqft)
        
                      
    session.close()
    
    kc_table = []
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
        kc_table.append(kc_dict)
    return jsonify(kc_table)
     
if __name__ == '__main__':
    austin_housing_app.run(debug=True)

            
    
    
            
    
    
