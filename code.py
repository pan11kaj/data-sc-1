import pandas as pd;
import csv;
df = pd.read_csv("data.csv") #reading the data
del df["Star_name"]
del df["Mass"]
del df["Distance"]
del df["Radius"]
del df["serial"]
print(list(df))
df = df.rename({
    "serial.1":"serial",
    "Star_name.1":"star_name",
    "Distance.1":"distance",
    "Radius.1":"radius",
    "Mass.1":"mass"
},axis= 'columns')
df.to_csv("main.csv")