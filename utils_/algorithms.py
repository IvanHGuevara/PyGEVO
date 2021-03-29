from utils_.cythonFunctions.mapper import Mapper
#from utils_.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
from utils_.general_functions import General_functions
from .search_operators.ga import GA
from .fitness_functions.fitness_functions import FitnessFunctions
import numpy as np

class Algorithms:

    def __init__(self, grammarPath,gen = 1, initBNF=1,debug=False) -> None:
        self.mapper = Mapper(GrammarWrapper.createFromFile(grammarPath))
        self.mapper.toMatrixBNF()
        self.gen=gen
        self.initBNF=initBNF
        self.debug=debug

    def evolveWithGE_(self, population, gen = 1, initBNF=1):
        evolvedIndividuals = []
        for generationNumber in range(gen):
            print("Generation: ", generationNumber)
            print("===================================================================")
            for ind in population:
                ind.phenotype=self.mapper.mapBNF(ind.genotype,initBNF-1)
                evolvedIndividuals.append(ind)
            print("selecting individuals with a probability of: ", 0.5)
            individualBatch = GA.select(evolvedIndividuals,0.5)
            print("Grabbing a batch of: ", len(individualBatch))
            print("mutating individuals.......")
            individualBatch = list(map(lambda indG: GA.mutateInd(indG), individualBatch))
            print("generating crossover.......")
            individualBatch = GA.crossover(individualBatch, self)
            newPopulation = np.concatenate((individualBatch, population))
            print("reevaluate new population")
            newPopulation = list(map(lambda ind: GA.evaluate(ind, FitnessFunctions.griewangk), newPopulation))
            individualBatch = sorted(individualBatch, key= lambda ind: ind.fitness_score, reverse=True)
            individualBatch = individualBatch[:100]
            evolvedIndividuals = []
            print("===================================================================")
            population = newPopulation
        return population
        
    def evolveWithGE(self, population):
        for _ in range(self.gen):
            evolvedIndividuals =  list(General_functions.async_map_g((lambda ind: self.mapper.mapBNF(ind.genotype,self.initBNF-1,debug=self.debug)[0]), population))
            for idx, ind in enumerate(population):
                ind.phenotype = evolvedIndividuals[idx]
        return population

    def evolveWithGE_FitnesFunction(self, population,fitness_function, gen = 1, initBNF=1,porcent=0.5):
        evolvedIndividuals = []

        for generationNumber in range(gen):
            print("Generation: ", generationNumber)
            print("===================================================================")

            for ind in population:
                ind.phenotype=self.mapper.mapBNF(ind.genotype, initBNF - 1)
                evolvedIndividuals.append(ind)
            print("selecting individuals with a probability of: ", porcent)
            individualBatch = GA.select(evolvedIndividuals,porcent)
            print("Grabbing a batch of: ", len(individualBatch))
            print("mutating individuals.......")
            individualBatch = list(map(lambda indG: GA.mutateInd(indG), individualBatch))
            print("generating crossover.......")
            individualBatch = GA.crossover(individualBatch, self)
            newPopulation = np.concatenate((individualBatch, population))
            print("reevaluate new population")
            newPopulation = list(map(lambda ind: GA.evaluate(ind, fitness_function), newPopulation))
            #individualBatch = sorted(enumerate(individualBatch), key= lambda ind: (fitness_function(ind[1],ind[0]+1,len(individualBatch)).fitness_score,len(ind[1].phenotype)), reverse=True)
            newPopulation = sorted(newPopulation, key=lambda ind: ind.fitness_score, reverse=True)

            print("===================================================================")
            population = newPopulation

        return population