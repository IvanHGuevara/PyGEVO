import sys
sys.path.append('../../')
import Examples.MazeGen_Generator.fitnessFunctionv2 as ff
from core.domain.population import Population
from core.domain.algorithms import Algorithms

RUNS = 1

for i in range(RUNS):
    print("RUN number", str(i))
    pop = Population("grammar-v2.bnf", numberIndividuals=5000, individualSize=16,  fitness_function=ff.fitnessFunction)
    population = pop.generatePop()
    algo = Algorithms("grammar-v2.bnf", initBNF=0, debug=False)
    evolvedPop = algo.evolveWithGE_v1(population, pop, gen=15, porcentSelect=0.6, fileSave="",reverse=True)
    f = open("RUN_5000_v1-32ind_Number_" + str(i), 'wt')
    f.write(str("RUN Number ") + str(i))
    for ind in evolvedPop[0:9]:
        f.write("\n")
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
