from math import sin,cos,log,tan,factorial,pi,fabs
import pandas as pd
import ta
import os
from Examples.Python_Trading.historicalCripto import HistoricalCripto
def smallerThan(a,b):
    return a<b
def greaterThan(a,b):
    return a>b



def fitnesFunction(phenotype,df,debug=False):
    #logicTrading =(<buyCondition>,<sellCondition>,<leverage>)
    contadorOperaciones=0
    comision=0.01
    presupuesto=100
    ganancia=0
    pico_ganancia=0

    precioPosicion=0
    buy=False
    sell=False
    for index, r in df[1:].iterrows():

        logicTrading=eval(phenotype)
        if (logicTrading[0] and logicTrading[1]):
            if debug:
                print(str("-")+" -> % GAIN:"+str(ganancia) + " -> Indesicion in " + str(r['Close']))
            continue

        #Liquidation
        if buy:
            porcentaje = ((precioPosicion - r['High']) / precioPosicion) * (1 - comision)
            pico_ganancia = ganancia + (presupuesto + pico_ganancia) * porcentaje * logicTrading[2]

            #print(["BUY",buy,r['High'],pico_ganancia])
        if sell:
            porcentaje = (((r['Low']) - precioPosicion) / precioPosicion) * (1 - comision)
            pico_ganancia = ganancia + (presupuesto + pico_ganancia) * porcentaje * logicTrading[2]

            #print(["SELL",sell,r['Low'],pico_ganancia])
        if (buy and (pico_ganancia+presupuesto)<0) or (sell and (pico_ganancia+presupuesto)<0) :
            if debug:
                print(str(contadorOperaciones)+" -> Liquidated in "+str(r['Close']))
            return 0

        if logicTrading[0] and not buy:
            if precioPosicion == 0:
                precioPosicion = r['Close']
            else:
                #cierra sell
                porcentaje=((precioPosicion - r['Close'])/precioPosicion)*(1-comision)
                ganancia = ganancia + ((presupuesto+ganancia)*porcentaje)*logicTrading[2]

                #pone posicion
                precioPosicion = r['Close']
            buy=True
            sell=False
            contadorOperaciones=contadorOperaciones+1
            if debug:
                print(str(contadorOperaciones)+" -> % GAIN:"+str(ganancia)+" -> BUY in "+str(r['Close'])+" x"+str(logicTrading[2]))
        if logicTrading[1] and not sell:
            if precioPosicion == 0:
                precioPosicion = r['Close']
            else:
                #cierra buy
                porcentaje = (((r['Close'])-precioPosicion) / precioPosicion)*(1-comision)
                ganancia=ganancia+(presupuesto+ganancia)*porcentaje*logicTrading[2]

                #pone posicion
                precioPosicion = r['Close']
            sell=True
            buy=False
            contadorOperaciones = contadorOperaciones + 1
            if debug:
                print(str(contadorOperaciones)+" -> % GAIN:"+str(ganancia)+" -> SELL in "+str(r['Close'])+" x"+str(logicTrading[2]))


    #print("CantidadOperaciones:"+str(contadorOperaciones)+" ->",end="")
    return ganancia



def fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=3,init="1 Jan, 2021",end="10 Jan, 2021",phenotype="((greaterThan(r['volatility_bbli'],r['others_cr']) or (smallerThan(r['volume_obv'],r['volatility_atr']) or (greaterThan(r['trend_psar_down_indicator'],r['volatility_bbhi']) and smallerThan(r['trend_visual_ichimoku_b'],r['volume_adi'])))),(smallerThan(r['momentum_stoch_rsi_d'],r['volatility_ui']) and greaterThan(r['volume_fi'],r['trend_ichimoku_base'])),20)"):
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
    carpeta="data"
    hC = HistoricalCripto()
    # hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))
    fileName = hC.getData((symbol, graficTypeNum,init,end))

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
    print( file + '_Indicators' + ".csv")
    data = pd.read_csv(carpeta + "//" + file + '_Indicators' + ".csv")
    #phenotype="(1,r['volume_adi']>r['Volume'],r['volume_adi']<r['Volume'])"

    print(fitnesFunction(phenotype,data,debug=True))