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

You can also get the json data by calling the API `https://api.eia.gov/series/?api_key=YOUR_API_KEY&series_id=NG.RNGWHHD.D`, This for the daily prices gas.
in the script the default duration type is daily 

     ```py
    # function return the csv file
    csv_file( duration_type="daily")
    
     ```
   You change the duration type `daily` by `monthly` to get the csv file for monthly [monthly_price_gas](https://github.com/msylla01/Data_wrangling_exercise/blob/main/gas_prices/data/monthly_gas_prices.csv).
   
## Script
