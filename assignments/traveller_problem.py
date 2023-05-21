from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("Txn Prob") \
    .getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

travel_info_df = spark.sparkContext \
    .parallelize([("LA", "SF"), ("SF", "LA"), ("KC", "SF")]) \
    .toDF("FRO", "TO")

travel_info_df.show()

traveller_df = spark.sparkContext \
    .parallelize([("Chender", "Bandaru"), ("Amit", "Kumar"), ("Jack", "Lawson")]) \
    .toDF("FirstName", "LastName")


# df.withColumn("Type", when(col("TransAmt") < lit(0), "N").otherwise("P")).show()
