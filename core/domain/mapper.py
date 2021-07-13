
import numpy as np
import sys
sys.setrecursionlimit(10000)
class Mapper:

    def __init__(self, grammar) -> None:
        self.grammar = grammar
        self.mBNF = None

    def toMatrixBNF(self):
        # Loading vectors with rules and definitions
        self.mBNF=np.zeros((len(self.grammar.getVWords()),len(self.grammar.getProductionRules())))
        #Loading Matrix
        productionRules = self.grammar.getProductionRules()
        for idx, word in enumerate(self.grammar.getVWords()):
            productions = self.grammar.getProductionRulesFromWord(word)
            for production in productions:
                self.mBNF[idx][productionRules.index(production)]=1

    def mapBNF(self,codons,start = 1,debug = False):
        i = start
        for codon in codons:
            cDefinitions = len(self.grammar.getProductionRulesForPosition(i))
            n=codon%cDefinitions
            xDefinition=self.grammar.getProductionRulesForPosition(i)[n]
            while len(codons[1:])>=1 :
                if debug:
                    print(str(len(codons))+"->"+str(codons))
                pIni=xDefinition.find("<")
                pFin=xDefinition.find(">")+1
                search=xDefinition[pIni:pFin]
                if debug:
                    print(xDefinition)
                if search in self.grammar.getVWords():
                    if debug:
                        print("")
                        print("Position:"+str(start+1)+" IndividualNumber:"+str(codon)+" ->Definition:"+str(xDefinition)+" -->Select:"+str(n)+" --->Select-Non-Terminal:"+search )
                    mapA,ind=self.mapBNF(codons[1:], self.grammar.getVWords().index(search),debug)
                    xDefinition=xDefinition.replace(search,mapA,1)
                    if ind>0:
                        codons=codons[-ind:]
                    else:
                        codons=np.random.randint(255, size=(0))
                else:
                    return xDefinition,len(codons[1:])
            return xDefinition,0

