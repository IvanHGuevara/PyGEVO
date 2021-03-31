from utils_.cythonFunctions import compileAll
# compileAll.compiler()
from utils_.cythonFunctions.population import Population
from utils_.algorithms import Algorithms
from utils_.search_operators.ga import GA
from utils_.general_functions import General_functions
from subprocess import call
import os
import platform
import time
import shutil
import subprocess

def runPhenotype(penotype):
    #define sistem
    system = platform.system()
    pathAnterior=os.getcwd()
    #path="Experiments/TestCompiler_ASIN_C/"
    #os.chdir(path)
    files=os.listdir('Build//')
    files=list(map(lambda file: int(file.replace("_out.txt","")),list(filter(lambda file: file.count("_out.txt"), files))))
    if len(files)>0:
        n=max(files)+1

    else:
        n=0
    fileName = ""+str(n)
    #File Creator

    file1 = "0_start.c"
    file2 = "1_end.c"
    list1 = open(file1, 'r')
    list2 = open(file2, 'r')
    file = open("Build//"+fileName+".c", 'w')
    datos = list1.read() +str(penotype)+list2.read()
    file.write(datos)
    file.close()

    fileLib = "GEClassify"
    #execute
    if system=="Linux":
        # Compile
        bashCommand = "gcc -pipe -o Build//" + fileName + " Build//" + fileName + ".c "+fileLib+".o -lm "
        os.system(bashCommand)

        bashCommand = "cd Build & "+fileName+".o  & cd .."
    elif system=="Windows":
        # Compile
        bashCommand = "gcc -pipe -o Build//" + fileName + " Build//" + fileName + ".c "+fileLib+".exe -lm "
        os.system(bashCommand)
        bashCommand = "cd Build & "+fileName+".exe  & cd .."
    elif system=="Darwin":
        # Compile
        bashCommand = "gcc -pipe -o Build//" + fileName + " Build//" + fileName + ".c "+fileLib+".o -lm "
        os.system(bashCommand)
        bashCommand = "cd Build & "+fileName+".o  & cd .."

    try:
        result = subprocess.check_output(bashCommand, shell=True)
        # result=os.system(bashCommand)
    except:
        print("score did not dump in "+"Build//"+fileName+"_out.txt")
    score=int(result)
    #porcentProgress=int(int(fileName)*100/int(lenPopulation))
    #print(fileName + "/"+str(lenPopulation)+" ->"+str(porcentProgress)+"% ->"+"Result_exect_Score: " + str(score))
    print("File:"+fileName +" Score:" + str(
        score))
    file = open("Build//"+fileName+"_out.txt", 'w')
    file.write(str(score))
    file.close()
    os.chdir(pathAnterior)
    os.remove("Build//" + fileName + ".c")
    os.remove("Build//"+fileName+".exe")
    return score
def preparateExperiment():
    #remove all files Build
    try:
        if os.path.isdir("Build"):
            shutil.rmtree("Build")
            time.sleep(1)
        else:
            time.sleep(1)
            os.mkdir('Build')
    except:
        if os.path.isdir("Build"):
            time.sleep(1)
            shutil.rmtree("Build")
        else:
            time.sleep(1)
            os.mkdir('Build')

        print("Warning shutil.rmtree(Build)")

    #compile libs
    fileLib="GEClassify"
    bashCommand = "gcc -Wall -Wextra -Wpedantic -g -o "+fileLib+".exe -c "+fileLib+".c "
    os.system(bashCommand)
    #copy data
    time.sleep(1)
    fuente = "SampleData.txt"
    destino = "Build//SampleData.txt"
    shutil.copyfile(fuente, destino)
    fuente = "GEClassify.c"
    destino = "Build//GEClassify.c"
    shutil.copyfile(fuente, destino)
    fuente = "GEClassify.c"
    destino = "Build//GEClassify.c"
    shutil.copyfile(fuente, destino)
    fuente = "GEClassify.h"
    destino = "Build//GEClassify.h"
    shutil.copyfile(fuente, destino)
    fuente = "GEClassify.exe"
    destino = "Build//GEClassify.exe"
    shutil.copyfile(fuente, destino)

def prossesIndividue(ind):
    print(ind.genotype)
    print(ind.phenotype)
    if str(ind.phenotype).count("<")==0 and str(ind.phenotype).count(">")==0:
        try:
            score=runPhenotype(ind.phenotype)

            if type(score) is int:
                ind.fitness_score=score
            else:
                ind.fitness_score = 0
        except:
            print("Error de formato de phenotype  en forma de tupla")
            ind.fitness_score = 0
    else:
        ind.fitness_score = 0
    #print(ind.fitness_score)
    print("----------------------------------------------------------------------------------------------------------")
    return ind
def createPhenotypes():
    preparateExperiment()
    pop = Population(numberIndividuals=100, individualSize=20)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", gen=5, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_FitnesFunction(population, prossesIndividue,4,porcent=0.2)
    lenPopulation=len(evolvedPop)
    #General_functions.async_map_g((lambda ind: prossesIndividue(ind[1],ind[0],lenPopulation)), enumerate(evolvedPop))
    #for ind in evolvedPop:
    inds=list(filter((lambda ind: ind.phenotype[0].count("<")==0), evolvedPop))
    inds=sorted(inds,
           key=lambda ind: ind.fitness_score, reverse=True)
    print("")
    print("Top mejores 20:")
    for ind in inds[0:20] :
        print(ind.genotype)
        print(ind.phenotype)
        print(ind.fitness_score)
        print("========================================================================================================")
createPhenotypes()