from utils_.cythonFunctions.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
from utils_.general_functions import General_functions
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
                phenotype=self.mapper.mapBNF(ind,initBNF-1)
                evolvedIndividuals.append(phenotype[0])
        return evolvedIndividuals
    def evolveWithGE(self, population):
        generation=[]
        for _ in range(self.gen):

            evolvedIndividuals =  list(General_functions.async_map_g((lambda ind: self.mapper.mapBNF(ind,self.initBNF-1,debug=self.debug)[0]), population))
            generation=generation+[x for x in zip(population, evolvedIndividuals)]
        return generation
