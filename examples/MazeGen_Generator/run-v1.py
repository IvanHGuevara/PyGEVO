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

pop = Population("grammar-v1.bnf", numberIndividuals=5000, individualSize=18, fitness_function=ff.fitnessFunction)
population = pop.generatePop()
algo = Algorithms("grammar-v1.bnf", initBNF=1, debug=False)
evolvedPop = algo.evolveWithGE(population, pop, processIndividual,gen=3,porcentSelect=0.3,fileSave="",reverse=True,debug=True)
algo.showTopTenWithKiviLanguage(evolvedPop)