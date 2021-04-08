import sys
sys.path.append('../../')
from utils_.cythonFunctions import compileAll
import pyximport
pyximport.install()
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

def runPhenotype(phenotype):
    #define system
    system = platform.system()
    pathAnterior=os.getcwd()
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
    datos = list1.read() +str(phenotype)+list2.read()
    file.write(datos)
    file.close()

    fileLib = "GEClassify"
    #execute
    if system=="Linux":
        # Compile
        bashCommand = "gcc -pipe -o Build/" + fileName + " Build/" + fileName + ".c "+fileLib+".o -lm -Warray-bounds -Wmultichar"
        os.system(bashCommand)
        bashCommand = "./Build/"+fileName
    elif system=="Windows":
        # Compile
        bashCommand = "gcc -pipe -o Build//" + fileName + " Build//" + fileName + ".c "+fileLib+".exe -lm "
        os.system(bashCommand)
        bashCommand = "cd Build & "+fileName+".exe  & cd .."
    elif system=="Darwin":
        # Compile
        bashCommand = "gcc -pipe -o Build/" + fileName + " Build/" + fileName + ".c "+fileLib+".o -lm -Warray-bounds -Wmultichar"
        os.system(bashCommand)
        bashCommand = "./Build/"+fileName
    try:
        result = subprocess.check_output(bashCommand, shell=True)
        score=int(result)
        print("File:"+fileName +" Score:" + str(score))
        file = open("Build//"+fileName+"_out.txt", 'w')
        file.write(str(score))
        file.close()
        os.chdir(pathAnterior)
        os.remove("Build//" + fileName + ".c")
        if system=="Windows":
            os.remove("Build//"+fileName+".exe")
        elif system=="Linux":
            os.remove("Build//"+fileName+".o")
        elif system=="Darwin":
            os.remove("Build//"+fileName+".o")
    except:
        print("score did not dump in "+"Build/"+fileName+"_out.txt")
    return score

def prepareExperiment():
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
    os.system("mkdir Build")
    os.system("cd Build")
    fileLib="GEClassify"
    system = platform.system()
    #execute
    if system=="Linux":
        # Compile
        bashCommand = "gcc -Wall -Wextra -Wpedantic -g -o "+fileLib+".o -c "+fileLib+".c "
        os.system(bashCommand)
        shutil.copy("GEClassify.o", "Build/GEClassify.o")
    elif system=="Windows":
        # Compile
        bashCommand = "gcc -Wall -Wextra -Wpedantic -g -o "+fileLib+".exe -c "+fileLib+".c "
        os.system(bashCommand)
        shutil.copy("GEClassify.exe", "Build/GEClassify.exe")
    elif system=="Darwin":
        # Compile
        bashCommand = "gcc -Wall -Wextra -Wpedantic -g -o "+fileLib+".o -c "+fileLib+".c "
        os.system(bashCommand)
        shutil.copy("GEClassify.o", "Build/GEClassify.o")
    shutil.copy("GEClassify.h", "Build/GEClassify.h")
    shutil.copy("SampleData.txt", "Build/SampleData.txt")


def processIndividual(ind):
    #We check if the phenotype is valid by checking if there is a < or a >
    try:
        score=runPhenotype(ind.phenotype)
        if type(score) is int:
            return score
        else:
            return 0
    except:
        print("Invalid phenotype:" + ind.phenotype)
        print("Setting up fitness to zero...."+ "\n")
        return 0

def createPhenotypes():
    prepareExperiment()
    pop = Population(numberIndividuals=100, individualSize=8)
    population = pop.generatePop()
    algo = Algorithms("grammar.bnf", initBNF=1, debug=False)
    evolvedPop = algo.evolveWithGE_1(population, processIndividual, 4)
    inds=list(filter((lambda ind: ind.isValid()), evolvedPop))
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