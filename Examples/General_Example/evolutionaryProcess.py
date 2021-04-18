from utils_.cythonFunctions import compileAll
compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA

pop = Population(numberIndividuals=6, individualSize=8)
population = pop.generatePop()
algo = Algorithms("grammar_ANSI_C.bnf",gen=5, initBNF=56,debug=False)
evolvedPop = algo.evolveWithGE(population, 3)