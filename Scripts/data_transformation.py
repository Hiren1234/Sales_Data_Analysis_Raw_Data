import pandas as pd

from data_cleaning import clean_data
from data_loading import load_csv


def transorm_data(df):

    # month Col
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month

    # Year col
    df['Year'] = df['Date'].dt.year


    # Profit Margin
    df['Profit_Margin'] = (df['Profit'] / df['Sales'])*100.0
    df['Profit_Margin'] = (df['Profit_Margin'].round(2).astype(str) + '%')

    #Total Revenue
    df['Revenue'] = df['Sales']+df['Profit']
    df['Date'] = pd.to_datetime(df['Date'])
    # df['Month_Name'] = df['Date'].dt.month_name()
    # df['Year_Name'] = df['Date'].dt.year_name()
    #



    # print("\n Transformed Data")
    # print(df)
    return df



# transorm_data(clean_data(load_csv()))
