"""
data_loader.py
-----------------------------------------
Responsible for: Loading the dataset from HDFS into a Spark DataFrame.

What this file does:
  - Reads diabetic_data.csv from HDFS (NOT from a local folder).
  - Prints the row count, column count, and partition count.
  - Partition count shows that Spark is reading the file in parallel —
    this is the evidence that HDFS + distributed processing is working.

BEFORE RUNNING — do this once in your Ubuntu terminal:
    hdfs dfs -mkdir -p /user/student/cs4074/data
    hdfs dfs -put /path/to/diabetic_data.csv /user/student/cs4074/data/
    hdfs dfs -ls /user/student/cs4074/data/

CHANGE THIS IF NEEDED:
    If your Ubuntu username is not "student", run whoami in your terminal
    and replace "student" below with whatever it returns.
-----------------------------------------
CS4074 - Big Data Analytics
Clinical Outcome Prediction from Noisy Medical Records
Effat University | Spring 2026 | Dr. Naila Marir
"""

# ---------------------------------------------------------------
# CHANGE THIS to your Ubuntu username (run: whoami in terminal)
# ---------------------------------------------------------------
HDFS_USERNAME = "student"

# Full HDFS path — automatically built from your username above
HDFS_DATA_PATH = f"hdfs://localhost:9000/user/{HDFS_USERNAME}/cs4074/data/diabetic_data.csv"


def load_data(spark, path=None):
    """
    Load diabetic_data.csv from HDFS.
    """
    hdfs_path = path if path else HDFS_DATA_PATH

    print("\n[1] Loading dataset from HDFS...")
    print(f"   Path: {hdfs_path}")

    df = spark.read.csv(hdfs_path, header=True, inferSchema=True)

    num_partitions = df.rdd.getNumPartitions()

    print(f"   Rows       : {df.count():,}")
    print(f"   Columns    : {len(df.columns)}")
    print(f"   Partitions : {num_partitions}  <- Spark processes these in parallel via HDFS")

    return df
