from compiler import Compiler
comp=Compiler()
#comp.enableCython()
comp.compile()
import sys
import Examples.Python_Pi.fitnesFunction as ff
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA
from pathlib import Path
import pickle

phenotypeScore={}

def prossesIndividue(ind, debug=True):
    #print(ind.genotype)
    scoreDic=phenotypeScore.get(ind.phenotype,-1)
    if scoreDic==-1:
        if ind.phenotype.count("<") == 0:

            score= ff.fitnesFunction(ind.phenotype)

            if ind.fitness_score==-1:
                #time.sleep(10)
                print("Error raro -1")
            else:
                ind.fitness_score=score
                phenotypeScore[ind.phenotype]=score
        else:
            score=999999999999999999999999999999999
            ind.fitness_score= score
            phenotypeScore[ind.phenotype] = score
        return score
    else:
        return scoreDic
def createPhenotypes():
    fileSave="data_1"
    fileObj = Path(fileSave + '.txt')
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
        pop = Population(numberIndividuals=25, individualSize=18)
        population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)

    evolvedPop = algo.evolveWithGE(population, prossesIndividue,gen=1000,porcentSelect=0.1,fileSave=fileSave,reverse=False,debug=True)#,staticSelection=200


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