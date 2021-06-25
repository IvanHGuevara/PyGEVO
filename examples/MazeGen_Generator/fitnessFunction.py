import sys
sys.path.append('../../')
from Examples.MazeGen_Generator.ScenarioBuilder import ScenarioBuilder
import numpy as np

def square(width, coordinateX, coordinateY, composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createSquare(width, coordinateX, coordinateY)

def triangle(width, coordinateX, coordinateY, composedElement = None): 
  if composedElement != None:
    eval(composedElement)
  builder.createTriangle(width, coordinateX, coordinateY)

def lshape(width, coordinateX, coordinateY, composedElement = None):
  if composedElement != None:
    eval(composedElement)  
  builder.createLShape(width, coordinateX, coordinateY)

def eshape(width, coordinateX, coordinateY, coordinateZ, coordinateK, composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createEShape(width, coordinateX, coordinateY, coordinateZ, coordinateK)

  # We need to create an intermediate board where we draw the elements somehow, this way we 
  # calculate
def fitnessFunction(phenotype):
  eval(phenotype)
  value = builder.figureCounter
  builder.figureCounter = 0
  return value
    
builder = ScenarioBuilder()
