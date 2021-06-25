import math
import numpy as np

class FitnessFunctions:

    @staticmethod
    def griewangk(ind):
        return 1. + sum(( (x ** 2.) / 4000. for x in ind.genotype)) - np.prod(list((math.cos(ind.genotype[i] / math.sqrt(i+1.)) for i in range(len(ind.genotype)))))

    @staticmethod
    def ackley(ind, a=20., b=0.2, c=2.*math.pi):
        return - a * math.exp(-b * math.sqrt(1./len(ind) * sum((x**2. for x in ind)) )) - math.exp(1./len(ind.genotype) * sum((math.cos(c*ind.genotype[i]) for i in range(len(ind.genotype)) )) ) + a + math.exp(1.),

    @staticmethod
    def zakharov(ind):
        return  sum((x**2. for x in ind)) + \
                sum(( 0.5 * float(i) * ind.genotype[i] for i in range(len(ind.genotype)) ))**2. + \
                sum(( 0.5 * float(i) * ind.genotype[i] for i in range(len(ind.genotype)) ))**4.
    @staticmethod
    def michalewicz(ind, m=10.):
        return - sum(( math.sin(ind[i]) * (math.sin(((i+1.)*(ind[i] **2.))/math.pi))**(2.*m) for i in range(len(ind.genotype)) ))
    
    @staticmethod
    def schwefel(ind):
        return 418.9829 * float(len(ind.genotype)) - sum((x * math.sin(math.sqrt(abs(x))) for x in ind.genotype))

    @staticmethod
    def rastrigin(ind, a=10.):
        n = float(len(ind))
        return a * n + sum(x * x - a * math.cos(2. * math.pi * x) for x in ind.genotype)

    @staticmethod
    def rosenbrock(ind):
        return sum((100. * (ind.genotype[i+1]-ind.genotype[i]**2.)**2. + (1-ind.genotype[i])**2. for i in range(len(ind.genotype)-1)))