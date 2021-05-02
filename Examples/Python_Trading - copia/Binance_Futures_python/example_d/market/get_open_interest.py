from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_open_interest(symbol="btcusd_200925")

print("======= Open Interest =======")
PrintBasic.print_obj(result)
print("==========================")
