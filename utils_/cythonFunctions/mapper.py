class Mapper:

    def __init__(self, grammar) -> None:
        self.grammar = grammar
        self.lines = None
        self.vWords = []
        self.vDefinitions = []
        self.mBNF = []

    def toMatrixBNF(self):
        lines=self.grammar.getProductionRules()

        #Carga de vectores con reglas y definiciones
        for line in lines:
            line=line.split(":=")
            word=line[0]
            if(word not in self.vWords):
                self.vWords.append(word)
            definitions = line[1]
            definitions = definitions.split("|")
            for definition in definitions:
                if (definition not in self.vDefinitions):
                    self.vDefinitions.append(definition)
        #Carga de matriz
        for line in lines:
            line=line.split(":=")
            word = line[0]
            definitions = line[1]
            definitions=definitions.split("|")
            self.mBNF.append([0]*len(self.vDefinitions))
            for definition in definitions:
                self.mBNF[self.vWords.index(word)][self.vDefinitions.index(definition)]=1

    def mapBNF(self,individuals,start):
        i = start
        for individual in individuals:
            p = 0
            xPosibles = []
            for bit in self.mBNF[i]:
                if bit == 1:
                    xPosibles.append(self.vDefinitions[p])
                p = p + 1
            cDefinitions = len(xPosibles)
            n=individual%cDefinitions
            print(str(individual)+"->rest "+str(n)+"-->"+xPosibles[n])

            xDefinition=xPosibles[n]
            for search in self.vWords:
                if search in xDefinition:
                        start=self.vWords.index(search)
                        print(str(start)+" encontrado "+search)
                        xDefinition=xDefinition.replace(search,self.mapBNF(individuals[1:], start))

            return xDefinition

