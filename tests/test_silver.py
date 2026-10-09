silver_count = spark.table("sample_ci_cd.silver.customers").count()

assert silver_count > 0, "Silver table is empty"

print(f"Silver row count: {silver_count}")
print("Silver test passed")