from binance_d import RequestClient
from binance_d.model import *
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_continuous_candlestick_data(pair="btcusd", contractType="CURRENT_QUARTER", interval=CandlestickInterval.MIN1, 
												startTime=None, endTime=None, limit=10)

print("======= Kline/Candlestick Data =======")
PrintMix.print_data(result)
print("======================================")
