from pyspark.sql.functions import col, trim, initcap, lower, upper, regexp_replace, current_timestamp, coalesce, lit

df = spark.table("sample_ci_cd.bronze.customers")

silver_df = (
    df
    # --- Deduplication: keep latest record per customer_id ---
    .dropDuplicates(["customer_id"])

    # --- Clean & standardize string columns ---
    .withColumn("first_name", trim(initcap(coalesce(col("first_name"), lit("")))))
    .withColumn("last_name", trim(initcap(coalesce(col("last_name"), lit("")))))
    .withColumn("email", lower(trim(regexp_replace(col("email"), r"\s+", ""))))
    .withColumn("phone", trim(regexp_replace(col("phone"), r"[^0-9+\-]", "")))
    .withColumn("city", trim(initcap(col("city"))))
    .withColumn("state", upper(trim(col("state"))))
    .withColumn("country", upper(trim(col("country"))))

    # --- Standardize column names to snake_case if needed ---
    # (adjust to match your actual bronze column names)

    # --- Data quality: flag invalid emails for review ---
    .withColumn("is_email_valid", col("email").rlike(r"^[^@\s]+@[^@\s]+\.[^@\s]+$"))

    # --- Silver-layer audit columns ---
    .withColumn("silver_ingested_at", current_timestamp())
    .withColumn("silver_source", lit("bronze.customers"))
)

(silver_df.write
    .mode("overwrite")
    .saveAsTable("sample_ci_cd.silver.customers"))

