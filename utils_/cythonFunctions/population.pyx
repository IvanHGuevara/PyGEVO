from random import randint

from utils_.general_functions import General_functions


class Population:

    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
    
    #def generatePop(self):
    #    for _ in range(self.numberIndividuals):
    #        individual = []
    #        for _ in range(self.individualSize):
    #            individual.append(randint(1,255))
    #        self.pop.append(individual)
    #    return self.pop

    def generatePop(self):
        individuals = list(
            General_functions.async_map(lambda codon: self.generateIndividual(), range(self.numberIndividuals)))
        self.pop=individuals
        return self.pop

    async def generateIndividual(self):
        individual = []
        individual=[randint(0,255) for _ in range(self.individualSize)]
        self.pop.append(individual)
        return individual

