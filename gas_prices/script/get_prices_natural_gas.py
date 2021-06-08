"""
All the data Daily Prices 'Henry Hub Natural Gas Spot Price (Dollars per Million Btu)'

The script have two function  that calls the EIA API and 
put the data in to the CSV file located in Data_Wrangling_Exercise/gas_prices/data/daily_gas_prices.csv 

"""


import requests
import json
import pandas as pd


def get_list_of_data(duration_type = "daily"):
    
    """
     API call the EIA and returns a list of daily prices.
     
     #The parameters duration_type : is str
     #Default value 'daily'
     #The value can be 'daily', 'weekly', 'monthly', 'annually'.
     
    """
    
    #YOUR API_KEY HERE
    # get the EIA API key 
    #Register at https://www.eia.gov/opendata/register.php
    
    API_KEY = 'YOUR_API_KEY'
    
    # URL for request to the EIA API 
    B_URL = "https://api.eia.gov/series/?api_key={}&series_id=".format(
        API_KEY
    )
    
    # Series ID for the different duration type we can get this on json request
    series_uni_id = {
        "daily": "NG.RNGWHHD.D",
        "weekly": "NG.RNGWHHD.W",
        "monthly": "NG.RNGWHHD.M",
        "annually": "NG.RNGWHHD.A"
    }
    
    
    # Generate the  URL  from the B_URL and series_id
    URL  = B_URL + series_uni_id.get(duration_type,"daily")
    
    #Using the python requests library and API reponse 
    #the response of request is  stored in the variable df and the format is json data as disctionary in python.
    df = json.loads(requests.get(URL).content)
    
    #List of days and corresponding prices in Dollars($) per Million Btu
    list_df = df.get("series")[0].get("data")
    
    # format dates returned  "19970108" (yyyymmdd)
    #sort the list started by big number or oldest dates 
    list_df.sort()
    
    
    return list_df

#################################################################
###### 
######
######Second function transform the list data to csv format for each types
###################################################################


def csv_file( duration_type="daily",filepath=None):
    
    """
    Data to CSV file
    
    #parameters 
    #filepath: optional and type is str
    #
    
    """
    
    # Default File path 
    
    path = 'gas_prices/data/{}_gas_prices.csv'.format(duration_type)
    
    if type(filepath) == str:
        path = filepath

    # get the list of data with the duration type
    list_df = get_list_of_data(duration_type = duration_type)
    
    # transform list to csv format
    df = pd.DataFrame( list_df, columns= ["Date", "Price"])
    df.to_csv(path, index = False)
csv_file(duration_type="daily")
