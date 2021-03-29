#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from Examples.Python_Classify import compileAll
compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
import os
import time
import shutil
import numpy as np
import Examples.Python_Classify.fitnesFunction as ff

def runPhenotype(phenotype):
    dim=np.loadtxt("SampleData.txt",dtype=float)
    score=ff.fitnesFunction(phenotype,dim)

    return score

def prossesIndividue(ind):
    #print(ind.genotype)

    if ind.phenotype.count("<") == 0:
        ind.fitness_score= runPhenotype(ind.phenotype)
        if ind.fitness_score>0:
            print(ind.phenotype)
            print(ind.fitness_score)
    else:
        ind.fitness_score= 0

    #porcentProgress = int(int(i) * 100 / int(lenPopulation))
    #print(str(i) + "/" + str(lenPopulation) + " ->" + str(porcentProgress) + "% ->" + "Result_exect_Score: " + str(
    #    ind.fitness_score))
    print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score
def createPhenotypes():
    pop = Population(numberIndividuals=6, individualSize=25)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", gen=4, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_FitnesFunction(population, prossesIndividue,4,porcent=0.4)
    inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
    inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
    print("")
    print("Top mejores 20:")
    for ind in inds[0:20]:
        print(ind.genotype)
        print(ind.phenotype)
        print(ind.fitness_score)
        print("========================================================================================================")
createPhenotypes()