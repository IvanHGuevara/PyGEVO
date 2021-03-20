import random
import math
import numpy as np
class GA:
    def __init__(self, algorithms) -> None:
        self.algorithms = algorithms


    def select(self,individuals, porcent=0.5, f_to_int=(lambda x: len(x)),reverse=False):
        n=math.trunc(len(individuals)*porcent)
        return sorted(individuals, key=f_to_int, reverse=reverse)[:n]
    def mutateInd(self,indG):
        size=len(indG)
        point = random.randint(1, size - 1)
        indG[point]=random.randint(0, 256)
        return indG
    def mutate(self,individuals):
        g=np.array(list(self.mutateInd(ind[0]) for ind in individuals))
        individuals = self.algorithms.evolveWithGE(g)
        return individuals
    def crossoverInds(self,ind1,ind2,point):
        ind1[point:], ind2[point:] = ind2[point:], ind1[point:]
        return ind1, ind2
    def crossover(self,individuals):
        g =list(list(ind[0]) for ind in individuals)
        gs=[]
        point = random.randint(1, len(g[0]) - 1)
        print(point)
        g1=g
        g2=g
        for ind1 in g1:

            for ind2 in g2:
                if ind1!=ind2 :
                    i1,i2=self.crossoverInds(ind1,ind2,point)
                    if i1 not in gs:
                        gs.append(i1)
                    if i2 not in gs:
                        gs.append(i2)

        gs_a=np.array(gs)
        individuals = self.algorithms.evolveWithGE(gs_a)
        return individuals