from compiler import Compiler
comp=Compiler()
#comp.enableCython()
comp.compile()
import ta
import sys
sys.path.append('../../')
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
import os
import Examples.Python_Trading.fitnesFunction as ff
from pathlib import Path
import pickle
from Examples.Python_Trading.historicalCripto import HistoricalCripto
import matplotlib.pyplot as plt
import pandas as pd
from ta.utils import dropna
from utils_.search_operators.ga import GA

class Run:
    def __init__(self) -> None:
        self.symbol="BTCUSDT"

        self.carpeta = "data"
        self.file = None
        self.data = None
    def prossesIndividue(self,ind, debug=True):
        #print(ind.genotype)

        if ind.phenotype.count("<") == 0:

            score= ff.fitnesFunction(ind.phenotype,self.data)
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
    def createPhenotypes(self):
        #extraction Data

        #1: Client.KLINE_INTERVAL_1MINUTE,
        #2: Client.KLINE_INTERVAL_3MINUTE,
        #3: Client.KLINE_INTERVAL_5MINUTE,
        #4: Client.KLINE_INTERVAL_15MINUTE,
        #5: Client.KLINE_INTERVAL_30MINUTE,
        #6: Client.KLINE_INTERVAL_1HOUR,
        #7: Client.KLINE_INTERVAL_2HOUR,
        #8: Client.KLINE_INTERVAL_4HOUR,
        #9: Client.KLINE_INTERVAL_6HOUR,
        #10: Client.KLINE_INTERVAL_8HOUR,
        #11: Client.KLINE_INTERVAL_12HOUR,
        #12: Client.KLINE_INTERVAL_1DAY,
        #13: Client.KLINE_INTERVAL_3DAY,
        #14: Client.KLINE_INTERVAL_1WEEK,
        #15: Client.KLINE_INTERVAL_1MONTH
        #for i in [1,2,3,4,5,7]:
        #6,3,1
        for i in [6]:
            hC = HistoricalCripto()
            #hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))
            fileName=hC.getData((self.symbol, i, "1 Jan, 2021", "17 Mar, 2021"))

            self.file = fileName[:-4]
            if not os.path.isfile(self.carpeta + "//" + self.file+ '_Indicators' +".csv"):
                df = pd.read_csv(self.carpeta + '//' + self.file+".csv")
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
                df.to_csv(self.carpeta + "//" + self.file+ '_Indicators' +".csv", sep=',')




        #df = pd.read_csv(carpeta + '//Binance_BTCUSDT_1m_1609459200000-1649548800000.csv')
        #df.head()
        #columns=['Close']
        #dataPlot=df.loc[:, columns]
        #print(dataPlot)
        #plt.plot(dataPlot[-100:])
        #plt.ylabel(columns)
        #plt.show()

        self.data=pd.read_csv(self.carpeta + "//" + self.file+ '_Indicators' +".csv")


        fileSave = self.carpeta + "//" + self.file+ '_Data'
        fileObj = Path(fileSave )
        pop = Population("grammar.bnf", numberIndividuals=25, individualSize=50, fitness_function=self.prossesIndividue)
        if fileObj.is_file():
            try:
                f = open(fileSave , 'rb')

                population = pickle.loads(f.read())
                f.close()
            except:
                f.close()
                sys.exit()
            # print(pop[0].phenotype)
            # pop = load(fileSave + '.txt',allow_pickle=True)
            evolvedIndividuals = []

            # for ind in population:

            #    evolvedIndividuals.append(ind)
            # population=evolvedIndividuals
            population = sorted(population, key=lambda ind: (ind.fitness_score), reverse=True)
            population = GA.select(population, 0.05, 500)
        else:

            population = pop.generatePop()
            print(population)
        algo = Algorithms("grammar.bnf", initBNF=1, debug=False)

        evolvedPop = algo.evolveWithGE(population, populationFactory=pop, gen=100000, porcentSelect=0.9,staticSelection=1000, fileSave=fileSave,
                                       reverse=True, debug=True,noDuplicates=True,cacheScore=True)  # ,staticSelection=200


        #inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
        #inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
        #print("")
        #("Top mejores 20:")
        #for ind in inds[0:20]:
        #    print(ind.genotype)
        #    print(ind.phenotype)
        #    print(ind.fitness_score)
        #    print("========================================================================================================")
run=Run()
run.createPhenotypes()
