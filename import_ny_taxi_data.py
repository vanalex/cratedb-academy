"""
Import a parquet file into CrateDB using polars + sqlalchemy

Install the dependencies to run this program::

    pip install --upgrade pandas polars pyarrow sqlalchemy-cratedb
"""

import polars

CRATE_URI = 'crate://localhost:4200'
FILE_PATH = './data/yellow_tripdata_2024-01.parquet'

def import_taxi_data():
    df = polars.read_parquet(FILE_PATH)
    df.write_database(table_name='ny_taxi',
                    connection=CRATE_URI,
                    if_table_exists='append')

if __name__ == '__main__':
    import_taxi_data()