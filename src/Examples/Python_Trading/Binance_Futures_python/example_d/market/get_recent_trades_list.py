from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_recent_trades_list(symbol="btcusd_200925", limit=10)

print("======= Recent Trades List =======")
PrintMix.print_data(result)
print("==================================")
