import sys
from tkinter import PhotoImage
sys.path.append('../../')
from Examples.MazeGen_Generator.RealScenarioBuilder import RealScenarioBuilder
from cachetools import cached
import random

positions = [50, 100, 150, 200, 250, 300, 350, 400]
width = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def wall(wallType, composedElement = None):
  position = random.choice(positions)
  if composedElement != None:
    eval(composedElement)
  if wallType == 0:
    realbuilder.createHorizontalWall(position, position)
  else:
    realbuilder.createVerticalWall(position, position)

def cobot(composedElement = None): 
  position = random.choice(positions)
  if composedElement != None:
    eval(composedElement)
  realbuilder.createCobot(position)

def productionLine(composedElement = None):
  position = random.choice(positions)
  if composedElement != None:
    eval(composedElement)
  realbuilder.createProductionLine(position)

def router(composedElement = None):
  position = random.choice(positions)
  if composedElement != None:
    eval(composedElement)
  realbuilder.createRouter(position)


#
@cached(cache={})
def fitnessFunction(individual):
  value = 0
  try:
    realbuilder.addHeader()
    eval(individual.phenotype)
    value = realbuilder.calculateFitness()
    #print("Fitness score:", value)
    stringBuild = realbuilder.getStringBuild()
    #print("String build:", stringBuild)
    individual.stringBuild = stringBuild
    individual.fitness_score = value
  except:
    print("Invalido:", individual.phenotype)
    stringBuild = ""
    realbuilder.components = []
    realbuilder.stringBuild = ""
  return value, stringBuild
    
realbuilder = RealScenarioBuilder()
#value, stringBuild = fitnessFunction("productionLine(router(router(wall(0,wall(1,productionLine())))))")
#print(value)
#print(stringBuild)
