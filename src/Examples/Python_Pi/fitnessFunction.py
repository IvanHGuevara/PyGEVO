from math import pi,fabs

import numpy as np

def assignFitness(evolved,dim):
  sum=0
  for i in range(0,len(dim)):
    sum =sum + evolved[i]
  return sum

def if_cond(exp1,exp2,exp3,exp4):
  if exp1 <= exp2:
    return exp3
  else:
    return exp4

def pdiv(a1,a2):
  if a2 == 0:
    return 0
  else:
    return a1/a2

def myadd(a1,a2):
  return a1+a2

def mysub(a1,a2):
  return a1-a2

def mymul(a1,a2):
  return a1*a2

def fitnessFunction(phenotype):
    puntaje=0
    acum=0
    for i in range(0,150):
        try:
            calc=eval(phenotype.lower())
            if abs(pi-acum) >= abs(pi-(acum + calc)) :
                acum = acum + calc
            else:
                return 9999999999999999999999999999999999999999
        except:
            return 9999999999999999999999999999999999999999
    if pi == acum:
        return 0
    try:
        puntaje=fabs(pi-acum)
    except:
        puntaje=9999999999999999999999999999999999999999
    return puntaje