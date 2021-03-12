from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from utils_.grammarWrapper import GrammarWrapper
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms

pop = Population(numberIndividuals=10000, individualSize=20)
population = pop.generatePop()
print(population)
#grammar = GrammarWrapper("grammar_1.bnf")
#algo = Algorithms(grammar)
algo = Algorithms("grammar_1.bnf")
evolvedPop = algo.evolveWithGE_v2(population, gen=10)
print(evolvedPop)
