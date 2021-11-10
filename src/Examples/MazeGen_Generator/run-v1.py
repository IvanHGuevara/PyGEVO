import sys
sys.path.append('../../')
import Examples.MazeGen_Generator.fitnessFunctionv1 as ff
from core.domain.population import Population
from utils_.algorithms import Algorithms


def processIndividual(individual):
    if individual.isValid():  
        score, stringBuild = ff.fitnessFunction(individual.phenotype)
        individual.fitness_score = score
        individual.stringBuild = str(stringBuild)
    else:
        individual.fitness_score = 0
    return individual.fitness_score

RUNS = 15

for i in range(RUNS):
    print("RUN number", str(i))
    pop = Population("grammar-v1.bnf", numberIndividuals=50000, individualSize=32,  fitness_function=ff.fitnessFunction)
    population = pop.generatePop()
    algo = Algorithms("grammar-v1.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE(population, pop, processIndividual,gen=30,porcentSelect=0.1,fileSave="",reverse=True,debug=True)
    f = open("RUN_50000_v1-32ind_Number_" + str(i), 'wt')
    f.write(str("RUN Number ") + str(i))
    for ind in evolvedPop:
        f.write(str(ind.phenotype))
        f.write("\n")
        f.write(str(ind.fitness_score))
        f.write("\n")
        f.write(str(ind.stringBuild))
        f.write("========================================================================================================")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    f.close()
