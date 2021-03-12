from utils_.general_functions import General_functions
from utils_.cythonFunctions import maper
class Algorithms:

    def __init__(self, grammar) -> None:
         self.grammar= grammar

    def evolveWithGE(self, population, gen = 10):
        #[84, 98, 141, 234, 156, 92, 202, 156] ==> Population
        evolvedIndividuals = []
        divisor = self.grammar.getDivisor()
        for _ in range(gen):
            for ind in population:
                #evolvedInd = list(map(lambda codon: self.grammar.generateCompliantRandomProductionLine(codon % divisor) , ind))
                evolvedInd = list(
                    General_functions.async_map(lambda codon: self.grammar.generateCompliantRandomProductionLine(codon % divisor), ind))
                evolvedIndividuals.append(evolvedInd)
        return evolvedIndividuals
    def evolveWithGE_v2(self, population, gen = 10):
        evolvedIndividuals=[]
        f = open(self.grammar, 'r')
        bnf = f.read()
        #print(bnf)
        f.close()
        for individue in population:
            y, x, m = maper.toMatrixBNF(bnf)
            #print(" ")
            try:
                penotype = maper.mapBNF(bnf, individue, 0, y, x, m)
            except:
                penotype=None
            #print(" ")
            #print(evolvedIndividuals)
            evolvedIndividuals.append(penotype)

        return evolvedIndividuals

