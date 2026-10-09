gold_count = spark.table("sample_ci_cd.gold.dim_customers").count()

assert gold_count > 0, "Gold table is empty"

print(f"Gold row count: {gold_count}")
print("Gold test passed")