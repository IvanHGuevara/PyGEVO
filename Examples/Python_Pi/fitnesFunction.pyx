from math import sin,cos,log,tan,factorial,pi,fabs

import numpy as np


#dim=np.loadtxt("SampleData.txt",dtype=float)
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


def fitnesFunction(phenotype):

    puntaje=0
    #print(phenotype)
    acum=0
    for i in range(0,100):
        try:
            calc=eval(phenotype.lower())
            acum= acum+calc
            #print(str(acum)+" + "+str(calc))
            #if (pi-temp) >= (pi-calc) :
            #    temp=calc
        except:
            return 9999999999999999999999999999999999999999
    if pi == acum:
        return 0
    #print(temp)
    try:
        puntaje=fabs(pi-acum)
    except:
        puntaje=9999999999999999999999999999999999999999
    return puntaje

#"pdiv(pdiv(myadd(i, mymul(i, cos(cos(i)))), factorial(i)), i)"
#"pdiv(sin(factorial(i)), myadd(sin(factorial(i+1)), i))"  score=1017.4998165340455
#dim = np.loadtxt("SampleData.txt", dtype=float)
#num=fitnesFunction("pdiv(sin(factorial(i)), myadd(sin(factorial(i+1)), i))",dim)
#print(num)
