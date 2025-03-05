import pandas as pd
file_name = "./big-mac-full-index.csv"

df = pd.read_csv(file_name)

def get_year_from_date(row):
    #return row["date"][:4]   # gives 4 digits
    return row["date"].split("_")[0]
new_column = df.apply(get_year_from_date,axis=1)
#print(new_column)

df["year"] = new_column

print(df)