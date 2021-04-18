#from random import randint
#from utils_.general_functions import General_functions
import numpy as np
from .Individual import Individual
from utils_.cythonFunctions.mapper import Mapper
#from utils_.mapper import Mapper
from utils_.grammarWrapper import GrammarWrapper
class Population:

    def __init__(self, grammarPath,numberIndividuals, individualSize = 5,fitness_function=None) -> None:

        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
        self.mapper = Mapper(GrammarWrapper.createFromFile(grammarPath))
        self.phenotypeScore={}
        self.fitness_function=fitness_function

    #def generatePop_(self):
    #    General_functions.async_map(lambda _: self.generateIndividual(), range(self.numberIndividuals))
    #    return self.pop

    def generatePop(self):
        individuals = []
        self.pop = np.random.randint(255, size=(self.numberIndividuals,self.individualSize))
        for genotype in self.pop:
            ind = Individual()
            ind.genotype = genotype
            ind.phenotype = self.mapper.mapBNF(ind.genotype, 0)[0]
            if self.fitness_function is not None:
                scoreDic = self.phenotypeScore.get(ind.phenotype, (-1,False))

                if scoreDic[0]==-1:
                    score=self.fitness_function(ind)
                    ind.fitness_score=score
                    self.phenotypeScore[ind.phenotype] = (score,False)
                else:
                    ind.fitness_score=scoreDic[0]
            individuals.append(ind)

        return individuals
    def recalculate_(self,inds,noDuplicates=False,cacheScore=True):
        #scoreDic {(score,isRepit)}
        for clave in self.phenotypeScore.keys():
            self.phenotypeScore[clave] = (self.phenotypeScore.get(clave, (-1, False))[0], False)
        indsNew=[]

        for ind in inds:
            ind.phenotype=self.mapper.mapBNF(ind.genotype, 0)[0]

            if self.fitness_function is not None:
                if cacheScore:
                    scoreDic = self.phenotypeScore.get(ind.phenotype, (-1,False))
                else:
                    scoreDic=(-1, False)
                #Control duplicates
                if noDuplicates:
                    #Control Cache
                    if scoreDic[1]==False :
                        if scoreDic[0]==-1:
                            score=self.fitness_function(ind)
                            ind.fitness_score=score

                            self.phenotypeScore[ind.phenotype] = (score, True)
                        else:
                            ind.fitness_score=scoreDic[0]
                            self.phenotypeScore[ind.phenotype] = (scoreDic[0], True)
                        indsNew.append(ind)

                elif not noDuplicates:
                    #Control Cache
                    if scoreDic[0]==-1:
                        score=self.fitness_function(ind)
                        ind.fitness_score=score
                        if cacheScore:
                            self.phenotypeScore[ind.phenotype] = (score, True)
                    else:
                        ind.fitness_score=scoreDic[0]
                        if cacheScore:
                            self.phenotypeScore[ind.phenotype] = (scoreDic[0], True)
                    indsNew.append(ind)
        return indsNew

    def recalculate(self,inds,noDuplicates=False,cacheScore=True):
        #scoreDic {(score,isRepit)}

        indsNew=[]

        #se inicia variable de repeticion
        for phenotype in self.phenotypeScore.keys():
            #guardo en diccionario
            self.phenotypeScore[phenotype] = (self.phenotypeScore[phenotype][0], False)
        #if noDuplicates:
        #    inds=inds.tolist()

        for ind in inds:

            # se genera los nuevos phenotipos
            ind.phenotype = self.mapper.mapBNF(ind.genotype, 0)[0]

            tuple=self.phenotypeScore.get(ind.phenotype, (None, False))


            # -1 -> no se encontro en cache
            if tuple[0] is None:
                ind.fitness_score = self.fitness_function(ind)
            else:
                ind.fitness_score = tuple[0]

            if cacheScore:
                self.phenotypeScore[ind.phenotype] = (ind.fitness_score, True)

            if noDuplicates and not tuple[1]:
                indsNew.append(ind)
                continue

        if noDuplicates:
            return np.array(indsNew)
        else:
            return inds

