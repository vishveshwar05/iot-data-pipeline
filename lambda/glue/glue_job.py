from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IoT ETL").getOrCreate()

df = spark.read.json("s3://your-bucket/raw-data/")

# Transformation
df_clean = df.filter(df.usage >= 0)

# Save processed data
df_clean.write.mode("overwrite").parquet("s3://your-bucket/processed-data/")
