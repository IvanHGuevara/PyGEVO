import sys
sys.path.append('../')
from utils_.search_operators.ga import GA
from utils_.domain_objects.population import Population

def initialise_test():
    return Population(numberIndividuals=4, individualSize=8)

def test_grammarMethods():
    population = initialise_test()
    population = population.generatePop()
    individuals = population.pop
    assert(len(GA.crossover(individuals))) == 4