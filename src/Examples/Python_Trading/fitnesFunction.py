from math import sin,cos,log,tan,factorial,pi,fabs
import pandas as pd
import ta
import os
from examples.Python_Trading.historicalCripto import HistoricalCripto
def smallerThan(a,b):
    return a<b
def greaterThan(a,b):
    return a>b



def fitnesFunction(phenotype,df,debug=False):
    #logicTrading =(<leverage>,<buyCondition>,<sellCondition>)
    contadorOperaciones=0
    comision=0.01/100
    presupuesto=100
    presupuestoOriginal=presupuesto
    precioPosicion=0
    buy=False
    sell=False

    r_ant=df.iloc[1]
    for index, r in df[2:].iterrows():
        logicTrading=eval(phenotype)
        leverage=logicTrading[0]
        buyCondition=logicTrading[1]
        sellCondition=logicTrading[2]

        #Liquidation Buy
        if buy and precioPosicion!=0:
            comi = (presupuesto * leverage * comision * 1)
            gan = (r['Low'] * (presupuesto * leverage) / precioPosicion) - (presupuesto * leverage)
            presupuesto_low = presupuesto + gan - comi
            if presupuesto_low <= 0:
                if debug:
                    print(str(contadorOperaciones) +" Presupuesto_low:" + str(
                        presupuesto_low) + " -> Liquidated in Close:" + str(r['Close'])+" Low:" + str(r['Low']))

                return presupuesto_low
        # Liquidation Sell
        if sell and precioPosicion!=0:
            comi = (presupuesto * leverage * comision * 1)
            gan =  (presupuesto * leverage) -(r['High'] * (presupuesto * leverage) / precioPosicion)
            presupuesto_high = presupuesto + gan - comi
            if presupuesto_high <= 0:
                if debug:
                    print(str(contadorOperaciones) + " Presupuesto_high:" + str(
                        presupuesto_high) + " -> Liquidated in Close:" + str(r['Close'])+" High:" + str(r['High']))

                return presupuesto_high
        #Buy
        if buyCondition and not buy and not sellCondition:
            # Close Sell
            if precioPosicion > 0:
                comi=(presupuesto * leverage * comision*1)
                gan=(presupuesto * leverage) -(r['Close']*(presupuesto * leverage)/precioPosicion)
                presupuesto=presupuesto + gan  - comi
            #Open Buy
            comi = (presupuesto * leverage * comision * 1)
            presupuesto=presupuesto- comi
            precioPosicion = r['Close']
            contadorOperaciones = contadorOperaciones + 1
            buy = True
            sell = False
            if debug:
                print(str(contadorOperaciones)+" -> % Presupuesto:"+str(presupuesto)+" -> BUY in "+str(r['Close'])+" x"+str(leverage))
            continue
        #Sell
        if sellCondition and not sell and not buyCondition:
            #Close buy
            if precioPosicion > 0:
                comi=(presupuesto * leverage * comision*1)
                gan=(r['Close']*(presupuesto * leverage)/precioPosicion) - (presupuesto * leverage)
                presupuesto=presupuesto + gan  - comi
            #Open Sell
            comi = (presupuesto * leverage * comision * 1)
            presupuesto=presupuesto- comi
            precioPosicion = r['Close']
            contadorOperaciones = contadorOperaciones + 1
            buy=False
            sell = True

            if debug:
                print(str(contadorOperaciones)+" -> % Presupuesto:"+str(presupuesto)+" -> SELL in "+str(r['Close'])+" x"+str(leverage))
            continue

    return presupuesto



def fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=3,init="1 Jan, 2021",end="10 Jan, 2021",typeMarket="spot",phenotype="((greaterThan(r['volatility_bbli'],r['others_cr']) or (smallerThan(r['volume_obv'],r['volatility_atr']) or (greaterThan(r['trend_psar_down_indicator'],r['volatility_bbhi']) and smallerThan(r['trend_visual_ichimoku_b'],r['volume_adi'])))),(smallerThan(r['momentum_stoch_rsi_d'],r['volatility_ui']) and greaterThan(r['volume_fi'],r['trend_ichimoku_base'])),20)"):
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
    fileName = hC.getData((symbol, graficTypeNum,init,end),fileName=None,typeMarket=typeMarket)

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