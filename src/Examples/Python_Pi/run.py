#from compiler import Compiler
#comp=Compiler()
#comp.enableCython()
#comp.compile()
import sys
sys.path.append('../../')
import Examples.Python_Pi.fitnessFunction as ff
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.searchOperators.gaCore import GA
from pathlib import Path
import pickle

import time

def processIndividual(ind, debug=True):
    if ind.isValid():
        score= ff.fitnessFunction(ind.phenotype)
        ind.fitness_score=score
        if score==0:
            print(ind.genotype)
            print(ind.phenotype)
            print(ind.fitness_score)
            print("Found it")
            time.sleep(60*60*10)
        else:
            score=999999999999999999999999999999999
            ind.fitness_score= score
        return score

def createPhenotypes():
    fileSave="data"
    fileObj = Path(fileSave)
    pop = Population("grammar.bnf", numberIndividuals=25, individualSize=25, fitness_function=processIndividual)
    if fileObj.is_file():
        try:
            f=open(fileSave , 'rb')
            population=pickle.loads(f.read())
            f.close()
        except:
            f.close()
            sys.exit()
        population = sorted(pop, key=lambda ind: (ind.fitness_score), reverse=False)
        population = GA.select(population, 0.05, 1000)
    else:
        population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_v1(population, populationFactory=pop, gen=1000, porcentSelect=0.5, fileSave=fileSave, reverse=False, debug=True, staticSelection=1000)
    inds=sorted(evolvedPop,key=lambda ind: ind.fitness_score, reverse=True)
    print("")
    ("Top mejores 20:")
    for ind in inds[0:20]:
        print(ind.genotype)
        print(ind.phenotype)
        print(ind.fitness_score)
        print("========================================================================================================")

createPhenotypes()