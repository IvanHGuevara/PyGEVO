import sys
sys.path.append('../../')
from core.domain.population import Population
from core.domain.algorithms import Algorithms
import numpy as np
import Examples.Python_PrimesN.fitnessFunction as ff

def processIndividual(ind, debug=True):
    if ind.isValid():
        dim = np.loadtxt("SampleData.txt", dtype=float)
        score= ff.fitnesFunction(ind.phenotype,dim)
        if ind.fitness_score==-1:
            print("Unknown error")
        else:
            ind.fitness_score=score
    else:
        ind.fitness_score= 0
    return ind.fitness_score

def createPhenotypes():
    fileSave="data"
    grammar="grammar.bnf"
    pop = Population(grammar, numberIndividuals=1000, individualSize=50, fitness_function=processIndividual)
    population = pop.generatePop()
    algo = Algorithms(grammar, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_v1(population, populationFactory=pop, gen=10000, porcentSelect=0.5, fileSave=fileSave, reverse=True, debug=True, staticSelection=1000)
    inds=sorted(evolvedPop,key=lambda ind: ind.fitness_score, reverse=True)
    print("")
    print("Best 20:")
    for ind in inds[0:20]:
        print(ind.genotype)
        print(ind.phenotype)
        print(ind.fitness_score)
        print("========================================================================================================")

createPhenotypes()