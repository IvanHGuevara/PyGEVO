from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.auto_cancel_all_orders(symbol="BTCUSD_PERP", countdownTime=5000)
PrintBasic.print_obj(result)
