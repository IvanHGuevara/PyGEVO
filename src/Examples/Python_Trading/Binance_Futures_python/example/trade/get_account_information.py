from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_account_information()
print("canDeposit: ", result.canDeposit)
print("canWithdraw: ", result.canWithdraw)
print("feeTier: ", result.feeTier)
print("maxWithdrawAmount: ", result.maxWithdrawAmount)
print("totalInitialMargin: ", result.totalInitialMargin)
print("totalMaintMargin: ", result.totalMaintMargin)
print("totalMarginBalance: ", result.totalMarginBalance)
print("totalOpenOrderInitialMargin: ", result.totalOpenOrderInitialMargin)
print("totalPositionInitialMargin: ", result.totalPositionInitialMargin)
print("totalUnrealizedProfit: ", result.totalUnrealizedProfit)
print("totalWalletBalance: ", result.totalWalletBalance)
print("updateTime: ", result.updateTime)
print("=== Assets ===")
PrintMix.print_data(result.assets)
print("==============")
print("=== Positions ===")
PrintMix.print_data(result.positions)
print("==============")