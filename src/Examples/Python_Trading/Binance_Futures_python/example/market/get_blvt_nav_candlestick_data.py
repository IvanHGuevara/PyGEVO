from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_blvt_nav_candlestick_data(symbol="BTCUP", interval=CandlestickInterval.MIN1, 
												startTime=None, endTime=None, limit=10)

print("======= BLVT NAV Kline/Candlestick Data =======")
PrintMix.print_data(result)
print("======================================")
