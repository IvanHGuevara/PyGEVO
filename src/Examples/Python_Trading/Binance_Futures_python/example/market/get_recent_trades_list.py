from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_recent_trades_list(symbol="BTCUSDT", limit=10)

print("======= Recent Trades List =======")
PrintMix.print_data(result)
print("==================================")
