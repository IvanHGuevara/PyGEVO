import sys
sys.path.append('../../')
import Examples.MazeGen_Generator.fitnessFunctionv1 as ff
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms

def processIndividual(individual):
    if individual.isValid():  
        score, stringBuild = ff.fitnessFunction(individual.phenotype)
        individual.fitness_score = score
        individual.stringBuild = stringBuild
    else:
        individual.fitness_score = 0
    return individual.fitness_score

pop = Population(numberIndividuals=100, individualSize=32)
population = pop.generatePop()
algo = Algorithms("grammar-v1.bnf", initBNF=1, debug=False)
evolvedPop = algo.evolveWithGE(population, processIndividual,gen=15,porcentSelect=0.5,fileSave="",reverse=False,debug=True)
evolvedPop.showTopTen()