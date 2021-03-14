#from random import randint
#from utils_.general_functions import General_functions
import numpy as np

class Population:

    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
    
    #def generatePop_(self):
    #    General_functions.async_map(lambda _: self.generateIndividual(), range(self.numberIndividuals))
    #    return self.pop

    #async def generateIndividual(self):
    #    ind = []
    #    for _ in range(self.individualSize):
    #         ind.append(randint(1,255))
    #    self.pop.append(ind)

    def generatePop(self):
        self.pop =  np.random.randint(255, size=(self.numberIndividuals,self.individualSize))
        return self.pop

