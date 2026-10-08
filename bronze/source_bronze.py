file_path = "/Volumes/data_sources_ci_cd/data_sources/data_sources_ci_cd_volumes/customer_data_100.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)
catalog = "sample_ci_cd"
schema = "bronze"
table_name = f"{catalog}.{schema}.customers"

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
spark.sql(f"CREATE DATABASE IF NOT EXISTS {catalog}.{schema}")

if not spark.catalog.tableExists(table_name):
    # Table does not exist yet — create it from the DataFrame schema
    df.write.saveAsTable(table_name)
else:
    # Table already exists — overwrite it with new data
    df.write.mode("overwrite").saveAsTable(table_name)
