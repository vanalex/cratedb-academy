import sqlalchemy as sa
import pandas as pd

dburi = "crate://localhost:4200"
query = "SELECT * FROM sys.summits ORDER BY country"

engine = sa.create_engine(dburi, echo=True)
with engine.connect() as connection:
    df = pd.read_sql(sql=sa.text(query), con=connection)
    df.info()
    print(df)