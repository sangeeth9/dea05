import pandas as pd
from sqlalchemy import create_engine
import time


def fileLoader(filepath):
    data = pd.read_csv(filepath)
    return data


def duplicateCleaner(df):
    return df.drop_duplicates().reset_index(drop=True)


def naCleaner(df):
    return df.dropna().reset_index(drop=True)


def dateCleaner(col, df):
    df[col] = df[col].astype(str).str.replace('"', "", regex=True)
    df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

    error_flag = df[col].isna()
    df = df[~error_flag].copy()
    df.reset_index(drop=True, inplace=True)

    return df


def enrich_dateDuration(colA, colB, df):
    df['date_delta'] = (df[colB] - df[colA]).dt.days

    df.loc[df['date_delta'] < 0, 'valid_loan_flag'] = False
    df.loc[df['date_delta'] >= 0, 'valid_loan_flag'] = True

    return df


def writeToSQL(df, table_name, server, database):
    connection_string = (
        f'mssql+pyodbc://@{server}/{database}'
        f'?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
    )

    engine = create_engine(connection_string)

    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Table {table_name} written to SQL")
    except Exception as e:
        print(f"Error writing {table_name} to SQL Server: {e}")


if __name__ == '__main__':
    pipeline_start_time = time.time()

    print('**************** Starting Clean ****************')

    server = 'localhost'
    database = 'DE5_Module5'

    filepath_books = 'data/03_Library Systembook.csv'
    filepath_customers = 'data/03_Library SystemCustomers.csv'

    date_columns = ['Book checkout', 'Book Returned']

    # Books data
    data = fileLoader(filepath_books)
    original_book_records = len(data)

    data = duplicateCleaner(data)
    data = naCleaner(data)

    for col in date_columns:
        data = dateCleaner(col, data)

    data = enrich_dateDuration(
        df=data,
        colA='Book checkout',
        colB='Book Returned'
    )

    cleaned_book_records = len(data)
    dropped_book_records = original_book_records - cleaned_book_records

    # Customer data
    data2 = fileLoader(filepath_customers)
    original_customer_records = len(data2)

    data2 = duplicateCleaner(data2)
    data2 = naCleaner(data2)

    cleaned_customer_records = len(data2)
    dropped_customer_records = original_customer_records - cleaned_customer_records

    # Pipeline execution time
    pipeline_end_time = time.time()
    pipeline_execution_time_seconds = round(
        pipeline_end_time - pipeline_start_time,
        2
    )

    # Metrics table for Power BI dashboard
    metrics = pd.DataFrame({
        'metric_name': [
            'book_records_processed',
            'book_records_dropped',
            'customer_records_processed',
            'customer_records_dropped',
            'total_records_processed',
            'total_records_dropped',
            'pipeline_execution_time_seconds'
        ],
        'metric_value': [
            cleaned_book_records,
            dropped_book_records,
            cleaned_customer_records,
            dropped_customer_records,
            cleaned_book_records + cleaned_customer_records,
            dropped_book_records + dropped_customer_records,
            pipeline_execution_time_seconds
        ]
    })

    print('**************** RECORD COUNTS ****************')
    print(metrics)

    print('**************** DATA CLEANED ****************')

    print('Writing to SQL Server...')

    writeToSQL(
        data,
        table_name='loans_bronze',
        server=server,
        database=database
    )

    writeToSQL(
        data2,
        table_name='customer_bronze',
        server=server,
        database=database
    )

    writeToSQL(
        metrics,
        table_name='pipeline_metrics',
        server=server,
        database=database
    )

    print('**************** End ****************')