from sqlalchemy import create_engine

def upload_to_mysql(df):

    username = "root"

    password = "root"

    host = "localhost"

    database = "temp1"

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    df.to_sql(
        name='processed_sales',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("DATA UPLOADED SUCCESSFULLY")