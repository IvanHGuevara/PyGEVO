import numpy as np
from .Individual import Individual

class Population:

    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []

    def generatePop(self):
        randomIndividuals = np.random.randint(255, size=(self.numberIndividuals,self.individualSize))
        for genotype in randomIndividuals:
            ind = Individual()
            ind.genotype = genotype
            self.pop.append(ind)
        return self

    def getValidIndividuals(self):
        return list(filter((lambda ind: ind.isValid()), self.pop))

    def getIndividualsOrderedByFitness(self):
       return sorted(self.pop, key=lambda ind: ind.fitness_score, reverse=True)

