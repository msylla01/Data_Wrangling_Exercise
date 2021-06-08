# Data wrangling exercise
 Data Wrangling Exercise - Natural Gas Prices 
 
 script in python to get a nice CSV file of natural gas prices.


## Requirements to use this Project

In this project all the script is wrtiten in python, so you must have python installed in your system.
If you dont have Python you can install here [python](https://www.python.org/downloads/)

### 1- Clone the project :

    ```sh
    git clone https://github.com/msylla01/Data_wrangling_exercise.git
    
    ```

### 2-  Dependencies
    ```sh
    pip install -r requirements.txt
    
    ```
    
### 3- Get EIA API key

To run this project You have to generate your private API Key. 
You can download your key by registering [here](https://www.eia.gov/opendata/register.php).

**More information about the API** [here](http://www.eia.gov/developer) 

You can also get the json data by calling the API `https://api.eia.gov/series/?api_key=YOUR_API_KEY&series_id=NG.RNGWHHD.D`, This for the daily prices gas.
in the script the default duration type is daily 

     ```py
    # function return the csv file
    csv_file( duration_type="daily")
    
     ```
   You can change the duration type `daily` by `monthly` to get the csv file for monthly [monthly_price_gas](https://github.com/msylla01/Data_wrangling_exercise/blob/main/gas_prices/data/monthly_gas_prices.csv).
   
## Script
You can find the script [here](https://github.com/msylla01/Data_Wrangling_Exercise/blob/main/gas_prices/script/get_prices_natural_gas.py)

In this script we have two functions, `get_list_of_data` and `csv_file`.<br>
the first function calling **get_list_of_data**  this function take the `duration type` like 'daily' or 'monthly' and return the list, we have in this liste the date and their prices.
The second function **csv_file** take also the `duration type`,  get the data list and stort it to the csv files in [data](gas_prices/data)
