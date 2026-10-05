# Databricks notebook source
# MAGIC %md
# MAGIC # 01 - Hello GitHub
# MAGIC
# MAGIC This notebook is a simple test for Databricks + GitHub version control.
# MAGIC
# MAGIC Workflow:
# MAGIC
# MAGIC ```text
# MAGIC Databricks Git Folder -> Commit -> Push -> GitHub
# MAGIC ```

# COMMAND ----------

print("Databricks + GitHub integration is working!")

# COMMAND ----------

project_name = "databricks-github-free-edition"
environment = "free-edition"

print(f"Project: {project_name}")
print(f"Environment: {environment}")

# COMMAND ----------

# Make a small change to this notebook, commit it, and push it.
# Then verify the commit in GitHub.

print("Test completed successfully.")
