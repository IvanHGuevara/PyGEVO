import sys
sys.path.append('../../')
import Examples.MazeGen_Generator.fitnessFunction as ff
from core.domain.population import Population
from utils_.algorithms import Algorithms
import pickle

def processIndividual(individual):
    if individual.isValid():  
        score = ff.fitnessFunction(individual)
        individual.fitness_score = score
    else:
        individual.fitness_score = 0
    return individual.fitness_score

RUNS = 15

for i in range(RUNS):
    print("RUN number", str(i))
    pop = Population("grammar.bnf", numberIndividuals=5000, individualSize=32,  fitness_function=ff.fitnessFunction)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE(population, pop, processIndividual,gen=15,porcentSelect=0.1,fileSave="",reverse=True,debug=True)
    f = open("RUN_5000_ind_Number_" + str(i), 'wt')
    f.write(str("RUN Number ") + str(i))
    for ind in evolvedPop[0:9]:
        f.write(str(ind.phenotype))
        f.write("\n")
        f.write(str(ind.fitness_score))
        f.write("\n")
        f.write("========================================================================================================")
        f.write("\n")
        f.write("\n")
        f.write("\n")
    f.close()