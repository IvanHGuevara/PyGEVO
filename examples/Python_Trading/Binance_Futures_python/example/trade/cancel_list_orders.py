from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
#result = request_client.cancel_list_orders(symbol="ETHUSDT", orderIdList = [459158679, 459159436, 10])
result = request_client.cancel_list_orders(symbol="BTCUSDT", origClientOrderIdList = ["web_BL7xhx6cz2lDbVlbLCbQ", "web_tW94LJCxDRUSrXN19myG", "abc"])
PrintList.print_object_list(result)
