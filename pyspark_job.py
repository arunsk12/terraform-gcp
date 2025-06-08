from pyspark.sql import SparkSession

def run_spark_job():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("GCP Demo") \
        .getOrCreate()

    # Create a simple DataFrame
    data = [("Arun", 28), ("Gandhi", 144), ("King", 45)]
    df = spark.createDataFrame(data, ["Name", "Age"])

    # Show the DataFrame
    df.show()

    # Write to Google Cloud Storage (GCS)
    df.write.csv("gs://bug-bucket-123/demo_output.csv")

    spark.stop()

if __name__ == "__main__":
    run_spark_job()
