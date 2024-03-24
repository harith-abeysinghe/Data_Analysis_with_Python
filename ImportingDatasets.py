import pandas as pd
import numpy as np
import requests
from io import StringIO

# URL of the file to download
file_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

# Download the file
response = requests.get(file_url)

# Check if the request was successful
if response.status_code == 200:
    # Read the content of the file into a DataFrame
    content = response.content.decode('utf-8')
    df = pd.read_csv(StringIO(content))
    print("The first 5 rows of the dataframe")
    print(df.head(5))

    print("The last 10 rows of the dataframe")
    print(df.tail(10))

    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
               "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
               "engine-type",
               "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
               "peak-rpm", "city-mpg", "highway-mpg", "price"]
    print("headers\n", headers)

    df.columns = headers

    print(df.columns)

    print("The first 5 rows of the dataframe")
    print(df.head(5))

    df1 = df.replace('?', np.NaN)
    df = df1.dropna(subset=["price"], axis=0)
    print("The first 20 rows of the dataframe")
    print(df.head(20))

    print(df.columns)

    df.to_csv("automobile.csv", index=False)

    print("The data types of the columns are")
    print(df.dtypes)

    print("The summary of the dataframe is")
    print(df.describe())

    print("The summary of the dataframe inlcuding NaN is")
    print(df.describe(include="all"))

    print("The summary of the columns length and compression-ratio is")
    print(df[['length', 'compression-ratio']].describe())

    print("Concise Summary of the dataframe")
    print(df.info())
else:
    print("Failed to download the file")
