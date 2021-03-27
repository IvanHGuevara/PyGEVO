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

def runPhenotype(penotype,n):
    #define sistem
    system = platform.system()
    pathAnterior=os.getcwd()
    #path="Experiments/TestCompiler_ASIN_C/"
    #os.chdir(path)

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
    score=str(int(result))
    print("Result_exect_Score " + fileName + ": " + score)
    file = open("Build//"+fileName+"_out.txt", 'w')
    file.write(score)
    file.close()
    os.chdir(pathAnterior)
def preparateExperiment():
    #remove all files Build
    try:
        shutil.rm("Build")
        os.mkdir('Build')
    except:
        os.mkdir('Build')
        print("Warning shutil.rmtree(Build)")

    #compile libs
    fileLib="GEClassify"
    bashCommand = "gcc -Wall -Wextra -Wpedantic -g -o "+fileLib+".exe -c "+fileLib+".c "
    os.system(bashCommand)
    #copy data
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

def prossesIndividue(ind,i):
    print(ind.genotype)
    print(ind.phenotype)
    print(ind.fitness_score)
    if str(ind.phenotype).count("<")==0 and str(ind.phenotype).count(">")==0:
        runPhenotype(ind.phenotype,i)
    print("----------------------------------------------------------------------------------------------------------")

def createPhenotypes():
    preparateExperiment()
    pop = Population(numberIndividuals=6, individualSize=100)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", gen=5, initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_(population, 3)

    General_functions.async_map_g((lambda ind: prossesIndividue(ind[1],ind[0])), enumerate(evolvedPop))
    #for ind in evolvedPop:

createPhenotypes()