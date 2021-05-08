
from ..core.searchOperators.gaCore import GA
from ..core.domain.population import Population


def initialise_test():
    return Population(numberIndividuals=4, individualSize=8)

def test_grammarMethods():
    population = initialise_test()
    population = population.generatePop()
    individuals = population.pop
    assert(len(GA.crossover(individuals))) == 4