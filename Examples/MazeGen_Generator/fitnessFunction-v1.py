import sys
sys.path.append('../../')
from Examples.MazeGen_Generator.ScenarioBuilder import ScenarioBuilder
import random

width = [1,2,3,4,5,6,7,8]
number = [100,200,300,400,500,600,700,800]

def square(composedElement = None):
  if composedElement != None:
    eval(composedElement)
  builder.createSquare(random.choice(width), random.choice(number), random.choice(number))

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

  # We need to create an intermediate board where we draw the elements somehow, this way we 
  # calculate
def fitnessFunction(phenotype):
  eval(phenotype)
    
builder = ScenarioBuilder()
fitnessFunction("square(eshape(triangle()))")