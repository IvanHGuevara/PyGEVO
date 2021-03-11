from utils_.grammarWrapper import GrammarWrapper
from utils_.population import Population
from utils_.algorithms import Algorithms

pop = Population(numberIndividuals=10, individualSize=80)
population = pop.generatePop()
print(population)
grammar = GrammarWrapper("grammar.bnf")
algo = Algorithms(grammar)
evolvedPop = algo.evolveWithGE(population, gen=10)
print(evolvedPop)
