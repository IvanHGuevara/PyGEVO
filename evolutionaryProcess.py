from utils_.cythonFunctions import compileAll
compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA
pop = Population(numberIndividuals=6, individualSize=8)
population = pop.generatePop()
algo = Algorithms("grammar_ANSI_C.bnf",gen=1, initBNF=56,debug=False)
evolvedPop = algo.evolveWithGE(population)

print("")
print("POPULATION:")
for p in evolvedPop:
    print(list(p[0]))
    print(p[1])
    print(".............................................................................................................")

ga = GA(algo)
print("")
print("SELECT:")
selected=ga.select(evolvedPop,porcent=0.5,f_to_int=(lambda x: len(x)),reverse=False)
for p in selected:
    print(list(p[0]))
    print(p[1])
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

print("")
print("MUTATE:")
mutated=ga.mutate(selected)
for p in mutated:
    print(list(p[0]))
    print(p[1])
    print("-------------------------------------------------------------------------------------------------------------")

print("")
print("CROSSOVER:")
crossover=ga.crossover(mutated)
for p in crossover:
    print(list(p[0]))
    print(p[1])
    print("-------------------------------------------------------------------------------------------------------------")
