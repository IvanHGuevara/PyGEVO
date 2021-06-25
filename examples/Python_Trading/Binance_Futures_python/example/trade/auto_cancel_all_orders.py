from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.auto_cancel_all_orders(symbol="BTCUSDT", countdownTime=5000)
PrintBasic.print_obj(result)
