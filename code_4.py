import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
   query_text = f"(iso_a3 == '{country_code.upper()}' and date.str.contains('{year}'))"
   usa_df = df.query(query_text)
   return round(usa_df['dollar_price'].mean(),2)


def get_big_mac_price_by_country(country_code):
    query_text = f"(iso_a3 == '{country_code.upper()}')"
    rus_df = df.query(query_text)
    return round(rus_df['dollar_price'].mean(),2)




def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"(date.str.contains('{year}'))"
    ind_df = df.query(query_text)
    min_df_idx = ind_df['dollar_price'].idxmin()
    min_item = ind_df.loc[min_df_idx]
    return f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'],2)}"





def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"(date.str.contains('{year}'))"
    nor_df = df.query(query_text)
    max_df_idx = nor_df['dollar_price'].idxmax()
    max_item = nor_df.loc[max_df_idx]
    return f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'],2)}"



if __name__ == "__main__":
    first = get_big_mac_price_by_year(2003,"usa")
    print(first)

    second = get_big_mac_price_by_country("rus")
    print(second)

    third = get_the_cheapest_big_mac_price_by_year(2012)
    print(third)

    fourth = get_the_most_expensive_big_mac_price_by_year(2014)
    print(fourth)
# not using query text