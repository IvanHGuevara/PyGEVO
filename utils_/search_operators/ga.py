import random
import math
import numpy as np
import copy

class GA:

    @staticmethod
    def select(individuals, porcent=0.5,estaticSelect=0):
        if estaticSelect<=0:
            n=math.trunc(len(individuals)*porcent)
        else:
            n=estaticSelect
        return individuals[:n]

    @staticmethod
    def evaluate(ind, function):
        fitness_score = function(ind)
        ind.fitness_score = fitness_score
        return ind

    @staticmethod
    def mutateInd(indG):
        size=len(indG.genotype)
        point = random.randint(0, size - 1)
        newIndG=copy.deepcopy(indG)
        newIndG.genotype[point]=random.randint(0, 256)
        return newIndG

    @staticmethod
    def mutate(individuals, algorithms):
        g=np.array(GA.mutateInd(ind) for ind in individuals)
        individuals = algorithms.evolveWithGE(g)
        return individuals

    @staticmethod
    def crossoverInds(ind1,ind2,point):
        ind1.genotype[point:], ind2.genotype[point:] = ind2.genotype[point:], ind1.genotype[point:]
        return ind1, ind2

    @staticmethod
    def crossover(individuals):

        gs=[]
        g = list(ind for ind in individuals)
        point = random.randint(1, len(g[0].genotype) - 1)
        for ind1,ind2 in zip(g[0::2], g[1::2]):
            ind1New=copy.deepcopy(ind1)
            ind2New = copy.deepcopy(ind2)
            i1,i2=GA.crossoverInds(ind1New,ind2New,point)
            if i1 not in gs:
                gs.append(i1)
            if i2 not in gs:
                gs.append(i2)
        gs_a=np.array(gs)

        return gs_a
