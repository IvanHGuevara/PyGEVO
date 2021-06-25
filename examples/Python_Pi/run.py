from compiler import Compiler
comp=Compiler()
#comp.enableCython()
comp.compile()
import sys
import examples.Python_Pi.fitnesFunction as ff
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.searchOperators.gaCore import GA
from pathlib import Path
import pickle

import time

def prossesIndividue(ind, debug=True):
    #print(ind.genotype)


        if ind.phenotype.count("<") == 0:

            score= ff.fitnesFunction(ind.phenotype)

            ind.fitness_score=score
            if score==0:
                print(ind.genotype)
                print(ind.phenotype)
                print(ind.fitness_score)
                print("Lo encontroooooooooooooooooooooooooooooooooooo")
                time.sleep(60*60*10)
        else:
            score=999999999999999999999999999999999
            ind.fitness_score= score

        return score

def createPhenotypes():
    fileSave="data"
    fileObj = Path(fileSave )
    pop = Population("grammar.bnf", numberIndividuals=25, individualSize=25, fitness_function=prossesIndividue)
    if fileObj.is_file():
        try:
            f=open(fileSave , 'rb')

            population=pickle.loads(f.read())
            f.close()
        except:
            f.close()
            sys.exit()
        #print(pop[0].phenotype)
        #pop = load(fileSave + '.txt',allow_pickle=True)
        evolvedIndividuals=[]

        #for ind in population:

        #    evolvedIndividuals.append(ind)
        #population=evolvedIndividuals
        population = sorted(population, key=lambda ind: (ind.fitness_score), reverse=False)
        population = GA.select(population, 0.05, 10000)
    else:

        population = pop.generatePop()
        print(population)
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)

    evolvedPop = algo.evolveWithGE(population, populationFactory=pop,gen=10000,porcentSelect=0.5,fileSave=fileSave,reverse=False,debug=True,staticSelection=1000,noDuplicates=True,cacheScore=True)#,staticSelection=200


    #inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
    #inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
    #print("")
    #("Top mejores 20:")
    #for ind in inds[0:20]:
    #    print(ind.genotype)
    #    print(ind.phenotype)
    #    print(ind.fitness_score)
    #    print("========================================================================================================")
createPhenotypes()