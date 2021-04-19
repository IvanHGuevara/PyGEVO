import Examples.Python_Trading.fitnesFunction as ff
#39766.416312626636
p="(1,(greaterThan(r['volume_mfi'],r['trend_aroon_down']) and (greaterThan(r_ant['volume_nvi'],r['momentum_stoch_rsi_d']) or smallerThan(r_ant['momentum_kama'],r['trend_vortex_ind_neg']))),smallerThan(r['trend_adx_pos'],r['trend_macd_diff']),smallerThan(r['volume_em'],r['volume_mfi']),smallerThan(r['trend_macd_signal'],r['Low']))"
ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=6,init="1 Jan, 2021",end="18 Apr, 2021",phenotype=p)