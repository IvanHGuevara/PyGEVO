import sys
sys.path.append('../../')
#from compiler import Compiler
#comp=Compiler()
#comp.enableCython()
#comp.compile()

import pyximport
pyximport.install()
from Examples.Python_Classify.FitnessFunction import FitnessFunction
import numpy as np
import sys
sys.path.append('../../')
from core.domain.population import Population
from core.domain.algorithms import Algorithms


def runPhenotype(phenotype):
    dim=np.loadtxt("SampleData.txt",dtype=float)
    score=FitnessFunction(phenotype,dim)
    return score

def processIndividual(ind, debug = False):
    if ind.phenotype.count("<") == 0:
        dim = np.loadtxt("SampleData.txt", dtype=float)
        ind.fitness_score= FitnessFunction(ind.phenotype,dim)
    else:
        ind.fitness_score= 0
    if debug:
        print(ind.phenotype)
        print(ind.fitness_score)
        print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score

def createPhenotypes():
    grammar="grammar.bnf"
    pop = Population(grammar,numberIndividuals=100, individualSize=200,fitness_function=processIndividual)
    population = pop.generatePop()
    algo = Algorithms(grammar, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE(population, populationFactory=pop, gen=60, porcentSelect=0.2, staticSelection=50,debug=True)
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