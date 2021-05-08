from ..core.searchOperators.gaCore import GA
from ..core.domain.population import Population

def initialise_test():
    return Population(numberIndividuals=4, individualSize=8)

def test_grammarMethods():
    population = initialise_test()
    assert(len(GA.crossover(population.generatePop()))) == 4