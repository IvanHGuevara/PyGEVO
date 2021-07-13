import sys
sys.path.append('../../')
from Examples.MazeGen_Generator.ScenarioBuilder import ScenarioBuilder
from cachetools import cached
import random

width = [1,2,3,4,5,6,7,8]
number = [100,200,300,400,500,600,700,800,900,1000,1100]

def square(composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createSquare(random.choice(number), random.choice(number), random.choice(number))

def triangle(composedElement = None): 
  if composedElement != None:
    eval(composedElement)
  builder.createSquare(random.choice(width), random.choice(number), random.choice(number))

def lshape(composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createLShape(random.choice(width), random.choice(number), random.choice(number))

def eshape(composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createEShape(random.choice(width), random.choice(number), random.choice(number), random.choice(number), random.choice(number))

@cached(cache={})
def fitnessFunction(phenotype):
  try:
    builder.addHeader()
    eval(phenotype)
    value = builder.figureCounter
    stringBuild = builder.stringBuild
  except:
    value = 0
    stringBuild = ""
  builder.figureCounter = 0
  builder.stringBuild = ""
  return value, stringBuild
    
builder = ScenarioBuilder()
