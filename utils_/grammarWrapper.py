from pathlib import Path

class GrammarWrapper:
    def __init__(self, grammarFile) -> None:
        grammarText = Path(grammarFile).read_text()
        self.grammar = grammarText
        self.generateGrammarComponents()

    def generateGrammarComponents(self):
        self.grammarDict = {}
        self.productionRules = self.grammar.split("\n")
        for rule in self.productionRules:
            rule = rule.split(":=")
            # We use strip() because the BNF grammar contains whitespaces
            productions = list(map(lambda x: x.strip(), rule[1:][0].split("|")))
            # We use strip() because the BNF grammar contains whitespaces
            self.grammarDict[rule[0].strip()] = productions
    
    def getDivisor(self):
        return len(self.getProductionRules())
    
    def getProductionRulesFromWord(self, word):
        return self.grammarDict[word]

    def getVWords(self):
        return list(map(lambda x: x.strip(), self.grammarDict.keys()))

    def getProductionRules(self):
        return sum(list(self.grammarDict.values()),[])

    def getProductionRulesForPosition(self, position):
        return list(self.grammarDict.values())[position]
