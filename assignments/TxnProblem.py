"""
There is one input dataset named : Transaction:
a.	Write a pySpark / Python program, which reads the input transaction table
and provides output as given Detail_trans.

Description: Customers are represented as Cust column. Each customer does a deposit marked by column “D”
and withdrawal marked as “W” . Output table has column Type which has 2 values N and P.
N = Negative value and P = Positive value.
Input : transaction
Cust                       TransAmt                    TransType
1                              100                      D
2                              200                      W
1                              500                      W
1                              100                      W
3                              200                      D
3                              400                      D

Output : Detail_trans
Cust                       TransAmt                            Type
1                              500                             N
2                              200                             N
3                              600                             P

"""
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("Txn Prob") \
    .getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.read \
    .option("header", "true") \
    .csv("cust_txn.csv")

df = df.withColumn("TransAmt", \
                   when(col("TransType") == lit("W"), col("TransAmt") * lit(-1)).otherwise(col("TransAmt")))

df = df.groupBy("Cust").agg(sum("TransAmt").alias("TransAmt"))

df.withColumn("Type", when(col("TransAmt") < lit(0), "N").otherwise("P")).show()
