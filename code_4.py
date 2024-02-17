import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    filtered_data = big_mac_file[(big_mac_file['year'] == year) & (big_mac_file['country_code'] == country_code)]

    mean_price = filtered_data['dollar_price'].mean()

    rounded_mean_price = round(mean_price,2)

    return rounded_mean_price

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    year = 2012
    country_code = 'us'

    result = get_big_mac_price_by_year(year, country_code)
    print(f"The mean Big Mac price in {country_code} in {year}is : ${result}")
    
