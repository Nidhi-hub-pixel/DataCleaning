import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df = df.rename({
    "Luminosity","Star_name","Distance","Mass","Radius"
},axis='columns')

df.to_csv("final.csv")
