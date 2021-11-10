from compiler import Compiler

comp=Compiler()
#comp.enableCython()
comp.compile()

from core.domain.population import Population
from core.domain.algorithms import Algorithms
import numpy as np
import examples.Python_PrimesN.fitnesFunction as ff


def processIndividual(ind, debug=True):
    if ind.isValid():
        dim = np.loadtxt("SampleData.txt", dtype=float)
        score= ff.fitnesFunction(ind.phenotype,dim)
        if ind.fitness_score==-1:
            print("Unknown error")
        else:
            ind.fitness_score=score
    else:
        ind.fitness_score= 0

    #if debug:



        #porcentProgress = int(int(i) * 100 / int(lenPopulation))
        #print(str(i) + "/" + str(lenPopulation) + " ->" + str(porcentProgress) + "% ->" + "Result_exect_Score: " + str(
        #    ind.fitness_score))
        #print("----------------------------------------------------------------------------------------------------------")
    return ind.fitness_score
def createPhenotypes():
    fileSave="data"
    grammar="grammar.bnf"
    pop = Population(grammar, numberIndividuals=1000, individualSize=50, fitness_function=processIndividual)
    population = pop.generatePop()

    algo = Algorithms(grammar, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE(population, populationFactory=pop,gen=10000,porcentSelect=0.5,fileSave=fileSave,reverse=True,debug=True,staticSelection=1000,noDuplicates=True,cacheScore=True)


    inds = list(filter((lambda ind: ind.phenotype[0].count("<") == 0), evolvedPop))
    inds=sorted(inds,key=lambda ind: ind.fitness_score, reverse=True)
    print("")
    print("Top mejores 20:")
    for ind in inds[0:20]:
        print(ind.genotype)
        print(ind.phenotype)
        print(ind.fitness_score)
        print("========================================================================================================")
createPhenotypes()