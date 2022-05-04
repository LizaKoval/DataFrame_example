import findspark
import pyspark
findspark.init()
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[1]") \
        .appName("NewSparkTry") \
        .getOrCreate()

df = spark.read.json('test_data')
#print(f'there are {df.count()} lines')
df.printSchema()

# create rdd with data, create schema and then tramslate rdd into dataframe
