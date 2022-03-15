# PyGEVO: a pythonic Grammatical Evolution framework

PyGEVO is a pythonic low-code framework for Grammatical Evolution. Minimalistic, efficient and powerful, this framework aims to enable non-expert users to easily wrap up a GE experiment in a few lines of codes:

```python
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.fitnessFunctions.syntheticFunctions import FitnessFunctions

population = Population(numberIndividuals=6, individualSize=8).generatePop()
population = Algorithms("grammar_ANSI_C.bnf", initBNF=56).evolveWithGE(population, FitnessFunctions.griewank, gen=30, porcentSelect=0.2, staticSelection=100,validIndividuals=True, orderedByFitness=True)
population.showTopTen()
```

PyGEVO has also the capability to cythonize the whole project, in order to have better performance. For this we call the Compiler and indicate it to compile the project (to import Cython classes is always recommended to use pyximport):

```python
from compiler import Compiler
Compiler.enableCython()
Compiler.compile()

import pyximport
pyximport.install()
from core.domain.population import Population
from core.domain.algorithms import Algorithms
from core.fitnessFunctions.syntheticFunctions import FitnessFunctions

population = Population(numberIndividuals=6, individualSize=8).generatePop()
population = Algorithms("grammar_ANSI_C.bnf", initBNF=56).evolveWithGE(population, FitnessFunctions.griewank, gen=30, porcentSelect=0.2, staticSelection=100,validIndividuals=True, orderedByFitness=True)
population.showTopTen()
```

This is inspired in the work from __[Prof. Conor Ryan](https://www.linkedin.com/in/conor-ryan-5166b083/)__ [1]

PyGEVO is still in an ALPHA stage

Primary Authors
===============

* __[Ivan Hugo Guevara](https://github.com/AivanGuevara)__

    PhD researcher at Confirm Centre@UL
    
* __[Lucas Agustin Gonzalez](https://github.com/lag21392)__

    BI analyst at Biwares

Acknowledgements
===============

* __[Dr. Enrique Naredo](https://www.linkedin.com/in/enrique-naredo-garc%C3%ADa-25770b93/)__

    Senior Postdoctoral Researcher at BDS group@UL
    
* __[Dr. Douglas Motas Dias](https://www.linkedin.com/in/douglas-mota-dias/)__

    Senior Postdoctoral Researcher at BDS group@UL

References
===============
[1] Conor Ryan, J. J. Collins, and Michael O’Neill. 1998. Grammatical Evolution: Evolving Programs for an Arbitrary Language. In EuroGP (Lecture Notes in Computer Science), Wolfgang Banzhaf, Riccardo Poli, Marc Schoenauer, and Terence C.Fogarty (Eds.), Vol. 1391. Springer, 83–96 