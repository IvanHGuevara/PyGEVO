
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
    for i in range(0,len(dim)):
        try:
            temp= eval(phenotype.lower())
            if temp == dim[i]:
                puntaje = puntaje + 1
        except:
            return puntaje
    return puntaje

#dim = np.loadtxt("SampleData.txt", dtype=float)
#num=fitnesFunction("cos(log(Dim[5][i]))",dim) #score=16
#print(num)