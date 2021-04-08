from utils_.cythonFunctions import compileAll
compileAll.compiler()
from utils_.search_operators import compileAll
compileAll.compiler()
from Examples.Python_Classify import compileAll
compileAll.compiler()


#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
#from Python_Classify import compileAll
#compileAll.compiler()
import pyximport
pyximport.install()
import numpy as np
from FitnessFunction import FitnessFunction
import sys
sys.path.append('../../')
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms

def runPhenotype(phenotype):
    dim=np.loadtxt("SampleData.txt",dtype=float)
    score=FitnessFunction(phenotype,dim)
    return score

def processIndividual(ind):
    if ind.phenotype.count("<") == 0:
        dim = np.loadtxt("SampleData.txt", dtype=float)
        ind.fitness_score= ff.fitnesFunction(ind.phenotype,dim)
        #if ind.fitness_score>0:

    else:
        ind.fitness_score= 0
    if debug:
        print(ind.phenotype)
        print(ind.fitness_score)

        #porcentProgress = int(int(i) * 100 / int(lenPopulation))
        #print(str(i) + "/" + str(lenPopulation) + " ->" + str(porcentProgress) + "% ->" + "Result_exect_Score: " + str(
        #    ind.fitness_score))
        print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score

def createPhenotypes():
    pop = Population(numberIndividuals=10, individualSize=20)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_FitnesFunction(population, processIndividual,gen=6,porcentSelect=0.2,estaticSelect=50)
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