from random import randint
import asyncio

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
            self.async_map(lambda codon: self.generateIndividual(), range(self.numberIndividuals)))
        self.pop=individuals
        return self.pop

    async def generateIndividual(self):
        individual = []
        for _ in range(self.individualSize):
            individual.append(randint(1,255))
        self.pop.append(individual)

        return individual

    def async_map(self,coroutine_func, iterable):
        loop = asyncio.get_event_loop()
        future = asyncio.gather(*(coroutine_func(param) for param in iterable))
        return loop.run_until_complete(future)