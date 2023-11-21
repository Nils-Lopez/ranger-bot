from uniswap import Uniswap
from dotenv import load_dotenv
import os
import time

# Load environment variables from the .env file
load_dotenv()

address = os.environ['ADDRESS']          # or None if you're not going to make transactions
private_key = os.environ['WALLET']     # or None if you're not going to make transactions
version = 3                       # specify which version of Uniswap to use
provider = os.environ['PROVIDER']       # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
aimbot = "0x00000"

in_position = 0

amount_per_trade = 250 * 10**18

while True:
    # Get the current price of ETH in DAI
    current_price = uniswap.get_price_output(aimbot, dai, 1_000 * 10**18)
    if current_price >= 9.9:
        if in_position != 0:
            uniswap.make_trade(aimbot, dai, in_position)  # sell all aimbots
            in_position = 0
    elif current_price <= 7.9:
        if in_position != 0:
            uniswap.make_trade_output(aimbot, dai, amount_per_trade/2)  # buy AIMBOT for half the amount
            in_position += amount_per_trade/2
        else: 
            uniswap.make_trade_output(aimbot, dai, amount_per_trade) # buy AIMBOT for the amount
            in_position = amount_per_trade
    print(current_price)
    time.sleep(5)
