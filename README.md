#  Smart Meter Real-Time Data Pipeline

##  Project Overview
Designed and implemented a scalable real-time IoT data pipeline processing ~50K+ records per day using AWS services.

# Technologies Used
- AWS Kinesis
- AWS Lambda
- AWS Glue (PySpark)
- Amazon S3
- Amazon Athena
- Amazon DynamoDB
- Amazon QuickSight

#  Architecture
IoT Devices → Kinesis → Lambda → S3 → Glue → Athena → QuickSight

#  Features
- Real-time streaming data ingestion
- Data validation and transformation using Lambda
- Batch ETL processing using AWS Glue
- Data lake storage in Amazon S3
- SQL querying using Athena
- Dashboard visualization using QuickSight

# Key Achievements
- Processed ~50K+ records/day
- Built scalable serverless architecture
- Improved query performance using partitioned data
