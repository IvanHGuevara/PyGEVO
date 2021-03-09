from random import randint

class Population:
    def __init__(self, numberIndividuals, individualSize = 5) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
    
    def generatePop(self):
        for _ in range(self.numberIndividuals):
            individual = []
            for _ in range(self.individualSize):
                individual.append(randint(1,255))
            self.pop.append(individual)
        return self.pop