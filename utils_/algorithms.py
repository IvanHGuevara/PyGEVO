from utils_.cythonFunctions.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper

class Algorithms:

    def __init__(self, grammarPath) -> None:
        self.mapper = Mapper(GrammarWrapper(grammarPath))
        self.mapper.toMatrixBNF()

    def evolveWithGE(self, population, gen = 1,initBNF=1,debug=False):
        evolvedIndividuals = []
        for _ in range(gen):
            for ind in population:
                phenotype=self.mapper.mapBNF(ind,initBNF-1,debug).replace(" ","").replace("<"," <").replace(">","> ").replace(" < =","<=").replace(" > ="," >=").replace(" < <","<<").replace(" > >"," >= ")
                evolvedIndividuals.append(phenotype)
        return evolvedIndividuals
