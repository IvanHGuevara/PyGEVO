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


def fitnesFunction(phenotype,dim):

    puntaje=0
    #print(phenotype)
    temp=0
    #for i in range(0,len(dim)-1):
    for i in range(0,100):
        try:

            calc= temp+eval(phenotype.lower())
            if (pi-temp) >= (pi-calc) :
                temp=calc
                #print("i:"+str(i)+"-> "+str(temp))

            #print(temp)
        except:

            return 0
            #print(phenotype.lower())
            #print(str(i+1))

    puntaje=fabs(pi-temp)
    #print("puntaje:" +str(puntaje)+" solution="+str(temp))
    return puntaje

#"pdiv(pdiv(myadd(i, mymul(i, cos(cos(i)))), factorial(i)), i)"
#dim = np.loadtxt("SampleData.txt", dtype=float)
#num=fitnesFunction("pdiv(pdiv(myadd(i, mymul(i, cos(cos(i)))), factorial(i)), i)",dim) #score=16
