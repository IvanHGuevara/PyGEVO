#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
#from utils_.search_operators import compileAll
#compileAll.compiler()
from Examples.Python_Pi import compileAll
compileAll.compiler()


from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
import os
import time
import shutil
import numpy as np
import Examples.Python_Pi.fitnesFunction as ff
from numpy import load
from numpy import save
from pathlib import Path
import pickle


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
    if debug:


        #porcentProgress = int(int(i) * 100 / int(lenPopulation))
        #print(str(i) + "/" + str(lenPopulation) + " ->" + str(porcentProgress) + "% ->" + "Result_exect_Score: " + str(
        #    ind.fitness_score))
        print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score
def createPhenotypes():
    fileSave="data_1"
    fileObj = Path(fileSave + '.txt')
    if fileObj.is_file():
        f=open(fileSave + '.txt', 'rb')
        population=pickle.loads(f.read())
        f.close()
        #print(pop[0].phenotype)
        #pop = load(fileSave + '.txt',allow_pickle=True)
    else:
        pop = Population(numberIndividuals=25, individualSize=18)
        population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_FitnesFunction(population, prossesIndividue,gen=1000,porcentSelect=0.2,estaticSelect=25,fileSave=fileSave)


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