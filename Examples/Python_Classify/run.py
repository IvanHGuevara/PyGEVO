import sys
sys.path.append('../../')
from compiler import Compiler
Compiler.enableCython()
Compiler.compile()

import pyximport
pyximport.install()

from FitnessFunction import FitnessFunction
import numpy as np
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms

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
    population = Population(numberIndividuals=10, individualSize=20).generatePop()
    population = Algorithms("grammar.bnf", initBNF=1, debug=False).evolveWithGE(population, processIndividual, gen=6, porcentSelect=0.2, staticSelection=50, validIndividuals=True, orderedByFitness=True)
    population.showTopTen()

createPhenotypes()