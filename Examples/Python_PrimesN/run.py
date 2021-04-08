#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
#from utils_.search_operators import compileAll
#compileAll.compiler()
from Examples.Python_PrimesN import compileAll
compileAll.compiler()


from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
import os
import time
import shutil
import numpy as np
import Examples.Python_PrimesN.fitnesFunction as ff



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
    pop = Population(numberIndividuals=100, individualSize=20)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE(population, prossesIndividue,gen=30,porcentSelect=0.2, staticSelect=100)


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