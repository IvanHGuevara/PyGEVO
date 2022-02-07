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

def fitnesFunction(phenotype,dim):
    evolved = np.zeros(len(dim), dtype=float)
    for i in range(0,len(dim)):
        print(dim[i][5])
        try:
            temp= eval(phenotype.lower())
        except:
            temp=0
        if temp < 0 and dim[i][-1] == 0:
            evolved[i]=1
        elif temp > 0 and dim[i][-1] == 1:
            evolved[i]=1

        else:
            evolved[i]=0
    return assignFitness(evolved,dim)


dim = np.loadtxt("SampleData.txt", dtype=float)
num=fitnesFunction("cos(log(Dim[i][5]))",dim) #score=16
print(num)