from pyspark.sql.functions import col, current_timestamp, monotonically_increasing_id

# ---------------------------------------------------------------------------
# 1. Read the Silver layer customers table
# ---------------------------------------------------------------------------
df_silver = spark.table("sample_ci_cd.silver.customers")
display(df_silver.limit(10))

# ---------------------------------------------------------------------------
# 2. Gold layer – Dimension table: dim_customers
#    (slowly-changing customer attributes)
# ---------------------------------------------------------------------------
dim_customers = (
    df_silver
    .select(
        col("customer_id"),
        col("first_name"),
        col("last_name"),
        col("email"),
        col("phone"),
        col("city"),
        col("state"),
        col("country"),
        col("signup_date"),
        col("customer_segment"),
        col("status"),
        current_timestamp().alias("gold_loaded_at"),
    )
    .dropDuplicates(["customer_id"])
)

(dim_customers.write
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("sample_ci_cd.gold.dim_customers"))

print("dim_customers written")

# ---------------------------------------------------------------------------
# 3. Gold layer – Fact table: fact_customer_transactions
#    (customer-related measures / events)
# ---------------------------------------------------------------------------
# Adjust the column names below to match the event/measure columns that
# actually exist in your silver table (e.g. order_id, amount, order_date, etc.).
# Exclude dimension attributes from the fact table; keep measures and FK
fact_columns = [
    c for c in df_silver.columns
    if c not in (
        "first_name", "last_name", "email", "phone",
        "city", "state", "country", "signup_date",
        "customer_segment", "status", "silver_source",
    )
]

fact_customer_metrics = (
    df_silver
    .select(*fact_columns)
    .withColumn("record_id", monotonically_increasing_id())
    .withColumn("gold_loaded_at", current_timestamp())
)

(fact_customer_metrics.write
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("sample_ci_cd.gold.fact_customer_metrics"))

print("fact_customer_metrics written")

