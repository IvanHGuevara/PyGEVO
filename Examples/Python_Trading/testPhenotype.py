import Examples.Python_Trading.fitnesFunction as ff
#39766.416312626636
p="(5,(greaterThan(r['volume_fi'],r['volatility_kcp']) or (greaterThan(r_ant['Close'],r['trend_vortex_ind_neg']) and (smallerThan(r['volatility_bbh'],r_ant['momentum_kama']) or greaterThan(r_ant['trend_stc'],r_ant['trend_ichimoku_conv'])))),smallerThan(r['trend_stc'],r['momentum_ppo_hist']))"
ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=6,init="1 Jan, 2021",end="18 Apr, 2021",phenotype=p)