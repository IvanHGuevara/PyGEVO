#from compiler import Compiler
#comp=Compiler()
#comp.enableCython()
#comp.compile()
import sys
sys.path.append('../../')
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.fitnessFunctions.syntheticFunctions import FitnessFunctions

grammar="grammar.bnf"
pop = Population(grammar,numberIndividuals=6, individualSize=8, fitness_function=FitnessFunctions.rosenbrock)
population = pop.generatePop()
algo = Algorithms(grammar, initBNF=56)
evolvedPop = algo.evolveWithGE(population, populationFactory=pop, gen=4, porcentSelect=0.2, staticSelection=50,debug=True, cacheScore=False)
