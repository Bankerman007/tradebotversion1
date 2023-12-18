from gui import timeframe_current, turn_off,entry_price, number_of_shares_entry, number_of_shares_partial,initial_stop_loss, take_profit,sell_partial, timeframe_current
#from api_calls import list_any_positions, place_order, exit_trade_order_final,exit_trade_partial,purchase_price, initial_stop
from test import list_any_positions, place_order, exit_trade_order_final,exit_trade_partial,purchase_price, initial_stop
import datetime
#from api_calls import timeframe_current
#from python_to_postgres import save_to_db

time_includes_milli = datetime.datetime.now()
time_without_leading_zero=time_includes_milli.isoformat(timespec='minutes').replace("-0", "-")
time_acceptable_format= time_without_leading_zero.replace("T"," ")

quantity= list_any_positions()

def submit_order_tests():
    current_price = timeframe_current
    #test to see if program is off or on.
    if turn_off == 0:
        pass                
        #initial order at entry price
    if not bool(quantity):
        if current_price <= entry_price:
            print('order placed on main')
            place_order()

    #check if stop loss is hit and sell if so.
    if quantity == number_of_shares_entry and current_price <= initial_stop_loss:
        print('stopped out on main')
        initial_stop()

    #check if first take profit target is hit & sell partial
    if quantity == number_of_shares_entry and current_price >= sell_partial:
        print('partial sold on main')
        exit_trade_partial()

    #check if second take profit target is hit
    if quantity == number_of_shares_partial and current_price >= take_profit:
        print('final sold on main')
        exit_trade_order_final()
        
submit_order_tests() 







    # if bool(quantity):
    #     entry_price = entry_price 
    #     if float(timeframe_current) - float(purchase_point) >= 4.00:
    #         exit_trade_order()
            #file.write(f'{datetime.datetime.now()} - Position exited at {current_price}. \n' )
            #new_data= (f'"{time_acceptable_format}","Position exited.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            #save_to_db(eval(new_data))
        #else:
            #new_data= (f'"{time_acceptable_format}","Price not at take profit level.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            #file.write(f'{datetime.datetime.now()} - Price point not acceptable to execute any trades. Market price {current_price}, Purchase Price {purchase_point}.\n' )
            #save_to_db(eval(new_data))

    # elif not bool(quantity):
    #     if acceptable_trade_criteria and not bool(quantity):
    #         place_order()
            #file.write(f'{datetime.datetime.now()} - Position is now open at {current_price}. \n' )
            # new_data= (f'"{time_acceptable_format}","Position is now open.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            # save_to_db(eval(new_data))  

        #else:
            #print(f'price point not acceptable to execute any trades') 
            #file.write(f'{datetime.datetime.now()} - Price point not acceptable to execute any trades. {current_price, stocks_last_fiveday_avg_close()}\n' )
            # new_data= (f'"{time_acceptable_format}","Price not at entry level.",{current_price},{stocks_last_fiveday_avg_close()},None')
            # save_to_db(eval(new_data))
