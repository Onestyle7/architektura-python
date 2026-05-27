import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["PYSPARK_PYTHON"] = r"C:\Users\klusb\Desktop\architektura-python\.venv\Scripts\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\klusb\Desktop\architektura-python\.venv\Scripts\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from pyspark.sql.functions import broadcast
import matplotlib.pyplot as plt

spark = SparkSession.builder \
    .appName("Chicago crimes") \
    .master("local[*]") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.bindAddress", "127.0.0.1") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem") \
    .getOrCreate()

df_crimes = spark.read.option("header", True) \
.option("multiline", True)\
.csv("chicago_crimes_sample.csv")

def przypisz_pore_dnia(hour):
    if hour is None:
        return "nieznana"
    if 6 <= hour < 12:
        return "rano"
    elif 12 <= hour < 18:
        return "dzien"
    elif 18 <= hour < 22:
        return "wieczór"
    else:
        return "noc"

df_crimes = df_crimes.withColumn("Date", F.to_timestamp(F.col("Date"), "yyyy-MM-dd'T'HH:mm:ss.SSS"))
df_crimes = df_crimes.withColumn("Hour", F.hour(F.col("Date")))

pora_dnia_udf = F.udf(przypisz_pore_dnia, StringType())

df_crimes = df_crimes.withColumn("Pora_dnia", pora_dnia_udf(F.col("Hour")))
df_crimes.cache()

df_crimes_filtered = df_crimes.filter(F.col("year").isNotNull() & F.col("primary_type").isNotNull())

df_analiza = df_crimes_filtered.groupBy("location_description", "Pora_dnia") \
    .agg(F.count("*").alias("Ilosc_przestepstw")) \
    .orderBy(F.col("Ilosc_przestepstw").desc())

df_analiza.show(20, truncate=False)
df_analiza.explain(True)
analiza_pd = df_analiza.limit(15).toPandas()

analiza_pd['Nazwa'] = analiza_pd['location_description'] + " (" + analiza_pd['Pora_dnia'] + ")"

plt.figure(figsize=(10, 6)) 

plt.bar(analiza_pd['Nazwa'], analiza_pd['Ilosc_przestepstw'], color='brown')

plt.title('Top 15 konfiguracji Miejsc i Pór Dnia przestępstw')
plt.xlabel('Miejsce (Pora dnia)')
plt.ylabel('Ilość przestępstw')

plt.xticks(rotation=45, ha='right') 

plt.tight_layout()

plt.show()
