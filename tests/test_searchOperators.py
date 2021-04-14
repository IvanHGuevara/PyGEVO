import sys
sys.path.append('../')
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA
from utils_.domain_objects.population import Population

def initialise_test():
    return Population(numberIndividuals=4, individualSize=8)

def test_grammarMethods():
    population = initialise_test()
    assert(len(GA.crossover(population.generatePop()))) == 4