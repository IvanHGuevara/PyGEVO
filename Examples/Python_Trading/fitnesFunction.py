from math import sin,cos,log,tan,factorial,pi,fabs
import pandas as pd
import ta
def smallerThan(a,b):
    return a<b
def greaterThan(a,b):
    return a>b

def fitnesFunction(phenotype,df):
    presupuesto=100
    ganancia=0
    precioPosicion=0
    buy=False
    sell=False
    for index, r in df[1:].iterrows():
        logicTrading=eval(phenotype)
        if logicTrading[0] and not buy:
            if precioPosicion == 0:
                precioPosicion = r['Close']
            else:
                #cierra sell
                porcentaje=(precioPosicion - r['Close'])/precioPosicion
                ganancia = ganancia + (presupuesto+ganancia)*porcentaje
                #pone posicion
                precioPosicion = r['Close']
            buy=True
            sell=False
        if logicTrading[1] and not sell:
            if precioPosicion == 0:
                precioPosicion = r['Close']
            else:
                #cierra buy
                porcentaje = ((r['Close'])-precioPosicion) / precioPosicion
                ganancia=ganancia+(presupuesto+ganancia)*porcentaje
                #pone posicion
                precioPosicion = r['Close']
            sell=True
            buy=False
        if (presupuesto-ganancia)<0 or (logicTrading[0] and logicTrading[1]):
            return 0
    return ganancia

#carpeta = "data"
#file='Binance_BTCUSDT_1m_1609459200000-1649548800000.csv'
#df = pd.read_csv(carpeta + '//'+file)
#df.head()
#
#columns = ["Open", "High", "Low", "Close", "Volume"]
#data = df.loc[:, columns]
#data =data.apply(pd.to_numeric, errors='coerce')
#df = ta.utils.dropna(data)
#print(df.columns)

# Add all ta features filling nans values
#df = ta.add_all_ta_features(
#    df, "Open", "High", "Low", "Close", "Volume", fillna=True
#)
#df.head()
#print(df)
#print(df.columns)
#print(len(df.columns))
#['Open', 'High', 'Low', 'Close', 'Volume', 'volume_adi', 'volume_obv',
#       'volume_cmf', 'volume_fi', 'volume_mfi', 'volume_em', 'volume_sma_em',
#       'volume_vpt', 'volume_nvi', 'volume_vwap', 'volatility_atr',
#       'volatility_bbm', 'volatility_bbh', 'volatility_bbl', 'volatility_bbw',
#       'volatility_bbp', 'volatility_bbhi', 'volatility_bbli',
#       'volatility_kcc', 'volatility_kch', 'volatility_kcl', 'volatility_kcw',
#       'volatility_kcp', 'volatility_kchi', 'volatility_kcli',
#       'volatility_dcl', 'volatility_dch', 'volatility_dcm', 'volatility_dcw',
#       'volatility_dcp', 'volatility_ui', 'trend_macd', 'trend_macd_signal',
#       'trend_macd_diff', 'trend_sma_fast', 'trend_sma_slow', 'trend_ema_fast',
#       'trend_ema_slow', 'trend_adx', 'trend_adx_pos', 'trend_adx_neg',
#       'trend_vortex_ind_pos', 'trend_vortex_ind_neg', 'trend_vortex_ind_diff',
#       'trend_trix', 'trend_mass_index', 'trend_cci', 'trend_dpo', 'trend_kst',
#       'trend_kst_sig', 'trend_kst_diff', 'trend_ichimoku_conv',
#       'trend_ichimoku_base', 'trend_ichimoku_a', 'trend_ichimoku_b',
#       'trend_visual_ichimoku_a', 'trend_visual_ichimoku_b', 'trend_aroon_up',
#       'trend_aroon_down', 'trend_aroon_ind', 'trend_psar_up',
#       'trend_psar_down', 'trend_psar_up_indicator',
#       'trend_psar_down_indicator', 'trend_stc', 'momentum_rsi',
#      'momentum_stoch_rsi', 'momentum_stoch_rsi_k', 'momentum_stoch_rsi_d',
#      'momentum_tsi', 'momentum_uo', 'momentum_stoch',
#      'momentum_stoch_signal', 'momentum_wr', 'momentum_ao', 'momentum_kama',
#      'momentum_roc', 'momentum_ppo', 'momentum_ppo_signal',
#      'momentum_ppo_hist', 'others_dr', 'others_dlr', 'others_cr']

#(<numberTipeGrafic>,<buyCondition>,<sellCondition>)
#phenotype="(1,r['volume_adi']>r['Volume'],r['volume_adi']<r['Volume'])"

#print(fitnesFunction(phenotype,df))