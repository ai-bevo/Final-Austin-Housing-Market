--DROP TABLE IF EXISTS seattle_sales

CREATE TABLE seattle_sales(
	id INT PRIMARY KEY,
    sale_id VARCHAR(50) NOT NULL,
    pinx VARCHAR(255),
    sale_date DATE,
    sale_price FLOAT NOT NULL,
    sale_nbr VARCHAR(50),
    sale_warning VARCHAR(255),
    join_status VARCHAR(50),
    join_year INT,
    latitude FLOAT,
    longitude FLOAT,
    area INT,
    city VARCHAR(100),
    zoning VARCHAR(50),
    subdivision VARCHAR(100),
    present_use INT,
    land_val FLOAT,
    imp_val FLOAT,
    year_built INT,
    year_reno INT,
    sqft_lot INT,
    sqft INT,
    sqft_1 INT,
    sqft_fbsmt INT,
    grade INT,
    fbsmt_grade INT,
    home_condition INT,
    stories FLOAT,
    beds INT,
    bath_full INT,
    bath_3qtr INT,
    bath_half INT,
    garb_sqft INT,
    gara_sqft INT,
    wfnt INT,
    golf INT,
    greenbelt INT,
    noise_traffic INT,
    view_rainier INT,
    view_olympics INT,
    view_cascades INT,
    view_territorial INT,
    view_skyline INT,
    view_sound INT,
    view_lakewash INT,
    view_lakesamm INT,
    view_otherwater INT,
    view_other INT,
    submarket VARCHAR(100),
	years INT
);

DROP TABLE IF EXISTS monthly_seattle_sales;

CREATE TABLE monthly_seattle_sales(
	id serial PRIMARY KEY,
	Years INT,
    Months INT,
    Average_Sale_Price FLOAT,
    Median_Sale_Price FLOAT,
    Total_Houses_sold INT
);

SELECT * FROM monthly_seattle_sales;