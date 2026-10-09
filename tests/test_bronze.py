# tests/test_bronze.py

bronze_count = spark.table("sample_ci_cd.bronze.customers").count()

assert bronze_count > 0, "Bronze table is empty"

print(f"Bronze row count: {bronze_count}")
print("Bronze test passed")