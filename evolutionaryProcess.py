from utils.grammarReader import GrammarWrapper
from utils.population import Population
from utils.algorithms import Algorithms

pop = Population(numberIndividuals=10, individualSize=8)
population = pop.generatePop()
print(population)
grammar = GrammarWrapper("grammar.bnf")
algo = Algorithms(grammar)
evolvedPop = algo.evolveWithGE(population, gen=10)
print(evolvedPop)
