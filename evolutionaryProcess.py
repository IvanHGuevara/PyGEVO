from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
#from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from utils_.algorithms import Algorithms

pop = Population(numberIndividuals=10000, individualSize=100)
population = pop.generatePop()
algo = Algorithms("grammar_1.bnf")
evolvedPop = algo.evolveWithGE(population, gen=10)
print(evolvedPop)

