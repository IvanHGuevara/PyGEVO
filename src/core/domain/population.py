from cachetools import cached, LRUCache
import numpy as np
from .Individual import Individual
from .mapper import Mapper
from .grammarWrapper import GrammarWrapper


class Population:

    def __init__(self, grammarPath, numberIndividuals, individualSize = 5,fitness_function=None) -> None:
        self.numberIndividuals = numberIndividuals
        self.individualSize = individualSize
        self.pop = []
        self.mapper = Mapper(GrammarWrapper.createFromFile(grammarPath))
        self.phenotypeScore={}
        self.fitness_function=fitness_function

    def generatePop(self):
        individuals = []
        self.pop = np.random.randint(255, size=(self.numberIndividuals,self.individualSize))
        for genotype in self.pop:
            ind = Individual()
            ind.genotype = genotype
            ind.phenotype = self.mapper.mapBNF(ind.genotype, 0)[0]
            if self.fitness_function is not None:
                scoreDic = self.phenotypeScore.get(ind.phenotype, (-1,False,0))
                if scoreDic[0]==-1:
                    score=self.fitness_function(ind)
                    ind.fitness_score=score
                    self.phenotypeScore[ind.phenotype] = (score,False,0)
                else:
                    ind.fitness_score=scoreDic[0]
            individuals.append(ind)

        return individuals


    def recalculate(self,inds,noDuplicates=True,cacheScore=True,maxCacheInactiveItem=4):
        #scoreDic {(score,isRepit)}
        countMatch=0
        countFail=0
        indsNew=[]

        #se inicia variable de repeticion
        for phenotype in self.phenotypeScore.keys():
            #guardo en diccionario
            item=self.phenotypeScore[phenotype]
            self.phenotypeScore[phenotype] = (item[0], False,item[2])
        #if noDuplicates:
        #    inds=inds.tolist()

        for ind in inds:

            # se genera los nuevos phenotipos
            ind.phenotype = self.mapper.mapBNF(ind.genotype, 0)[0]

            tuple=self.phenotypeScore.get(ind.phenotype, (None, False, 0))

            #(score, inCache,use)
            # (None, inCache,use) -> no se encontro en cache
            if tuple[0] is None:
                countFail=countFail+1
                ind.fitness_score = self.fitness_function(ind)

            else:
                countMatch=countMatch+1
                ind.fitness_score = tuple[0]
            if cacheScore:
                self.phenotypeScore[ind.phenotype] = (ind.fitness_score, True, 1)

            # control de duplicados
            if noDuplicates and not tuple[1]:
                indsNew.append(ind)
                continue


        tamCacheAnt=len(self.phenotypeScore)
        if cacheScore:
            #se elimina de cache si no se utilizo dos veces seguidas
            for phenotype in list(self.phenotypeScore.keys()):
                if phenotype not in list(map(lambda ind : ind.phenotype,inds)):
                    item = self.phenotypeScore[phenotype]
                    if item[2]>=-maxCacheInactiveItem:
                        self.phenotypeScore[phenotype]=(item[0], False,item[2]-1)
                    else:
                        self.phenotypeScore.pop(phenotype, None)
                else:
                    item = self.phenotypeScore[phenotype]
                    if item[2] <= maxCacheInactiveItem:
                        self.phenotypeScore[phenotype] = (item[0], False, 0)
        print("Size Cache:"+str(len(self.phenotypeScore))+" countMatch:"+str(countMatch)+" countFail:"+str(countFail)+" Performance:"+str(round(100*countMatch/(countMatch+countFail+1),2))+" Deleted:"+str(tamCacheAnt-len(self.phenotypeScore)))
        if noDuplicates:
            return np.array(indsNew)
        else:
            return inds
    
    @cached(cache=LRUCache(maxsize=500))
    def getPhenotype(self, ind):
        return self.phenotypeScore.get(ind.phenotype, (None, False, 0))
   
    def recalculate_v1(self, inds):
        for ind in inds:
            # We generate new phenotypes
            ind.phenotype = self.mapper.mapBNF(ind.genotype, 0)[0]
            tuple=self.getPhenotype(ind)
            if tuple[0] is None:
                ind.fitness_score = self.fitness_function(ind)
            else:
                ind.fitness_score = tuple[0]
        return inds