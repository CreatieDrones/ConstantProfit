# ConstantProfit
ConstantProfit is a python script that uses the CCXT library and Phemex API with experimental logic( using USDT and NEAR)

# NOTE:
this is a personal project and so any variables are subject to change(prices, etc.)
I recommend modifying this to fit your needs and standards, as this is my first algorithm for trading

# SETUP-DIRECTIONS:
1. prepare a venv environment with the main.py code in this repo.
2. install the ccxt library so we have access to the phemex API easier(this can be done with pip install ccxt)
3. Make a Phemex account if you haven't already
4. I recommend depositing or buying 5 USDT through Phemex
5. Create a new Phemex API key, DON'T chose the API key type that requires an IP address to be listed
6. replace the api key and secret with your Phemex api details
   - The buy prices have been set to 1.50 USDT for testing purposes, but if you want to use greater amounts change those 
      variables as you chose. If you decide to change the buy price amounts, I recommend setting it to something like
       half of your USDT you deposited just to manage risk a bit easier
7. Run the python code and monitor your profit and loss, and make any logic changes you need

# Additional Info
  you may donate to fund anything I need for learning purposes at the USDT TRC20 address: TKB2Lb2Mrb5CLcUGzE4ds9z9M7CtVhghAd
  Phemex website: https://phemex.com
  API section URL: https://phemex.com/account/api-management
