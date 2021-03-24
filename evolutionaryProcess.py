from utils_.cythonFunctions import compileAll
#compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA

pop = Population(numberIndividuals=10, individualSize=8)
population = pop.generatePop()
algo = Algorithms("grammar_ANSI_C.bnf",gen=1, initBNF=56,debug=False)
evolvedPop = algo.evolveWithGE(population)
print("")
print("POPULATION:")
for p in evolvedPop:
    print(p.genotype)
    print(p.phenotype)
    print(".............................................................................................................")

ga = GA(algo)
print("")
print("SELECT:")
selected=ga.select(evolvedPop,porcent=0.5,f_to_int=(lambda x: len(x.genotype)),reverse=False)
for p in selected:
    print(p.genotype)
    print(p.phenotype)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print("")
print("MUTATE:")
mutated=ga.mutate(selected)
for p in mutated:
    print(p.genotype)
    print(p.phenotype)
    print("-------------------------------------------------------------------------------------------------------------")

print("")
print("CROSSOVER:",end="")
crossover=ga.crossover(mutated)
for p in crossover:
    print(p.genotype)
    print(p.phenotype)
    print("-------------------------------------------------------------------------------------------------------------")
