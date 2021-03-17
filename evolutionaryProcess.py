from utils_.cythonFunctions import compileAll
compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms


pop = Population(numberIndividuals=1, individualSize=10000)
population = pop.generatePop()
algo = Algorithms("grammar_1.bnf")
print("\nGenotipos:")
evolvedPop = algo.evolveWithGE(population, gen=1,initBNF=1,debug=False)
for p in evolvedPop:
    print("")
    print(p)


