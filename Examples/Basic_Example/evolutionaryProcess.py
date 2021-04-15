import sys
sys.path.append("../../")
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms
from utils_.fitness_functions.fitness_functions import FitnessFunctions

population = Population(numberIndividuals=6, individualSize=8).generatePop()
population = Algorithms("grammar_action.bnf", initBNF=56, debug=False).evolveWithGE(population, FitnessFunctions.griewangk , gen=4, porcentSelect=0.2, staticSelection=50, validIndividuals=True, orderedByFitness=True)
population.showTopTen()