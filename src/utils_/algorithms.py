from compiler import Compiler
if Compiler.cythonEnabled:
    import pyximport
    pyximport.install()
from core.domain.mapper import Mapper
from core.domain.grammarWrapper import GrammarWrapper
from core.domain.generalFunctions import General_functions
from core.searchOperators.gaCore import GA
import numpy as np
import pickle


class Algorithms:

    def __init__(self, grammarPath, initBNF=1, debug=False) -> None:
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

    def evolveWithGE(self, population, populationFactory=None, fitness_function = None, gen = 1, initBNF=1, porcentSelect=0.5, staticSelection=0, fileSave="", reverse=True):
        self.gen=gen
        evolvedIndividuals = []
        for generationNumber in range(gen):
            print("Generation: ", generationNumber)
            print("===================================================================")
            for ind in population:
                ind.phenotype=self.mapper.mapBNF(ind.genotype, initBNF - 1)[0]
                evolvedIndividuals.append(ind)
            if staticSelection<=0:
                print("selecting individuals with a probability of: ", porcentSelect)
            else:
                print("selecting individuals : ", staticSelection)
            individualBatch = GA.select(evolvedIndividuals,porcentSelect,staticSelection)
            print("Grabbing a batch of: ", len(individualBatch))
            print("mutating individuals.......")
            #Save Population
            if fileSave != "":
                f=open(fileSave+'.txt', 'wb')
                f.write(pickle.dumps(population))
                f.close()
            individualBatch_1 = list(General_functions.async_map(lambda indG: GA.mutateInd(indG), individualBatch))
            print("generating crossover.......")
            individualBatch = GA.crossover(individualBatch)
            newPopulation = np.concatenate((individualBatch, individualBatch_1))
            print("reevaluate new population")
            newPopulation = list(set(newPopulation))
            newPopulation = list(General_functions.async_map(lambda ind: GA.evaluate(ind, fitness_function), newPopulation))
            newPopulation = sorted(newPopulation, key=lambda ind: (ind.fitness_score,len(ind.phenotype)), reverse=reverse)
            self.showTopTen(newPopulation)
        return newPopulation

    def showTopTen(_, population):
        print("Top ten:")
        for ind in population[0:9]:
            print(ind.genotype)
            print(ind.phenotype)
            print(ind.fitness_score)
            print("========================================================================================================")

    def showTopTenWithKiviLanguage(_, population):
        print("Top ten:")
        i = 0
        for ind in population[0:9]:
            print(ind.genotype)
            print(ind.phenotype)
            print(ind.fitness_score)
            print(ind.stringBuild)
            f = open("KiviFile" + "_" + str(i) + ".txt", "wt")
            print(ind.stringBuild)
            f.write(ind.stringBuild)
            f.close()
            i = i + 1
            print("========================================================================================================")
