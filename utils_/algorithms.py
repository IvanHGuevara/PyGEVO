from utils_.cythonFunctions.mapper import Mapper
#from utils_.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
from utils_.general_functions import General_functions
from .search_operators.ga import GA

class Algorithms:

    def __init__(self, grammarPath,gen = 1, initBNF=1,debug=False) -> None:
        self.mapper = Mapper(GrammarWrapper(grammarPath))
        self.mapper.toMatrixBNF()
        self.gen=gen
        self.initBNF=initBNF
        self.debug=debug

    def evolveWithGE_(self, population, gen = 1, initBNF=1):
        evolvedIndividuals = []
        for _ in range(gen):
            for ind in population:
                ind.phenotype=self.mapper.mapBNF(ind,initBNF-1)
                evolvedIndividuals.append(ind)
        return evolvedIndividuals
        
    def evolveWithGE(self, population):
        generation=[]
        for _ in range(self.gen):
            evolvedIndividuals =  list(General_functions.async_map_g((lambda ind: self.mapper.mapBNF(ind.genotype,self.initBNF-1,debug=self.debug)[0]), population))
            for idx, ind in enumerate(population):
                ind.phenotype = evolvedIndividuals[idx]
        return population
