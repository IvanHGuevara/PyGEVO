from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# result = request_client.get_liquidation_orders()
result = request_client.get_global_long_short_accounts(symbol="BTCUSDT", period='1d')

print("======= Get Global Long Short Accounts Ratio =======")
PrintMix.print_data(result)
print("==========================================")
