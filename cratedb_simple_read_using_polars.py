import polars as pl

dburi = "crate://localhost:4200"
query = "SELECT * FROM sys.summits ORDER BY country"

#df = pl.read_database_uri(query, dburi, protocol='cursor')
#print(df.head())
df = pl.read_database_uri(query, dburi)
print(df.head())