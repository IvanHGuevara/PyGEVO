from compiler import Compiler
comp=Compiler()
#comp.enableCython()
comp.compile()
import sys
import Examples.Python_Pi.fitnesFunction as ff
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA
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
    fileSave="data_1"
    fileObj = Path(fileSave + '.txt')
    pop = Population("grammar.bnf", numberIndividuals=25, individualSize=18, fitness_function=prossesIndividue)
    if fileObj.is_file():
        try:
            f=open(fileSave + '.txt', 'rb')

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

    evolvedPop = algo.evolveWithGE(population, populationFactory=pop,gen=100000,porcentSelect=0.5,fileSave=fileSave,reverse=False,debug=True,staticSelection=10000)#,staticSelection=200


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