from utils_.population import Population
from utils_.algorithms import Algorithms

pop = Population(numberIndividuals=100000, individualSize=10)
population = pop.generatePop()
print(population)
algo = Algorithms("/Users/iguevara/Projects/Confirm Centre/PyGE/grammar.bnf")
evolvedPop = algo.evolveWithGE(population, gen=10)
print(evolvedPop)

