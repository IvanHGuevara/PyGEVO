#from compiler import Compiler
#comp=Compiler()
#comp.enableCython()
#comp.compile()
import sys
sys.path.append('../../')
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.fitnessFunctions.syntheticFunctions import FitnessFunctions
import time

s = time.time()
grammar="grammar.bnf"
pop = Population(grammar,numberIndividuals=10000, individualSize=8, fitness_function=FitnessFunctions.rosenbrock)
population = pop.generatePop()
algo = Algorithms(grammar, initBNF=56)
evolvedPop = algo.evolveWithGE_v1(population, populationFactory=pop, gen=400, porcentSelect=0.6, staticSelection=250, debug=True)
print("Time taken:", time.time() - s)