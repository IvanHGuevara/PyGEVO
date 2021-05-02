from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_exchange_information()
print("======= Exchange Information =======")
print("timezone: ", result.timezone)
print("serverTime: ", result.serverTime)
print("=== Rate Limits ===")
PrintMix.print_data(result.rateLimits)
print("===================")
print("=== Exchange Filters ===")
PrintMix.print_data(result.exchangeFilters)
print("===================")
print("=== Symbols ===")
PrintMix.print_data(result.symbols)
print("===================")
print("====================================")
