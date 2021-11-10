from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# result = request_client.get_liquidation_orders()
result = request_client.get_taker_buy_sell_vol(pair="BTCUSD", contractType="CURRENT_QUARTER", period='1d')

print("======= Get Taker Buy/Sell Ratio =======")
PrintMix.print_data(result)
print("==========================================")
