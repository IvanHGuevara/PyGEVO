from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_order_book(symbol = "btcusd_200925", limit = 10)
print("======= Order Book =======")
print("lastUpdateId: ", result.lastUpdateId)
print("=== Bids ===")
PrintMix.print_data(result.bids)
print("===================")
print("=== Asks ===")
PrintMix.print_data(result.asks)
print("===================")
print("====================================")
