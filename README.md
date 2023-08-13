# Seattle Washington Housing Market
---
Group Project # 4 - Seattle Washington Housing Market with machine learning model
<p align="center">
<img src="images/seattle.jpg" alt="Austin skyline" width="500" height="300">
</p>

---
## 🏠 Table of Contents
- [Background](#background)
- [Process](#process)
- [Data Sources](#data)
- [Findings and Conclusions](#findings)
- [Part 1: Populate Database in pgAdmin](#part-1)
- [Part 2: Python Flask API ](#part-2)
- [Part 3: Dashboard Page](#part-3)
- [Part 4: ML modeling - multiple linear regression model](#part-4)
- [Part 5: Tableau Dashboard](#part-5) - placeholder - https://public.tableau.com/app/profile/allan.ivey/viz/AustinDashboard-MiniProject/Dashboard1

---
## 🏠 Background <a name="background"></a>

Welcome to the Seattle Washington Housing Market Analysis project, where we dive deep into the real estate dynamics of one of the Pacific Northwest's most exciting cities. This repository is dedicated to an in-depth exploration of the housing market trends spanning the years 2018 to 2022 in the bustling urban landscape of Seattle. Powered by the combined prowess of PostgreSQL and a Python Flask application, our project presents an interactive dashboard that offers an insightful overview of the housing market's evolution during this significant timeframe.

We completed a comprehensive analysis and a visualization dashboard using a Python Flask-powered API, HTML/CSS, JavaScript, and a SQL database plotly, leaflet, D3 and charts.js. This project seeks to provide valuable insights in understanding Seattle's real estate dynamics.

In addition to dissecting historical trends, we've developed a cutting-edge machine learning model aimed at forecasting housing prices in the Seattle area. Leveraging the power of Random Forest and Linear Regression algorithms, we've trained a robust predictive model that takes into account a multitude of factors affecting housing prices. By incorporating data on property attributes, location details, economic indicators, and more, our model serves as a powerful tool for prospective buyers, sellers, and investors looking to make informed decisions in the complex Seattle real estate landscape.

# 🏠 Final Production Database
Uploaded the CSV data files into a Postgres database a relational database management system.

---
## 🏠 Process <a name="process"></a>

1. Clean data in CSV files.
2. Import data into a Database.
3. Create a flask app.
4. Import table into Jupyter Notebook.
5. Process data using a Machine Learning Model.
6. Analyze the results and create visualizations.
7. Create a dashboard and presentation.

---
## 🏠 Data Sources <a name="data"></a>
Data for this dataset was pulled from a kaggle csv. All data collected and used in this analysis is intended for educational purposes only.

1. seattle_sales_all_data.csv (From kaggle)
2. seattle_sales.csv (cleaned up kaggle csv of only seattle from 2018-2022)

---
## 🏠 Findings and Conclusions <a name="findings"></a>
The following findings and conclusions from the analysis are as follows:

 

 
---
## 🏠 Part 1: Populate Database in pgAdmin <a name="part-1"></a>
Deeper discription of the data can be found in the Resources folder king_county_SQL_schema.sql document

---
## 🏠 Part 2: Python Flask API  <a name="part-2"></a>
The python Flask api was used to jsonify the databases:


---
## 🏠 Part 3: Dashboard Page <a name="part-3"></a>


---
## 🏠 Part 4: ML modeling - multiple linear regression model <a name="part-4"></a>
Data Exploration and Preprocessing

Model Selection
  -  Pros:
  -  Cons:

About our Model

Model Analysis

---

## 🏠 Part 5: Tableau Dashboard <a name="part-5"></a>

# Housing Distribution in Seattle (2018-2022) with Square Feet:
This Tableau visualization is a dynamic map representing residential houses in Seattle between 2018 and 2022. The map is color-coded to display the distribution of houses based on square footage and has a filter to select the number of bedrooms. Each house is represented by a marker on the map, and the color e of the marker corresponds to the square footage. This visualization provides a quick overview of the spatial distribution of different-sized houses with varying bedroom counts, allowing users to identify trends and patterns in the housing market over the specified years.

# Average Sales Price Mapping with Average & Median Price Analysis (2018-2022):
This Tableau visualization combines a map with line graphs to depict the average sales prices of homes in Seattle from 2018 to 2022. The map itself displays geographic areas with color gradients representing different price ranges. The graphs show the trends in both average and median prices over the same period. The graph's x-axis represents the years, while the y-axis represents the price. This visualization enables users to compare the average and median price trends against the spatial distribution of price ranges, giving insights into the changing real estate market dynamics and providing a comprehensive view of price fluctuations over time.
