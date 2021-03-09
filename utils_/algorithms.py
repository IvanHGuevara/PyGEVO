from utils_.general_functions import General_functions
class Algorithms:

    def __init__(self, grammar) -> None:
        self.grammar = grammar

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

