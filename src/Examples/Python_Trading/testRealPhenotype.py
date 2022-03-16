import time
import math
import logging
import json
from binance_f import RequestClient
from binance_f.model.constant import *
#from binance_f.constant.test import *
from binance_f.base.printobject import *
#from binance_f.model.constant import *
import ta
from examples.Python_Trading.historicalCripto import HistoricalCripto
import os
import pandas as pd
from tabulate import tabulate
import warnings
from datetime import datetime
from datetime import timedelta

class TestRealPhenotype:
    def __init__(self,symbol="BTCUSDT",interval=6,phenotype=None,lapsoMinutes=5,debug=False,trading=False) -> None:
        with open('config.json') as f:
            data = json.load(f)
            self.usuarios=data["Usuarios"]
            self.id=0
        self.symbol=symbol
        self.phenotype=phenotype
        self.file="data_RealTime_1"
        self.carpeta="data"
        self.ganancia=0
        self.buy = False
        self.sell = False
        self.contadorOperaciones = 0
        self.interval=interval
        self.trading=trading
        self.precioPosicion = 0
        self.comision = 0.01
        self.presupuesto = 100
        self.lapsoMinutes=lapsoMinutes
    def alarm(self,sound="coin",n=3):
        for i in range(1,n):
            time.sleep(1)

        return 0
    def loginBinance(self,n):
        request_client = RequestClient(api_key=self.usuarios[n]["api_key"], secret_key=self.usuarios[n]["secret_key"],url="https://fapi.binance.com")

        return request_client
    def compraFuturos(self,request_client,usuario):

        result = request_client.get_balance()
        #PrintMix.print_data(result)
        usdt=0.0
        for i in result:
            if i.asset=="USDT":
                usdt = i.withdrawAvailable

        #print(str(i.asset) + "-> balance:" + str(i.balance) + " withdrawAvailable:" + str(i.withdrawAvailable))

        result = request_client.change_initial_leverage(symbol=self.symbol, leverage=int(usuario["leverage_long"]))
        #PrintBasic.print_obj(result)
        result = request_client.get_mark_price(symbol=self.symbol)
        #quantity = round(math.trunc(usdt)/result.markPrice, 3)
        tick_size = 4
        trade_quantity = usdt*int(usuario["leverage_long"])*float(usuario["porcent_use"]) / result.markPrice
        quantity = float("{:0.0{}f}".format(trade_quantity, tick_size))
        print("Compra cantidad:"+str(quantity)[0:-1])
        if quantity>0:
            result = request_client.post_order(symbol=self.symbol, side=OrderSide.BUY, ordertype=OrderType.MARKET,quantity=str(quantity)[0:-1])
            #PrintBasic.print_obj(result)
    def venderFuturos(self,request_client,usuario):

        result = request_client.get_balance()
        PrintMix.print_data(result)
        usdt=0.0
        for i in result:
            if i.asset=="USDT":
                usdt = i.withdrawAvailable

        #print(str(i.asset) + "-> balance:" + str(i.balance) + " withdrawAvailable:" + str(i.withdrawAvailable))

        result = request_client.change_initial_leverage(symbol=self.symbol, leverage=int(usuario["leverage_short"]))
        #PrintBasic.print_obj(result)
        result = request_client.get_mark_price(symbol=self.symbol)
        #quantity = round(math.trunc(usdt)/result.markPrice, 3)
        tick_size=4
        trade_quantity = usdt*int(usuario["leverage_short"])*float(usuario["porcent_use"]) / result.markPrice
        quantity=float("{:0.0{}f}".format(trade_quantity, tick_size))
        print("Vende cantidad:"+str(quantity)[0:-1])
        if quantity > 0:
            result = request_client.post_order(symbol=self.symbol, side=OrderSide.SELL, ordertype=OrderType.MARKET,quantity=str(quantity)[0:-1])
            #PrintBasic.print_obj(result)
    def compraFuturosCancelSell(self,request_client):

        result = request_client.get_position()
        for i in result:
            if i.symbol == self.symbol:
                leverage_operacion = i.leverage
                quantity = i.positionAmt*(-1)
                PrintMix.print_data(i)
        result = request_client.change_initial_leverage(symbol=self.symbol, leverage=leverage_operacion)
        #PrintBasic.print_obj(result)

        print("Cancela Venta cantidad:" + str(quantity))
        if quantity > 0:
            result = request_client.post_order(symbol=self.symbol, side=OrderSide.BUY, ordertype=OrderType.MARKET,quantity=str(quantity))
            #PrintBasic.print_obj(result)

    def venderFuturosCancelBuy(self,request_client):

        result = request_client.get_position()
        for i in result:
            if i.symbol==self.symbol:
                leverage_operacion=i.leverage
                quantity=i.positionAmt
                PrintMix.print_data(i)
        result = request_client.change_initial_leverage(symbol=self.symbol, leverage=leverage_operacion)
        #PrintBasic.print_obj(result)
        print("Cancela Compra cantidad:"+str(quantity))
        if quantity != 0:
            result = request_client.post_order(symbol=self.symbol, side=OrderSide.SELL, ordertype=OrderType.MARKET,quantity=str(quantity))
            #PrintBasic.print_obj(result)

    def fitnesFunction(self,phenotype, df, debug=False):
        request_client = self.loginBinance(self.id)
        def mostrar(df):
            print(" ")
            print("Operacion:"+str(datetime.now()))
            dfMostrar = df.copy()
            dfMostrar['Open time'] = pd.to_datetime(dfMostrar.loc[:, 'Open time'], unit="ms")
            dfMostrar['Open time'] = dfMostrar['Open time'].dt.tz_localize('UTC').dt.tz_convert(
                'America/Argentina/Catamarca')
            dfMostrar.set_index('Open time')
            df = df.set_index('Open time')
            print(tabulate(dfMostrar.iloc[-2:], tablefmt='fancy_grid', stralign='center', floatfmt='.0f',
                           headers=list(dfMostrar.columns)))
        def smallerThan(a, b):
            return a < b

        def greaterThan(a, b):
            return a > b

        # logicTrading =(<leverage>,<buyCondition>,<sellCondition>)
        r_ant = df.iloc[-3]
        r=df.iloc[-2]
        r_now = df.iloc[-1]

        logicTrading = eval(phenotype)
        leverage = logicTrading[0]
        buyCondition = logicTrading[1]
        sellCondition = logicTrading[2]

        # Liquidation Buy
        if self.buy and self.precioPosicion != 0:
            porsentaje_actual=1*r_now['Low']/self.precioPosicion
            ganancia_actual=((self.presupuesto*porsentaje_actual)-self.presupuesto)*leverage*(1+self.comision*2)
            presupuesto_actual=self.presupuesto*(1+(ganancia_actual/100))
            if presupuesto_actual <= 0:
                if debug:
                    print(str(self.contadorOperaciones) + " ganancia_actual:" + str(
                        ganancia_actual) +" presupuesto_actual:" + str(
                        presupuesto_actual) + " -> Liquidated in Close:" + str(r_now['Close'])+" Low:" + str(r_now['Low']))

                return 0
        # Liquidation Sell
        if self.sell and self.precioPosicion != 0:
            porsentaje_actual = 1 * r_now['High'] / self.precioPosicion
            ganancia_actual = -((self.presupuesto * porsentaje_actual) - self.presupuesto) * leverage * (1 + self.comision*2)
            presupuesto_actual = self.presupuesto * (1 + (ganancia_actual / 100))
            if presupuesto_actual <= 0:
                if debug:
                    print(str(self.contadorOperaciones) + " ganancia_actual:" + str(
                        ganancia_actual) + " presupuesto_actual:" + str(
                        presupuesto_actual) + " -> Liquidated in Close:" + str(r_now['Close']) + " High:" + str(r_now['High']))

                return 0
        # Buy
        if buyCondition and not self.buy and not sellCondition:
            # Close Sell
            if self.precioPosicion != 0:
                porcentaje = ((self.precioPosicion - r_now['Close']) / self.precioPosicion) * (1 - self.comision*2)
                self.ganancia = self.ganancia + ((self.presupuesto + self.ganancia) * porcentaje) * leverage

            # Open Buy
            self.precioPosicion = r_now['Close']

            self.contadorOperaciones = self.contadorOperaciones + 1
            if debug:
                mostrar(df)
                print(str(self.contadorOperaciones) + " -> % GAIN:" + str(self.ganancia) + " -> BUY in " + str(
                    r_now['Close']) + " x" + str(leverage))
            r_ant = r
            if self.trading and self.sell:
                self.compraFuturosCancelSell(request_client)
            self.buy = True
            self.sell = False
            if self.trading:
                self.compraFuturos(request_client, self.usuarios[self.id])
            self.alarm(n=2)
        # Sell
        if sellCondition and not self.sell and not buyCondition:
            # Close buy
            if self.precioPosicion != 0:
                porcentaje = (((r_now['Close']) - self.precioPosicion) / self.precioPosicion) * (1 - self.comision*2)
                self.ganancia = self.ganancia + (self.presupuesto + self.ganancia) * porcentaje * leverage

            # Open Sell
            self.precioPosicion = r_now['Close']

            self.contadorOperaciones = self.contadorOperaciones + 1
            if debug:
                mostrar(df)
                print(str(self.contadorOperaciones) + " -> % GAIN:" + str(self.ganancia) + " -> SELL in " + str(
                    r_now['Close']) + " x" + str(leverage))
            r_ant = r
            if self.trading and self.buy:
                self.venderFuturosCancelBuy(request_client)
            self.sell = True
            self.buy = False
            if self.trading:
                self.venderFuturos(request_client, self.usuarios[self.id])
            self.alarm(n=1)


        return self.ganancia

    def fitnesFunction_futuro(self, graficTypeNum=6, init="1 Jan, 2021", end=None,phenotype=None):
        # extraction Data

        # 1: Client.KLINE_INTERVAL_1MINUTE,
        # 2: Client.KLINE_INTERVAL_3MINUTE,
        # 3: Client.KLINE_INTERVAL_5MINUTE,
        # 4: Client.KLINE_INTERVAL_15MINUTE,
        # 5: Client.KLINE_INTERVAL_30MINUTE,
        # 6: Client.KLINE_INTERVAL_1HOUR,
        # 7: Client.KLINE_INTERVAL_2HOUR,
        # 8: Client.KLINE_INTERVAL_4HOUR,
        # 9: Client.KLINE_INTERVAL_6HOUR,
        # 10: Client.KLINE_INTERVAL_8HOUR,
        # 11: Client.KLINE_INTERVAL_12HOUR,
        # 12: Client.KLINE_INTERVAL_1DAY,
        # 13: Client.KLINE_INTERVAL_3DAY,
        # 14: Client.KLINE_INTERVAL_1WEEK,
        # 15: Client.KLINE_INTERVAL_1MONTH
        # for i in [1,2,3,4,5,7]:
        # 6,3,1
        carpeta = "data_RealTime"
        hC = HistoricalCripto(data=carpeta)
        # hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))
        fileName = hC.getData((self.symbol, graficTypeNum, init, end))

        file = fileName[:-4]
        if not os.path.isfile(carpeta + "//" + file + '_Indicators' + ".csv"):
            df = pd.read_csv(carpeta + '//' + file + ".csv")
            df.head()

            columns = ["Open", "High", "Low", "Close", "Volume"]
            data = df.loc[:, columns]
            data = data.apply(pd.to_numeric, errors='coerce')
            df = ta.utils.dropna(data)
            # print(df.columns)
            # Add all ta features filling nans values
            df = ta.add_all_ta_features(
                df, "Open", "High", "Low", "Close", "Volume", fillna=True
            )
            # df.head()
            # print(df)
            # print(df.columns)
            # print(len(df.columns))
            df.to_csv(carpeta + "//" + file + '_Indicators' + ".csv", sep=',')
        print(file + '_Indicators' + ".csv")
        data = pd.read_csv(carpeta + "//" + file + '_Indicators' + ".csv")
        # phenotype="(1,r['volume_adi']>r['Volume'],r['volume_adi']<r['Volume'])"

        #print(fitnesFunction(phenotype, data, debug=True))

    def operar(self):

        print("---------------------------------------------------------------------------------------------------------")
        print(self.phenotype)
        print("Fecha inicio: " + str(datetime.now().replace(  microsecond=0)))

        dt=datetime.now()
        mins=int(dt.minute/self.lapsoMinutes)*self.lapsoMinutes


        dt_new = datetime.now().replace( minute=mins,second=0, microsecond=0)
        if mins == dt.minute:
            dt_sig=datetime.now().replace(minute=mins, second=0, microsecond=0)
        else:
            dt_sig =dt_new + timedelta(minutes=self.lapsoMinutes)
        imprCantidadRegistrosAnalizados=True
        time.sleep(1)
        while True:

            if dt_sig == dt_new:

                #print("-------------------------------------------------------------------------------------------------")
                #print("Fecha operacion: "+str(dt_new)+" -> " ,end="")
                if os.path.isfile(self.carpeta + "//" + self.file + ".csv"):
                    os.remove(self.carpeta + "//" + self.file +".csv")
                if os.path.isfile(self.carpeta + "//" + self.file+ '_Indicators'  + ".csv"):
                    os.remove(self.carpeta + "//" + self.file+ '_Indicators' +".csv")
                hC = HistoricalCripto()
                # hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))

                now = datetime.now()

                f_init = (now - timedelta(days=1)).strftime('%d %b, %Y')
                f_end = (now + timedelta(days=1)).strftime('%d %b, %Y')
                #print("Data Now:" + f_now + " Init:" + f_init + " End:" + f_end,end="")

                cargoDatos=False
                while not cargoDatos:
                    try:
                        fileName = hC.getData((self.symbol, self.interval, f_init, f_end),self.file+".csv",typeMarket="future")
                        cargoDatos=True
                        print(".", end="")
                        time.sleep(1)
                    except:
                        cargoDatos=False
                        print("-",end="")
                        self.alarm(sound="robot_error",n=2)
                self.file = fileName[:-4]


                df = pd.read_csv(self.carpeta + '//' + self.file + ".csv")
                df.head()

                #print(" Data: Close:" + str(df.iloc[-2]["Close"])+" Low:" + str(df.iloc[-2]["Low"])+" High:" + str(df.iloc[-2]["High"]))
                columns = ["Open", "High", "Low", "Close", "Volume"]
                data = df.loc[:, columns]#.iloc[-200:]
                if imprCantidadRegistrosAnalizados:
                    print("")
                    print("Cantidad de registros descargados en cada operacion:" + str(len(df)))
                    print("Cantidad de registros a analizar en cada operacion:"+str(len(data)))
                    imprCantidadRegistrosAnalizados=False
                data = data.apply(pd.to_numeric, errors='coerce')
                df1 = ta.utils.dropna(data)
                # print(df.columns)
                # Add all ta features filling nans values
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    df1 = ta.add_all_ta_features(
                        df, "Open", "High", "Low", "Close", "Volume", fillna=True
                    )
                # df.head()
                # print(df)
                # print(df.columns)
                # print(len(df.columns))
                df1.to_csv(self.carpeta + "//" + self.file + '_Indicators' + ".csv", sep=',')


                gain=self.fitnesFunction(self.phenotype, df.iloc[-3:], debug=True)
                if gain<-100:
                    return 0
                dt_sig =datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=self.lapsoMinutes)
            else:
                time.sleep(0.5)
                dt_new = datetime.now().replace(second=0, microsecond=0)


        # 1: Client.KLINE_INTERVAL_1MINUTE,
        # 2: Client.KLINE_INTERVAL_3MINUTE,
        # 3: Client.KLINE_INTERVAL_5MINUTE,
        # 4: Client.KLINE_INTERVAL_15MINUTE,
        # 5: Client.KLINE_INTERVAL_30MINUTE,
        # 6: Client.KLINE_INTERVAL_1HOUR,
        # 7: Client.KLINE_INTERVAL_2HOUR,
        # 8: Client.KLINE_INTERVAL_4HOUR,
        # 9: Client.KLINE_INTERVAL_6HOUR,
        # 10: Client.KLINE_INTERVAL_8HOUR,
        # 11: Client.KLINE_INTERVAL_12HOUR,
        # 12: Client.KLINE_INTERVAL_1DAY,
        # 13: Client.KLINE_INTERVAL_3DAY,
        # 14: Client.KLINE_INTERVAL_1WEEK,
        # 15: Client.KLINE_INTERVAL_1MONTH



phenotype="(3,smallerThan(r['volume_em'],r['volume_sma_em']),(greaterThan(r['trend_aroon_down'],r['momentum_ppo']) and (greaterThan(r['volatility_kch'],r['volatility_dch']) or (smallerThan(r_ant['volume_adi'],r['volume_em']) and (greaterThan(r['trend_kst'],r['momentum_tsi']) or greaterThan(r['Low'],r_ant['trend_psar_down']))))))"
trp=TestRealPhenotype("BTCUSDT",interval=1,phenotype=phenotype,lapsoMinutes=1,trading=False)

trp.operar()
