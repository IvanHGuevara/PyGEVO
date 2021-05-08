from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

aggregate_trades_list = request_client.get_aggregate_trades_list(symbol="BTCUSDT", fromId=None, 
												startTime=None, endTime=None, limit=10)

print("======= Compressed/Aggregate Trades List =======")
PrintMix.print_data(aggregate_trades_list)
print("================================================")
