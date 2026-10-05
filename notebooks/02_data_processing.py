# Databricks notebook source
# MAGIC %md
# MAGIC # 02 - Sample Data Processing
# MAGIC
# MAGIC A small PySpark example that can be used to test notebook execution
# MAGIC after connecting the Git folder.

# COMMAND ----------

from pyspark.sql import functions as F

# COMMAND ----------

data = [
    (1, "Alice", "Data Engineering", 90000),
    (2, "Bob", "Analytics", 80000),
    (3, "Charlie", "Data Engineering", 95000),
    (4, "Diana", "Analytics", 85000),
]

columns = ["employee_id", "name", "department", "salary"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

department_summary = (
    df.groupBy("department")
      .agg(
          F.count("*").alias("employee_count"),
          F.avg("salary").alias("average_salary")
      )
      .orderBy("department")
)

display(department_summary)

# COMMAND ----------

# Version-control test:
# Change the transformation below, save the notebook,
# commit the change, and push it to GitHub.

result = (
    df.withColumn("salary_band", F.when(F.col("salary") >= 90000, "High")
                                  .otherwise("Standard"))
)

display(result)
