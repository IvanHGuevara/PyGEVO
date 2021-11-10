from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_old_trade_lookup(symbol="BTCUSDT", limit=10, fromId=None)

print("======= Old Trade Lookup =======")
PrintMix.print_data(result)
print("==================================")
