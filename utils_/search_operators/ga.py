import random
import math
import numpy as np
import copy

class GA:
    def __init__(self, algorithms) -> None:
        self.algorithms = algorithms

    def select(_,individuals, porcent=0.5, f_to_int=(lambda x: len(x)),reverse=False):
        n=math.trunc(len(individuals)*porcent)
        return sorted(individuals, key=f_to_int, reverse=reverse)[:n]

    def mutateInd(_,indG):
        size=len(indG.genotype)
        point = random.randint(1, size - 1)
        indG.genotype[point]=random.randint(0, 256)
        return indG

    def mutate(self,individuals):
        g=np.array(list(self.mutateInd(ind) for ind in individuals))
        individuals = self.algorithms.evolveWithGE(g)
        return individuals

    def crossoverInds(_,ind1,ind2,point):
        ind1.genotype[point:], ind2.genotype[point:] = ind2.genotype[point:], ind1.genotype[point:]
        return ind1, ind2

    def crossover(self,individuals):
        g = list(ind for ind in individuals)
        gs=[]
        point = random.randint(1, len(g[0].genotype) - 1)
        g1=g.copy()
        for ind1 in g1:
            g2=g.copy()
            g2.remove(ind1)
            for ind2 in g2:
                ind1New=copy.deepcopy(ind1)
                ind2New = copy.deepcopy(ind2)
                i1,i2=self.crossoverInds(ind1New,ind2New,point)
                if i1 not in gs:
                    gs.append(i1)
                if i2 not in gs:
                    gs.append(i2)
        gs_a=np.array(gs)
        individuals = self.algorithms.evolveWithGE(gs_a)
        return individuals