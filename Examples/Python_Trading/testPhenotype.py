import Examples.Python_Trading.fitnesFunction as ff
phenotype="((smallerThan(r['trend_macd_signal'],r['volatility_bbm']) and (smallerThan(r['others_cr'],r['volatility_kcw']) and smallerThan(r['trend_kst_diff'],r['volatility_dch']))),(smallerThan(r['trend_ema_fast'],r['volatility_bbhi']) or (smallerThan(r['volatility_dcw'],r['volume_em']) and smallerThan(r['volatility_dcp'],r['momentum_ppo_signal']))),20)"
ff.fitnesFunction_futuro(symbol="BTCUSDT",graficTypeNum=3,init="17 Mar, 2021",end="17 Apr, 2021",phenotype=phenotype)