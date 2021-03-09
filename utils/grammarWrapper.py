import string
import random
from parsimonious.grammar import Grammar

from pathlib import Path

class GrammarWrapper:
    def __init__(self, grammarFile) -> None:
        grammarText = Path(grammarFile).read_text()
        self.grammar = Grammar(grammarText)
    
    def getProductionRules(self):
        return list(self.grammar.values())
    
    def getDivisor(self):
        return len(self.getProductionRules())

    def getProductionRule(self, number):
        return self.getProductionRules()[number]

    def generateCompliantRandomProductionLine(self, number):
        productionLine = self.getProductionRule(number)
        #We should generate the random string based on the grammar
        str = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(random.randint(1,8)))
        while(productionLine.parse(str).text is None):
            str = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(random.randint(1,8)))
        return str
        