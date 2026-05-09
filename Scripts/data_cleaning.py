import pandas as pd

from data_loading import load_csv


def clean_data(df):
   # Remove duplicates
    df = df.drop_duplicates()

   # Convert Data Col
    df['Date'] = pd.to_datetime(df['Date'])

    # Fill missing profit values
    df['Profit'] = df['Profit'].fillna(0)

    # print("\n Data Cleaned")
    # print(df)

    return df


# clean_data(load_csv())

