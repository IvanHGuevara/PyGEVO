from compiler import Compiler
comp=Compiler()
#comp.enableCython()
comp.compile()
import ta
import sys
sys.path.append('../../')
from core.domain.population import Population
from core.domain.algorithms import Algorithms
import os
import examples.Python_Trading.fitnesFunction as ff
from pathlib import Path
import pickle
from examples.Python_Trading.historicalCripto import HistoricalCripto
import matplotlib.pyplot as plt
import pandas as pd
from ta.utils import dropna
from core.searchOperators.gaCore import GA
import sys
from contextlib import redirect_stdout
import shutil
temp = sys.stdout                 # store original stdout object for later


class Run:

    def __init__(self) -> None:
        self.symbol="BTCUSDT"

        self.carpeta = "data"
        self.file = None
        self.data = None
        self.log=""
    def printL(self, text,end=None):

        with open(self.log,"a") as f:
            if end=="":
                f.write(str(text) )
            else:
                f.write( str(text)+'\n')
            f.close()
            print(str(text),end=end)
    def prossesIndividue(self,ind, debug=True):
        #print(ind.genotype)

        if ind.phenotype.count("<") == 0:

            score= ff.fitnesFunction(ind.phenotype,self.data)
            #if ind.fitness_score>0:
            if ind.fitness_score==-1:
                #time.sleep(10)
                self.printL("Error raro -1")
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
    def createPhenotypes(self,symbol="BTCUSDT",typeMarket="future",intervalo=4, ini="1 Ago, 2020", fin="1 Mar, 2021",individues = 300,individuesSize = 50,gen = 10000):


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


        hC = HistoricalCripto()
        #hC.getData(("BTCUSDT", i, "1 Jan, 2021", "10 Apr, 2022"))
        #fileName=hC.getData((self.symbol, 6, "1 Ago, 2020", "1 Jan, 2021"),typeMarket="future")
        #fileName=hC.getData((self.symbol, i, "2 Ago, 2020", "1 Jan, 2021"),typeMarket="future")
        #fileName = hC.getData((self.symbol, 1, "1 Jan, 2021", "1 Mar, 2021"), typeMarket="future")
        #fileName = hC.getData((self.symbol, 1, "1 Jan, 2021", "1 Mar, 2021"), typeMarket="future") #10
        #fileName = hC.getData((self.symbol, 1, "2 Jan, 2021", "1 Mar, 2021"), typeMarket="future")
        #fileName = hC.getData((self.symbol, 4, "1 Ago, 2020", "1 Mar, 2021"), typeMarket="future")
        #fileName = hC.getData((self.symbol, 3, "1 Ago, 2020", "1 Mar, 2021"), typeMarket="future")
        fileName = "Binance_{}_{}_{}_{}-{}.csv".format(symbol,
                                                       intervalo, typeMarket,
                                                       ini.replace(" ", "_").replace(",", ""),
                                                       fin.replace(" ", "_").replace(",", ""))
        self.file = fileName[:-4]
        self.carpeta = self.carpeta + "//" + self.file
        if not os.path.exists(self.carpeta):
            os.mkdir(self.carpeta)
        hC.getData((symbol,intervalo, ini, fin),fileName=self.file+"//"+fileName,typeMarket=typeMarket)



        self.log=self.carpeta + "//" + self.file+'.log'
        titule=str(symbol) + " " + str(typeMarket) + " " + str(intervalo) + " " + ini + "-" + fin + " Individues:" + str(
            individues) + " Size:" + str(individuesSize) + " Generations:" + str(gen)
        self.printL(titule)
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
        pop = Population("grammar.bnf", numberIndividuals=individues, individualSize=individuesSize, fitness_function=self.prossesIndividue)
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
            population = GA.select(population, 0.05, individues)
        else:

            population = pop.generatePop()
            self.printL(population)
        algo = Algorithms("grammar.bnf", initBNF=1, debug=False)

        evolvedPop = algo.evolveWithGE(population, populationFactory=pop, gen=gen,staticSelection=individues, fileSave=fileSave,
                                       reverse=True, debug=True,noDuplicates=True,cacheScore=True,print=self.printL,titule=titule)  # ,staticSelection=200


        #inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
        #inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
        #print("")
        #("Top mejores 20:")
        #for ind in inds[0:20]:
        #    print(ind.genotype)
        #    print(ind.phenotype)
        #    print(ind.fitness_score)
        #    print("========================================================================================================")
#run=Run()
#run.createPhenotypes()
