from utils_.cythonFunctions.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
from utils_.general_functions import General_functions
class Algorithms:

    def __init__(self, grammarPath) -> None:
        self.mapper = Mapper(GrammarWrapper(grammarPath))
        self.mapper.toMatrixBNF()

    def evolveWithGE_(self, population, gen = 1, initBNF=1):
        evolvedIndividuals = []
        for _ in range(gen):
            for ind in population:
                phenotype=self.mapper.mapBNF(ind,initBNF-1)
                evolvedIndividuals.append(phenotype[0])
        return evolvedIndividuals
    def evolveWithGE(self, population, gen = 1, initBNF=1,debug=False):
        evolvedIndividuals = []
        for _ in range(gen):
            evolvedIndividuals = evolvedIndividuals + list(General_functions.async_map_g((lambda ind: self.mapper.mapBNF(ind,initBNF-1,debug=debug)[0]), population))
        return evolvedIndividuals
