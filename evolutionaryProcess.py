from utils_.cythonFunctions import compileAll
compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms


pop = Population(numberIndividuals=1000, individualSize=1000)
population = pop.generatePop()
algo = Algorithms("grammar_ANSI_C.bnf")
evolvedPop = algo.evolveWithGE(population, gen=1,initBNF=56,debug=False)
print("Genotipos:\n")
for p in evolvedPop:
    print(p)
    print("")

