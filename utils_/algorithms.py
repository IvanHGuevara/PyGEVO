from utils_.cythonFunctions.mapper import Mapper
#from utils_.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
from utils_.general_functions import General_functions
import pyximport
pyximport.install()
from .search_operators.ga import GA
from .fitness_functions.fitness_functions import FitnessFunctions
import numpy as np
from numpy import load
from numpy import save
from pathlib import Path
import pickle


class Algorithms:

    def __init__(self, grammarPath, initBNF=1,debug=False) -> None:

        self.mapper = Mapper(GrammarWrapper.createFromFile(grammarPath))
        self.mapper.toMatrixBNF()
        self.initBNF=initBNF
        self.debug=debug
        self.gen=0


    def asyncEvolveWithGE(self, population):
        for _ in range(self.gen):
            evolvedIndividuals =  list(General_functions.async_map_g((lambda ind: self.mapper.mapBNF(ind.genotype,self.initBNF-1,debug=self.debug)[0]), population))
            for idx, ind in enumerate(population):
                ind.phenotype = evolvedIndividuals[idx]
        return population


    def evolveWithGE(self, population, populationFactory=None, gen = 1, initBNF=1, porcentSelect=0.5, staticSelection=0, fileSave="", reverse=True,debug=False):
        self.gen=gen

        individualBatch=np.array(population)
        for generationNumber in range(gen):
            print("Generation: ", generationNumber)
            print("===================================================================")
            #for ind in population:
            #    ind.phenotype=self.mapper.mapBNF(ind.genotype, initBNF - 1)[0]
            #    evolvedIndividuals.append(ind)
            if staticSelection<=0:
                print("selecting individuals with a probability of: ", porcentSelect)
            else:
                print("selecting individuals : ", staticSelection)
            print("Grabbing a batch of: ", len(individualBatch))
            print("mutating individuals.......")
            #Save Population
            if fileSave != "":
                f=open(fileSave+'.txt', 'wb')
                f.write(pickle.dumps(individualBatch))
                f.close()

            individualBatch_1 = list(General_functions.async_map_g(lambda indG: GA.mutateInd(indG), individualBatch))
            print("generating crossover.......")
            individualBatch_1 = GA.crossover(individualBatch_1)

            newPopulation = np.concatenate((individualBatch, individualBatch_1))
            newPopulation=populationFactory.recalculate(newPopulation,noDuplicates=True,cacheScore=True)
            #for ind in newPopulation:
            #    ind.phenotype=self.mapper.mapBNF(ind.genotype, initBNF - 1)[0]
            #newPopulation = list(General_functions.async_map_g(lambda ind: GA.evaluate(ind, fitness_function), newPopulation))
            newPopulation = sorted(newPopulation, key=lambda ind: ind.fitness_score, reverse=reverse)
            individualBatch = GA.select(newPopulation, porcentSelect, staticSelection)


            if debug:
                print("Top 10:")
                for ind in individualBatch[:3]:
                    print(ind.genotype)
                    print(ind.phenotype)
                    print(ind.fitness_score)
                    print("========================================================================================================")
        return population