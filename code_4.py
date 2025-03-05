import csv
import pandas as pd              #this line imports pandas as "pd" 
big_mac_file = './big-mac-full-index.csv'  # make sure to store file path
df = pd.read_csv(big_mac_file)         #dataframe

def get_big_mac_price_by_year(year,country_code):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01' and iso_a3 == '{country_code}'" #query filters rows with date, iso_a3.
    q_df = df.query(query)          #dataframe filtered by query
    return round(q_df['dollar_price'].mean(),2)   # calculate mean price for filtered rows  #,2 rounds mean 3 deci places

def get_big_mac_price_by_country(country_code):
    query = f"iso_a3 == '{country_code.upper()}'" #upper makes sure country code is uppercase #query filters rows to match iso_a3
    q_df = df.query(query)   # apply filter
    return round(q_df["dollar_price"].mean(),2) # average big mac price for specific country #,2 decimals

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01'"  #filter by year
    q_df = df.query(query)        #will provide only big macs for specific year
    min_row = q_df.loc[q_df["dollar_price"].idxmin()]  #find index of row with smallest price #df.loc retrieves full row for cheapest big mac
    return f"{min_row['name']}({min_row['iso_a3']}): ${round(min_row['dollar_price'],2)}" #min_row name retrieves country name  #min_row[dollar_price gets cheapest price

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01'" #filter requested year
    q_df = df.query(query)
    max_row = q_df.loc[q_df["dollar_price"].idxmax()]  #q_df.loc gives full row priciest big mac
    return f"{max_row['name']}({max_row['iso_a3']}): ${round(max_row['dollar_price'],2)}" #gets country name, country code, highest price

if __name__ == "__main__":

    print(get_big_mac_price_by_year(2012,'arg'))
    print(get_big_mac_price_by_country('arg'))
    print(get_the_cheapest_big_mac_price_by_year(2000))
    print(get_the_most_expensive_big_mac_price_by_year(2003))
    