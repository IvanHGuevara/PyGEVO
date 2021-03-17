
import numpy as np
import sys
sys.setrecursionlimit(10000)
import time
import asyncio
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
            word=lineV[0].replace(" ","")
            if(word not in self.vWords):
                self.vWords.append(word)
            if len(lineV)!=2:
                print("Error line no se puede separar en 2 por el simbolo :=  lineV=",str(lineV))
            definitionsText = lineV[1]
            definitions = definitionsText.split("|")
            for definition in definitions:
                if (definition not in self.vDefinitions):
                    self.vDefinitions.append(definition)
        self.mBNF=np.full((len(lines),len(self.vDefinitions)),False,dtype=bool)
        #Carga de matriz
        for line in lines:
            lineV=line.split(":=")
            word = lineV[0].replace(" ","")
            definitions = lineV[1]
            definitions=definitions.split("|")
            #self.mBNF.append([0]*len(self.vDefinitions))
            indexWord=self.vWords.index(word)
            if indexWord==-1:
                print("Operador no encontrado indexWord="+word)

            for definition in definitions:
                #self.mBNF[self.vWords.index(word)][self.vDefinitions.index(definition)]=1
                self.mBNF[indexWord][self.vDefinitions.index(definition)]=True
    def mapBNF(self,individuals,start,debug):
        cdef int i
        cdef str search
        i = start

        cdef int p
        for individual in individuals:
            p = 0
            xPosibles = []
            for bit in self.mBNF[i]:
                if bit == True:
                    xPosibles.append(self.vDefinitions[p])
                p = p + 1
            cDefinitions = len(xPosibles)
            n=individual%cDefinitions
            #time.sleep(2)
            xDefinition=xPosibles[n]


            while len(individuals[1:])>=1 :
                if debug:
                    print(str(len(individuals))+"->"+str(individuals))
                pIni=xDefinition.find("<")
                pFin=xDefinition.find(">")+1

                search=xDefinition[pIni:pFin]
                #time.sleep(1)
                if debug:
                    print(xDefinition)
                if search in self.vWords:

                    if debug:
                        print("")
                        print("Position:"+str(start+1)+" IndividualNumber:"+str(individual)+" ->Definition:"+str(xDefinition)+" -->Select:"+str(n)+" --->Select-Non-Terminal:"+search )

                    mapA,ind=self.mapBNF(individuals[1:], self.vWords.index(search),debug)
                    xDefinition=xDefinition.replace(search,mapA,1)



                    if ind>0:
                        individuals=individuals[-ind:]
                    else:
                        individuals=np.random.randint(255, size=(0))

                else:

                    return xDefinition,len(individuals[1:])

            return xDefinition,0

