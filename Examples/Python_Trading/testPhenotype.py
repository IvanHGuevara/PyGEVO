import Examples.Python_Trading.fitnesFunction as ff
#1min
print("Grafico de 1m Futuros")

p="(5,smallerThan(r['trend_aroon_up'],r['trend_adx']),greaterThan(r['volume_cmf'],r['volatility_kchi']))"
#107005317
p="(5,smallerThan(r['trend_aroon_up'],r['trend_adx']),(greaterThan(r['volume_em'],r_ant['trend_macd_diff']) and (greaterThan(r['trend_aroon_down'],r['trend_cci']) or (smallerThan(r['volatility_bbw'],r['others_cr']) and smallerThan(r['trend_cci'],r['trend_dpo'])))))"
#236413376
p="(5,smallerThan(r['trend_aroon_up'],r['trend_mass_index']),(greaterThan(r['volume_em'],r['volatility_dcw']) and (greaterThan(r['trend_aroon_down'],r['trend_cci']) or (smallerThan(r['volatility_bbw'],r['others_cr']) and smallerThan(r['trend_cci'],r['trend_macd_signal'])))))"
#1932057861
p="(5,smallerThan(r['trend_aroon_up'],r['trend_mass_index']),(greaterThan(r['volume_em'],r_ant['trend_vortex_ind_diff']) and (greaterThan(r['trend_aroon_down'],r['trend_cci']) or (greaterThan(r_ant['momentum_stoch_signal'],r['volatility_bbp']) and smallerThan(r['trend_cci'],r['trend_dpo'])))))"
#123670227  5x
p="(5,(greaterThan(r['volume_adi'],r['volume_em']) or (greaterThan(r_ant['momentum_ao'],r['volatility_dch']) and (greaterThan(r['trend_ichimoku_conv'],r['trend_visual_ichimoku_a']) and (smallerThan(r['trend_psar_down'],r['volume_obv']) and smallerThan(r['momentum_stoch_signal'],r['trend_ichimoku_a']))))),greaterThan(r['volume_em'],r_ant['volatility_kcli']))"


#ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=1,init="1 Mar, 2021",end="26 Apr, 2021",typeMarket="future",phenotype=p)

#3 mins
print("3 mins")
p="(5,greaterThan(r['volatility_ui'],r['momentum_stoch_rsi_d']),greaterThan(r['volume_fi'],r_ant['momentum_ao']))"
#ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=2,init="1 Mar, 2021",end="26 Apr, 2021",typeMarket="future",phenotype=p)
#5 mins
print("Grafico de 5m Futuros")
#223228
p="(5,smallerThan(r['momentum_roc'],r['momentum_ppo_hist']),(greaterThan(r['volume_obv'],r_ant['momentum_wr']) and smallerThan(r_ant['trend_vortex_ind_neg'],r['volume_fi'])))"
p="(5,smallerThan(r['volume_em'],r['volume_sma_em']),(greaterThan(r['volume_adi'],r['trend_vortex_ind_diff']) and (greaterThan(r_ant['volatility_dcm'],r['volatility_dch']) or (smallerThan(r['volume_adi'],r['volume_em']) and (greaterThan(r['trend_kst'],r['momentum_tsi']) or greaterThan(r_ant['trend_cci'],r['trend_kst_sig']))))))"
p="(5,(smallerThan(r_ant['momentum_stoch'],r['momentum_stoch_rsi']) or smallerThan(r_ant['others_dr'],r['momentum_ppo'])),(smallerThan(r['trend_sma_fast'],r['volume_fi']) and (greaterThan(r['trend_kst_diff'],r['volatility_bbw']) or (smallerThan(r['trend_sma_slow'],r['momentum_kama']) or smallerThan(r['trend_stc'],r_ant['trend_adx'])))))"
#14124042
p="(5,(smallerThan(r['volume_obv'],r['trend_mass_index']) or smallerThan(r['trend_psar_down_indicator'],r['momentum_ppo'])),(smallerThan(r['volatility_kcl'],r['volume_fi']) and (greaterThan(r['trend_kst_diff'],r['volatility_bbw']) or (smallerThan(r['trend_sma_slow'],r['momentum_kama']) or smallerThan(r['trend_stc'],r_ant['trend_adx'])))))"
#ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=3,init="1 Mar, 2021",end="26 Apr, 2021",typeMarket="future",phenotype=p)


#15mins
print("Grafico de 15m Futuros")
p="(5,smallerThan(r['volume_em'],r['volume_sma_em']),(greaterThan(r['trend_aroon_down'],r['momentum_ppo']) and (greaterThan(r['volatility_kch'],r['volatility_dch']) or (smallerThan(r_ant['volume_adi'],r['volume_em']) and (greaterThan(r['trend_kst'],r['momentum_tsi']) or greaterThan(r['Low'],r_ant['trend_psar_down']))))))"
p="(5,smallerThan(r['volume_em'],r['volume_sma_em']),(greaterThan(r['trend_aroon_down'],r['momentum_ppo']) and (greaterThan(r['volatility_kch'],r['volatility_dch']) or (smallerThan(r_ant['volume_adi'],r['volume_em']) and (greaterThan(r['trend_kst'],r['momentum_tsi']) or greaterThan(r['Low'],r_ant['trend_psar_down']))))))"

p="(5,smallerThan(r['volume_em'],r['volume_sma_em']),(greaterThan(r['trend_aroon_down'],r['momentum_ppo']) and (greaterThan(r['volatility_kch'],r['volatility_dch']) or (smallerThan(r_ant['volume_adi'],r['volume_em']) and (greaterThan(r['trend_kst'],r['momentum_tsi']) or greaterThan(r['Low'],r_ant['trend_psar_down']))))))"
ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=3,init="1 Mar, 2021",end="26 Apr, 2021",typeMarket="future",phenotype=p)
