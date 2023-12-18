import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime, timedelta
from business_calendar import Calendar, MO, TU, WE, TH, FR
import pandas as pd
from gui import symbol, number_of_shares_entry, number_of_shares_partial, number_of_shares_exit

#paper account
key = os.environ['API_KEY']
secret = os.environ['SECRET_KEY']
alpaca_endpoint = os.environ['APCA_API_BASE_URL']
api = tradeapi.REST(key,secret,alpaca_endpoint,)

#live account
# key = os.environ['APCA_API_KEY_LIVE']
# secret = os.environ['APCA_Secret_KEY_LIVE']
# alpaca_endpoint = os.environ['APCA_API_LIVE']
# api = tradeapi.REST(key,secret,alpaca_endpoint,)

symbol = symbol
timeframe_day = "1Day"
timeframe_hour= "1Hour"
timeframe_5min= "5Min"
timeframe_1min= "1Min"
timeframe_current= "current"

current_time= datetime.now()
day_minus_one = datetime.today() - timedelta(days=1)
h_comma= day_minus_one.strftime('%Y,%d,%m')
h_dash= day_minus_one.strftime('%Y-%m-%d')
date1 = h_comma
cal = Calendar(workdays=[MO,TU,WE,TH,FR], holidays=['2023-01-16','2023-02-20','2023-04-07','2023-05-29','2023-06-19','2023-07-04','2023-09-04','2023-11-23','2023-12-25'])
date2 = cal.addbusdays(date1, -5)
date2=(date2.strftime('%Y-%m-%d'))

now = h_dash
end = h_dash
start = date2

def list_any_positions():
    #quantity= api.list_positions()
    data = api.get_position(f'{symbol}')
    position = data.qty    
    print(position)
    return position

def timeframe_current():
    price_current = api.get_bars(symbol,timeframe_current,start,end,limit=5).df
    return price_current

def place_order():
    api.submit_order(symbol, number_of_shares_entry,'buy', 'market','gtc',)

def initial_stop():
    api.submit_order(symbol, number_of_shares_entry, 'sell', 'market','gtc')

def exit_trade_partial():
    api.submit_order(symbol, number_of_shares_partial, 'sell', 'market','gtc')

def break_even_stop():
    api.submit_order(symbol, number_of_shares_exit, 'sell', 'market','gtc')

def exit_trade_order_final():
    api.submit_order(symbol, number_of_shares_exit, 'sell', 'market','gtc')
   
def purchase_price():
    purchase_price = (api.get_position(symbol).avg_entry_price)
    return float(purchase_price)

list_any_positions()

# def order_history():
#     orders= api.list_orders(status="closed", limit=100).df
#     file=open(r'C:\Users\scott\Documents\Python\Trading_bot\closed_orders.txt', 'a')
#     file.write(f'{orders} -. \n' )

# def get_profits():
#     data= api.get_portfolio_history(period="3M",timeframe="1D").df
#     profits =data["profit_loss"]
#     return profits

# def assets():
#     assets= api.list_assets()
#     print(assets)




