from random import randint

from utils_.general_functions import General_functions
class Population:
    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
    
    def generatePop(self):
        General_functions.async_map(lambda _: self.generateIndividual(), range(self.numberIndividuals))
        return self.pop

    async def generateIndividual(self):
        ind = []
        for _ in range(self.individualSize):
             ind.append(randint(1,255))
        self.pop.append(ind)
