
import numpy as np
import sys
sys.setrecursionlimit(10000)

class Mapper:

    def __init__(self, grammar) -> None:
        self.grammar = grammar
        self.lines = None
        self.vWords = []
        self.vDefinitions = []
        self.mBNF = None

    def toMatrixBNF(self):
        lines=self.grammar.getProductionRules()
        cdef str word
        cdef str definitionsText
        cdef str definition
        cdef str line
        # Loading vectors with rules and definitions
        self.mBNF=np.zeros((self.grammar.getProductionRules(),self.grammar.getNumberDefinitions()))
        #Loading Matrix
        for line in lines:
            lineV=line.split(":=")
            word = lineV[0]
            definitions = lineV[1]
            definitions=definitions.split("|")
            #self.mBNF.append([0]*len(self.vDefinitions))
            indexWord=self.vWords.index(word)
            if indexWord==-1:
                print("Operator not found indexWord="+word)

            for definition in definitions:
                #self.mBNF[self.vWords.index(word)][self.vDefinitions.index(definition)]=1
                self.mBNF[indexWord][self.vDefinitions.index(definition)]=1
    def mapBNF(self,individuals,start):
        cdef int i
        cdef str search
        i = start
        cdef int p
        for codon in individuals:

            p = 0
            xPosibles = []
            for bit in self.mBNF[i]:
                if bit == 1:
                    xPosibles.append(self.vDefinitions[p])
                p = p + 1
            cDefinitions = len(xPosibles)
            n=codon%cDefinitions
            #print(str(codon)+"->rest "+str(n)+"-->"+xPosibles[n])

            xDefinition=xPosibles[n]
            for search in self.vWords:
                if search in xDefinition:
                        if self.vWords.count(search)>0:
                            start=self.vWords.index(search)
                            if start==-1:
                                print("Operator not found"+search)
                            if len(individuals[1:])>0:
                                    try:
                                        xDefinition=xDefinition.replace(search,self.mapBNF(individuals[1:], start)+" ")
                                    except MemoryError as error:
                                        # Output expected MemoryErrors.
                                        print(error)
                                        return xDefinition
                                    except Exception as exception:
                                        # Output unexpected Exceptions.
                                        print(exception, False)
                                        return xDefinition
                            else:
                                return xDefinition
            return xDefinition

