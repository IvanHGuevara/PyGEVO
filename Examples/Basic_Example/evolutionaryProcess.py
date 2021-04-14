import sys
sys.path.append("../../")
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms
from utils_.fitness_functions.fitness_functions import FitnessFunctions

pop = Population(numberIndividuals=6, individualSize=8)
population = pop.generatePop()
algo = Algorithms("grammar_action.bnf", initBNF=56, debug=False)
evolvedPop = algo.evolveWithGE(population, FitnessFunctions.griewangk , gen=4, porcentSelect=0.2, staticSelection=50)
evolvedPop = evolvedPop.getValidIndividuals()

print("")
print("Showing evolved individuals")
for ind in evolvedPop:
    print(ind.genotype)
    print(ind.phenotype)