import compileAll
compileAll.compiler()
import sys
sys.path.append('../../')

from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
import os
import time
import shutil
import numpy as np
import Examples.Python_Trading.fitnesFunction as ff
from numpy import load
from numpy import save
from pathlib import Path
import pickle
from Examples.Python_Trading.historicalCripto import HistoricalCripto
import matplotlib.pyplot as plt
import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands
def prossesIndividue(ind, debug=True):
    #print(ind.genotype)

    if ind.phenotype.count("<") == 0:
        dim = np.loadtxt("SampleData.txt", dtype=float)
        score= ff.fitnesFunction(ind.phenotype,dim)
        #if ind.fitness_score>0:
        if ind.fitness_score==-1:
            #time.sleep(10)
            print("Error raro -1")
        else:
            ind.fitness_score=score
    else:
        ind.fitness_score= 0
    #if debug:
        #porcentProgress = int(int(i) * 100 / int(lenPopulation))
        #print(str(i) + "/" + str(lenPopulation) + " ->" + str(porcentProgress) + "% ->" + "Result_exect_Score: " + str(
        #    ind.fitness_score))
        #print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score
def createPhenotypes():
    #extraction Data
    data="data"
    if not os.path.isdir(data):
        for i in [1,2,3,4,5,7]:
            hC = HistoricalCripto()
            hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))
    df = pd.read_csv(data + '//Binance_BTCUSDT_1m_1609459200000-1649548800000.csv')
    df.head()
    columns=['Close']
    dataPlot=df.loc[:, columns]
    print(dataPlot)
    plt.plot(dataPlot[-100:])
    plt.ylabel(columns)
    plt.show()

    # Clean NaN values
    df = dropna(df)

    # Add ta features filling NaN values
    df = add_all_ta_features(
        df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
    # Initialize Bollinger Bands Indicator
    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)

    # Add Bollinger Bands features
    df['bb_bbm'] = indicator_bb.bollinger_mavg()
    df['bb_bbh'] = indicator_bb.bollinger_hband()
    df['bb_bbl'] = indicator_bb.bollinger_lband()

    # Add Bollinger Band high indicator
    df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

    # Add Bollinger Band low indicator
    df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

    # Add Width Size Bollinger Bands
    df['bb_bbw'] = indicator_bb.bollinger_wband()

    # Add Percentage Bollinger Bands
    df['bb_bbp'] = indicator_bb.bollinger_pband()
    return 0
    #fileSave="data_1"
    #fileObj = Path(fileSave + '.txt')
    #if fileObj.is_file():
    #    f=open(fileSave + '.txt', 'rb')
    #    population=pickle.loads(f.read())
    #    f.close()
    #    #print(pop[0].phenotype)
    #    #pop = load(fileSave + '.txt',allow_pickle=True)
    #else:
    #    pop = Population(numberIndividuals=25, individualSize=18)
    #    population = pop.generatePop()
    #algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    #evolvedPop = algo.evolveWithGE(population, prossesIndividue,gen=1000,porcentSelect=0.2,fileSave=fileSave,reverse=True)


    #inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
    #inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
    #print("")
    #("Top mejores 20:")
    #for ind in inds[0:20]:
    #    print(ind.genotype)
    #    print(ind.phenotype)
    #    print(ind.fitness_score)
    #    print("========================================================================================================")
createPhenotypes()
