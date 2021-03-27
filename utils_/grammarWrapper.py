from pathlib import Path

class GrammarWrapper:

    def __init__(self, grammarText) -> None:
        self.grammar = grammarText
        self.generateAndPrecalculateGrammarComponents()

    @classmethod
    def createFromFile(cls, grammarFile):
        grammarText = Path(grammarFile).read_text()
        return cls(grammarText) 
    
    @classmethod
    def createFromString(cls, stringText):
        return cls(stringText) 

    def generateAndPrecalculateGrammarComponents(self):
        self.grammarDict = {}
        self.productionRules = self.grammar.split("\n")
        for rule in self.productionRules:
            rule = rule.split(":=")
            # We use strip() because the BNF grammar contains whitespaces
            productions = list(map(lambda x: x.strip(), rule[1:][0].split("|")))
            # We use strip() because the BNF grammar contains whitespaces
            self.grammarDict[rule[0].strip()] = productions
        self.VWords = list(map(lambda x: x.strip(), self.grammarDict.keys()))
        self.productionRulesList = list(self.grammarDict.values())
    
    def getProductionRulesFromWord(self, word):
        return self.grammarDict[word]

    def getVWords(self):
        return self.VWords
        
    def getProductionRules(self):
        return sum(self.productionRulesList,[])

    def getProductionRulesForPosition(self, position):
        return self.productionRulesList[position]
