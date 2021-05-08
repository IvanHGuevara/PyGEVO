import logging
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException

from binance_f.base.printobject import *

logger = logging.getLogger("binance-futures")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        print("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        print("Event type: ", event.eventType)
        print("Event time: ", event.eventTime)
        print("transaction time: ", event.transactionTime)
        print("Symbol: ", event.symbol)
        print("first update Id from last stream: ", event.firstUpdateId)
        print("last update Id from last stream: ", event.lastUpdateId)
        print("last update Id in last stream: ", event.lastUpdateIdInlastStream)
        print("=== Bids ===")
        PrintMix.print_data(event.bids)
        print("===================")
        print("=== Asks ===")
        PrintMix.print_data(event.asks)
        print("===================")
       # sub_client.unsubscribe_all()
    else:
        print("Unknown Data:")
    print()


def error(e: 'BinanceApiException'):
    print(e.error_code + e.error_message)

# Valid limit values are 5, 10, or 20 
sub_client.subscribe_book_depth_event("btcusdt", 10, callback, error, update_time=UpdateTime.FAST)
#sub_client.subscribe_book_depth_event("btcusdt", 10, callback, error, update_time=UpdateTime.NORMAL)
#sub_client.subscribe_book_depth_event("btcusdt", 10, callback, error)
