# Here now I am going to perform exploratory analysis
from data_cleaning import clean_data
from data_loading import load_csv
from data_transformation import transorm_data


def total_sales(df):

    return df['Sales'].sum()


def total_profit(df):
    return df['Profit'].sum()

def sales_by_region(df):
    return df.groupby('Region')['Sales'].sum()

def best_selling_product(df):
    return df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
# print("\n Exploratory Data Analysis")
# print(total_sales(transorm_data(clean_data(load_csv()))))
# print(total_profit(transorm_data(clean_data(load_csv()))))
# print(sales_by_region(transorm_data(clean_data(load_csv()))))


# print(total_sales(transorm_data(clean_data(load_csv()))))

#Month wise sales analysis
def month_wise_sales(df):
    monthly_sales = (
        df.groupby('Month')['Sales'].sum().sort_values(ascending=False)

        )
    return monthly_sales

# def Month_Name_Sales(df):
#   Monthly_Sales = df.groupby  (
#       df.groupby('Month_Name')['Sales'].sum().sort_values(ascending=False)
#
#     )
#   return Monthly_Sales

def Year_Wise_Sales(df):

    Yearly_Sales = (
        df.groupby('Year')['Revenue'].sum().sort_values(ascending=False)


    )
    return Yearly_Sales
def monthly_growth(df):
    Monthly_Sales = (
        df.groupby('Month')['Sales'].sum()
    )
    growth = (
        Monthly_Sales.pct_change()
    )*100
    return growth.round(2)