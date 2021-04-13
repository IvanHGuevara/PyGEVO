#from random import randint
#from utils_.general_functions import General_functions
import numpy as np
from .Individual import Individual

class Population:

    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
    
    #def generatePop_(self):
    #    General_functions.async_map(lambda _: self.generateIndividual(), range(self.numberIndividuals))
    #    return self.pop

    def generatePop(self):
        individuals = []
        self.pop = np.random.randint(255, size=(self.numberIndividuals,self.individualSize))
        for genotype in self.pop:
            ind = Individual()
            ind.genotype = genotype
            individuals.append(ind)
        return individuals

