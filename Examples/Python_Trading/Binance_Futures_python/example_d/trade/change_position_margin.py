from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.change_position_margin(symbol="btcusd_200925", amount=0.01, type=1)

PrintBasic.print_obj(result)
