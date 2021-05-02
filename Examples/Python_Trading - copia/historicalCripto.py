import time
import dateparser
import pytz
import json
import csv
import os
from datetime import datetime
from binance.client import Client
import ta
import pandas as pd
import warnings
import numpy as np
class HistoricalCripto:
    def __init__(self,data="data") -> None:
        self.defaultSymbol="BTCUSDT"
        self.data=data
    def date_to_milliseconds(self,date_str):
        """Convert UTC date to milliseconds

        If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

        See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/

        :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
        :type date_str: str
        """
        # get epoch value in UTC
        epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
        # parse our date string
        d = dateparser.parse(date_str)
        # if the date is not timezone aware apply UTC timezone
        if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
            d = d.replace(tzinfo=pytz.utc)

        # return the difference in time
        return int((d - epoch).total_seconds() * 1000.0)


    def interval_to_milliseconds(self,interval):
        """Convert a Binance interval string to milliseconds

        :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
        :type interval: str

        :return:
             None if unit not one of m, h, d or w
             None if string not in correct format
             int value of interval in milliseconds
        """
        ms = None
        seconds_per_unit = {
            "m": 60,
            "h": 60 * 60,
            "d": 24 * 60 * 60,
            "w": 7 * 24 * 60 * 60
        }

        unit = interval[-1]
        if unit in seconds_per_unit:
            try:
                ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
            except ValueError:
                pass
        return ms


    def get_historical_klines(self,symbol, interval, start_str, end_str=None,typeMarket="spot"):
        """Get Historical Klines from Binance

        See dateparse docs for valid start and end string formats http://dateparser.readthedocs.io/en/latest/

        If using offset strings for dates add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

        :param symbol: Name of symbol pair e.g BNBBTC
        :type symbol: str
        :param interval: Biannce Kline interval
        :type interval: str
        :param start_str: Start date string in UTC format
        :type start_str: str
        :param end_str: optional - end date string in UTC format
        :type end_str: str

        :return: list of OHLCV values

        """
        # create the Binance client, no need for api key
        client = Client("", "")
        #client.FUTURES_URL = 'https://dapi.binance.com/dapi'
        #client.FUTURES_URL = "https://fapi.binance.com"
        # init our list
        output_data = []

        # setup the max limit
        limit = 500

        # convert interval to useful value in seconds
        timeframe = self.interval_to_milliseconds(interval)

        # convert our date strings to milliseconds
        start_ts = self.date_to_milliseconds(start_str)

        # if an end time was passed convert it
        end_ts = None
        if end_str:
            end_ts = self.date_to_milliseconds(end_str)

        idx = 0
        # it can be difficult to know when a symbol was listed on Binance so allow start time to be before list date
        symbol_existed = False
        while True:
            # fetch the klines from start_ts up to max 500 entries or the end_ts if set
            if typeMarket=="future":
                #future
                temp_data = client.futures_klines(
                    symbol=symbol,
                    interval=interval,
                    limit=limit,
                    startTime=start_ts,
                    endTime=end_ts
                )
            elif typeMarket=="spot":
                #spot
                temp_data = client.get_klines(
                    symbol=symbol,
                    interval=interval,
                    limit=limit,
                    startTime=start_ts,
                    endTime=end_ts
                )

            # handle the case where our start date is before the symbol pair listed on Binance
            if not symbol_existed and len(temp_data):
                symbol_existed = True

            if symbol_existed:
                # append this loops data to our output data
                output_data += temp_data

                # update our start timestamp using the last value in the array and add the interval timeframe
                start_ts = temp_data[len(temp_data) - 1][0] + timeframe
            else:
                # it wasn't listed yet, increment our start date
                start_ts += timeframe

            idx += 1
            # check if we received less than the required limit and exit the loop
            if len(temp_data) < limit:
                # exit the while loop
                break

            # sleep after every 3rd call to be kind to the API
            if idx % 3 == 0:
                time.sleep(1)

        return output_data

    def getData(self,operation=None,fileName=None,typeMarket="spot"):
        os.makedirs(self.data, exist_ok=True)
        #operation is a tuple ("BTCUSDT",2,"1 Jan, 2021","10 Apr, 2022")
        if operation is None:
            symbol = input("Bitcoin a historizar [Por def. BTCUSDT]: ")

            if symbol == "" :
                symbol = self.defaultSymbol
                print("Symbolo por defecto: "+symbol)
            else :
                print("Symbolo elegido: "+symbol)

            print("---")
            start = input("Fecha inicio [Ej. 1 Jan, 2021]: ")
            print("---")
            end = input("Fecha fin [Ej. 10 Apr, 2022]: ")

            print("Ingrese opcion de periodo de mediciones:")
            print("1-> 1m")
            print("2-> 3m")
            print("3-> 5m")
            print("4-> 30m")
            print("5-> 1h")
            print("6-> 2h")
            print("7-> 4h")
            print("8-> 6h")
            print("9-> 8h")
            print("10-> 12h")
            print("11-> 1d")
            print("12-> 3d")
            print("13-> 1sem")
            print("14-> 1mes")
            opc_per = int(input("Opcion: "))

            print("---")
        else:

            symbol=operation[0]
            opc_per=operation[1]
            start=operation[2]
            end=operation[3]

        switcher = {
            1: Client.KLINE_INTERVAL_1MINUTE,
            2: Client.KLINE_INTERVAL_3MINUTE,
            3: Client.KLINE_INTERVAL_5MINUTE,
            4: Client.KLINE_INTERVAL_15MINUTE,
            5: Client.KLINE_INTERVAL_30MINUTE,
            6: Client.KLINE_INTERVAL_1HOUR,
            7: Client.KLINE_INTERVAL_2HOUR,
            8: Client.KLINE_INTERVAL_4HOUR,
            9: Client.KLINE_INTERVAL_6HOUR,
            10: Client.KLINE_INTERVAL_8HOUR,
            11: Client.KLINE_INTERVAL_12HOUR,
            12: Client.KLINE_INTERVAL_1DAY,
            13: Client.KLINE_INTERVAL_3DAY,
            14: Client.KLINE_INTERVAL_1WEEK,
            15: Client.KLINE_INTERVAL_1MONTH
        }

        interval = switcher.get(opc_per, Client.KLINE_INTERVAL_1MINUTE)
        if fileName is None:
            fileName = "Binance_{}_{}_{}_{}-{}.csv".format(symbol,
                                                        interval,typeMarket,
                                                        start.replace(" ","_").replace(",",""),
                                                        end.replace(" ","_").replace(",",""))
                                                        #self.date_to_milliseconds(start),
                                                        #self.date_to_milliseconds(end))

        if not os.path.isfile(self.data + "//"  + fileName):
            klines = self.get_historical_klines(symbol, interval, start, end,typeMarket=typeMarket)

            # open a file with filename including symbol, interval and start and end converted to milliseconds


            with open(self.data+"//"+fileName,
                'w',  # set file write mode
                newline=''
            ) as f:
                # f.write(json.dumps(klines))
                writer = csv.writer(f, delimiter=',')
                writer.writerow([
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored"
                    ])
                writer.writerows(klines)

            #print("Terminado.-")
        return fileName


    def getData_v2(self,operation=None,fileName=None,typeMarket="spot"):
        os.makedirs(self.data, exist_ok=True)
        #operation is a tuple ("BTCUSDT",2,"1 Jan, 2021","10 Apr, 2022")
        if operation is None:
            symbol = input("Bitcoin a historizar [Por def. BTCUSDT]: ")

            if symbol == "" :
                symbol = self.defaultSymbol
                print("Symbolo por defecto: "+symbol)
            else :
                print("Symbolo elegido: "+symbol)

            print("---")
            start = input("Fecha inicio [Ej. 1 Jan, 2021]: ")
            print("---")
            end = input("Fecha fin [Ej. 10 Apr, 2022]: ")

            print("Ingrese opcion de periodo de mediciones:")
            print("1-> 1m")
            print("2-> 3m")
            print("3-> 5m")
            print("4-> 30m")
            print("5-> 1h")
            print("6-> 2h")
            print("7-> 4h")
            print("8-> 6h")
            print("9-> 8h")
            print("10-> 12h")
            print("11-> 1d")
            print("12-> 3d")
            print("13-> 1sem")
            print("14-> 1mes")
            opc_per = int(input("Opcion: "))

            print("---")
        else:

            symbol=operation[0]
            opc_per=operation[1]
            start=operation[2]
            end=operation[3]

        switcher = {
            1: Client.KLINE_INTERVAL_1MINUTE,
            2: Client.KLINE_INTERVAL_3MINUTE,
            3: Client.KLINE_INTERVAL_5MINUTE,
            4: Client.KLINE_INTERVAL_15MINUTE,
            5: Client.KLINE_INTERVAL_30MINUTE,
            6: Client.KLINE_INTERVAL_1HOUR,
            7: Client.KLINE_INTERVAL_2HOUR,
            8: Client.KLINE_INTERVAL_4HOUR,
            9: Client.KLINE_INTERVAL_6HOUR,
            10: Client.KLINE_INTERVAL_8HOUR,
            11: Client.KLINE_INTERVAL_12HOUR,
            12: Client.KLINE_INTERVAL_1DAY,
            13: Client.KLINE_INTERVAL_3DAY,
            14: Client.KLINE_INTERVAL_1WEEK,
            15: Client.KLINE_INTERVAL_1MONTH
        }

        interval = switcher.get(opc_per, Client.KLINE_INTERVAL_1MINUTE)
        if fileName is None:
            fileName = "Binance_{}_{}_{}_{}-{}.csv".format(symbol,
                                                        interval,typeMarket,
                                                        start.replace(" ","_").replace(",",""),
                                                        end.replace(" ","_").replace(",",""))
                                                        #self.date_to_milliseconds(start),
                                                        #self.date_to_milliseconds(end))

            if not os.path.isfile(self.data + "//"  + fileName):
                klines = self.get_historical_klines(symbol, interval, start, end,typeMarket=typeMarket)

                # open a file with filename including symbol, interval and start and end converted to milliseconds
                #print(klines)

                df=pd.DataFrame(np.array(klines,dtype=np.float32),
                  columns=[
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored"
                    ])

                df.head()
                # print(" Data: Close:" + str(df.iloc[-2]["Close"])+" Low:" + str(df.iloc[-2]["Low"])+" High:" + str(df.iloc[-2]["High"]))
                columns = ["Open", "High", "Low", "Close", "Volume"]
                data = df.loc[:, columns]
                data = data.apply(pd.to_numeric, errors='coerce').fillna(0)
                df1 = ta.utils.dropna(data)

                # print(df.columns)
                # Add all ta features filling nans values

                df1 = ta.add_all_ta_features(
                    df, "Open", "High", "Low", "Close", "Volume", fillna=True
                )
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    df1 = ta.add_all_ta_features(
                        df, "Open", "High", "Low", "Close", "Volume", fillna=True
                    )
                    # df.head()
                    print(df)
                    print(df.columns)
                    print(len(df.columns))
                    #df1.to_csv(self.carpeta + "//" + self.file + '_Indicators' + ".csv", sep=',')
                return fileName
#hC=HistoricalCripto()
#hC.getData(("BTCUSDT",13,"1 Jan, 2021","10 Apr, 2022"))

#hC=HistoricalCripto()
#hC.getData_v2(("BTCUSDT",6,"7 Jan, 2021","11 Apr, 2022"))