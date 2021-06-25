from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

aggregate_trades_list = request_client.get_aggregate_trades_list(symbol="btcusd_200925", fromId=None, 
												startTime=None, endTime=None, limit=10)

print("======= Compressed/Aggregate Trades List =======")
PrintMix.print_data(aggregate_trades_list)
print("================================================")
