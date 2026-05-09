from fontTools.unicodedata import Scripts

from Scripts.data_loading import load_csv
from Scripts.analysis import (total_sales, total_profit,sales_by_region,best_selling_product,Year_Wise_Sales,month_wise_sales,monthly_growth)
import pandas as pd
from Scripts.data_loading import load_csv
from Scripts.data_cleaning import clean_data
from Scripts.data_transformation import transorm_data
from visulization import sales_chart, year_chart, monthly_sales_chart
from my_sql_connection import upload_to_mysql
from Scripts.report_generator import generate_report

# Now Load Data

df = load_csv()

print("\n Raw Data")
print(df.head())

#Clean Data
df = clean_data(df)
print("\n Cleaned Data")
print(df.head())

#Transform Data
df = transorm_data(df)
print("\n Transformed Data")
print(df.head())

#Analysis
print("\n Total Sales")
print(total_sales(df))
print("\n Total Profit")
print(total_profit(df))
print("\n Sales By Region")
region_sales= sales_by_region(df)
print(region_sales)
print("\n Year Wise Revenue")
Year_Wise_Revenue = Year_Wise_Sales(df)
print(Year_Wise_Revenue)

print("\n Monthly_Sales")
Monthly_Sales = month_wise_sales(df)
print(Monthly_Sales)





print("\n Best selling Product")
print(best_selling_product(df))

# Month_Wise_sales
# print("\n Monthly Sales")
# print((df))

# Month Wise Sales
print("\n Yearly Sales ")
print(Year_Wise_Sales(df))

# Growth Month Wise
print("\n Monthly Growth")
print(monthly_growth(df))

# Chart Visualization
sales_chart(region_sales)
year_chart(Year_Wise_Revenue)
monthly_sales_chart(Monthly_Sales)

upload_to_mysql(df)

generate_report(df)

#Export file
df.to_csv("Outputs/Reports/Processed_sales.csv", index=False)

print("\n Project Completed Successfully")

















# Clean Data
# print("\n Total Sales")
# print(total_sales(df))
#
# # Total Profit
# print("\n Total Profit")
# print(total_profit(df))
#
# # Sales By Region
# print("\n Sales By Region to identify the best performing region")
# print(sales_by_region(df))
#
# # Best Selling Product
# print("\n Best Selling Product")
# print(best_selling_product(df))
#

