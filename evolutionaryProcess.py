from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from utils_.algorithms import Algorithms

pop = Population(numberIndividuals=1000000, individualSize=10)
population = pop.generatePop()
algo = Algorithms("/Users/iguevara/Projects/Confirm Centre/PyGE/grammar.bnf")
evolvedPop = algo.evolveWithGE(population, gen=10)
print(evolvedPop)

