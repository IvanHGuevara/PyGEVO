from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA

pop = Population(numberIndividuals=6, individualSize=8)
population = pop.generatePop()
algo = Algorithms("grammar_ANSI_C.bnf",gen=5, initBNF=56,debug=False)
evolvedPop = algo.evolveWithGE_(population, 3)
for ind in evolvedPop:
    print(ind.genotype)
    print(ind.phenotype)
    print(ind.fitness_score)
"""print("")
print("POPULATION:")
for p in evolvedPop:
    print(p.genotype)
    print(p.phenotype)
    print(".............................................................................................................")

print("")
print("SELECT:")
selected=GA.select(evolvedPop,porcent=0.5,f_to_int=(lambda x: len(x.genotype)),reverse=False)
for p in selected:
    print(p.genotype)
    print(p.phenotype)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print("")
print("MUTATE:")
mutated=GA.mutate(selected, algo)
for p in mutated:
    print(p.genotype)
    print(p.phenotype)
    print("-------------------------------------------------------------------------------------------------------------")

print("")
print("CROSSOVER:",end="")
crossover=GA.crossover(mutated, algo)
for p in crossover:
    print(p.genotype)
    print(p.phenotype)
    print("-------------------------------------------------------------------------------------------------------------")"""
