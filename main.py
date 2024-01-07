import ccxt
import time

# Initialize Phemex API
exchange = ccxt.phemex({
    'apiKey': 'your api key',
    'secret': 'your api secret',
})

symbol = 'NEAR/USDT'
sellorder_amount = 0
buyorder_amount = 0
binary = 0
bought_price = 0
total_profit_loss = 0

def get_near_price():
    ticker = exchange.fetch_ticker(symbol)
    return float(ticker['ask']) 
R = 4.0 / get_near_price()   #CHANGE ALL 1.5 VALUES TO WHATEVER AMOUNT OF USDT YOU WANT TO USE IN EACH SELL/BUY
BuyPrice = 4.0
buy_amount = 4.0

# Initialize Phemex API
exchange = ccxt.phemex({
    'apiKey': '3f184439-0db7-4334-862b-53cf3651ffc4',
    'secret': 'FXn3yfCGh13jTkOiNJ8OzDwfczXxjgsQHhlb6Rq31Uo1OTI1ZDU5My0yODJiLTRhNzItOGUzNy1mMjA5ZGFjMDVkMmY',
})

symbol = 'NEAR/USDT'
sellorder_amount = 0
buyorder_amount = 0
binary = 0
bought_price = 0
total_profit_loss = 0

def get_near_price():
    ticker = exchange.fetch_ticker(symbol)
    return float(ticker['ask'])  

BuyPrice = 4.0
buy_amount = 4.0
def place_buy_order():
    global binary, bought_price
    print("Placing buy order for NEAR...")
    bought_price = final_price  
    order = exchange.create_market_buy_order(symbol, buy_amount / bought_price)
    print("NEAR buy order made and most likely successful")
    binary = 1

def place_sell_order(amount):
    global total_profit_loss, binary
    print("Placing sell order for NEAR...")
    sell_price = final_price
    order = exchange.create_market_sell_order(symbol, amount / sell_price)
    binary = 0

while True:
    try:
        if binary == 0:
          initial_price = get_near_price()
          print('buy price point 1:', initial_price)
          time.sleep(90)
          final_price = get_near_price()
          print('buy price point 2:', final_price)
            
          if final_price <= initial_price - 0.004:
            place_buy_order()
        else:
          print("No buy order could be placed.")

#SELL (binary) variables are here to prevent a couple of errors
        if binary == 1:
            current_price = get_near_price()
            print('sell price point :', current_price)
            if current_price >= bought_price + 0.01:
                balance = exchange.fetch_balance()
                NEAR_available = balance['total']['NEAR']  
                amnt = 1.5
                place_sell_order(amnt)
            else:
                print("No sell order placed.")
        else:
            print('SELL ERR: NO ACTIVE BUY ORDER')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        time.sleep(60)  