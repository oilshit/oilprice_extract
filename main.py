# import dependencies
import json, requests
import pandas as pd
import datetime
import sys

def get_blend_info(blend, period):
    """
    Function to read oil and price data
    based on blend and period params
    """

    # read oil anda gas price based on oilprice-api
    blend_url = requests.get("http://localhost:3000/prices/{}/{}".format(blend, period))
    blend_info = json.loads(blend_url.text)

    # testing data  
    # # print(blend_info["blend"])

    # prepare for accumulate prices data
    prices = []
    dates = []
    times = []

    # read and also accumulate prices data
    for price in blend_info["prices"]:
        price_time = datetime.datetime.fromtimestamp(int(price["time"]))

        prices.append(price["price"])
        dates.append(price_time.strftime("%Y-%m-%d"))
        times.append(price_time.strftime("%H:%M:%S"))

        # print(price["price"], price_time.strftime("%Y-%m-%d %H:%M:%S"))

    return {
        "prices": prices,
        "dates": dates,
        "times": times
    }

def save_to_csv_data(data):
    """
    Function to save prices data into CSV file
    """

    # init'd title
    field_name = ["Prices (USD/bbl)", "Date (CDT)", "Time (CDT)"]

    prices_df = pd.DataFrame(data)
    prices_df.columns = field_name
    prices_df.to_csv("prices-{}-{}.csv".format(sys.argv[1], sys.argv[2]), index=False)


if __name__ == "__main__":
    blend_data = get_blend_info(sys.argv[1], sys.argv[2])
    
    save_to_csv_data(blend_data)