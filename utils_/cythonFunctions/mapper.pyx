
import numpy as np


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
        #Carga de vectores con reglas y definiciones
        for line in lines:
            lineV=line.split(":=")
            word=lineV[0]
            if(word not in self.vWords):
                self.vWords.append(word)
            definitionsText = lineV[1]
            definitions = definitionsText.split("|")
            for definition in definitions:
                if (definition not in self.vDefinitions):
                    self.vDefinitions.append(definition)
        self.mBNF=np.zeros((len(lines),len(self.vDefinitions)))
        #Carga de matriz
        for line in lines:
            lineV=line.split(":=")
            word = lineV[0]
            definitions = lineV[1]
            definitions=definitions.split("|")
            #self.mBNF.append([0]*len(self.vDefinitions))
            indexWord=self.vWords.index(word)
            for definition in definitions:
                #self.mBNF[self.vWords.index(word)][self.vDefinitions.index(definition)]=1
                self.mBNF[indexWord][self.vDefinitions.index(definition)]=1
    def mapBNF(self,individuals,start):
        cdef int i
        cdef str search
        i = start
        cdef int p
        for individual in individuals:

            p = 0
            xPosibles = []
            for bit in self.mBNF[i]:
                if bit == 1:
                    xPosibles.append(self.vDefinitions[p])
                p = p + 1
            cDefinitions = len(xPosibles)
            n=individual%cDefinitions
            #print(str(individual)+"->rest "+str(n)+"-->"+xPosibles[n])

            xDefinition=xPosibles[n]
            for search in self.vWords:
                if search in xDefinition:
                        if self.vWords.count(search)>0:
                            start=self.vWords.index(search)
                            #print(str(start)+" encontrado "+search)
                            xDefinition=xDefinition.replace(search,self.mapBNF(individuals[1:], start))
            return xDefinition

