# Databricks notebook source
# MAGIC %md
# MAGIC # 03 - Data Quality Validation
# MAGIC
# MAGIC Sample validation notebook for demonstrating how reusable
# MAGIC Databricks notebooks can be maintained in GitHub.

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

data = [
    (1, "Alice"),
    (2, "Bob"),
    (None, "Missing ID"),
    (4, None),
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name"]
)

display(df)

# COMMAND ----------

null_id_count = df.filter(F.col("employee_id").isNull()).count()
null_name_count = df.filter(F.col("employee_name").isNull()).count()

print(f"Null employee_id count: {null_id_count}")
print(f"Null employee_name count: {null_name_count}")

# COMMAND ----------

quality_results = {
    "employee_id_not_null": null_id_count == 0,
    "employee_name_not_null": null_name_count == 0,
}

for check, passed in quality_results.items():
    status = "PASS" if passed else "FAIL"
    print(f"{status}: {check}")

# COMMAND ----------

# In a real project, failed checks could be logged to a
# data-quality table or monitoring system.
