import pandas as pd
df = pd.read_csv("./big-mac-full-index.csv")

#query the big mac index for rows with data from the year 2018

print(type(df["date"][0]))  # we need 'date' on square brackets because its the key to what we need

query = "date >= '2018-01-01' and date < '2019-01-01'"
#query2 = "date < 2019-01-01"
df = df.query(query)

print(df)