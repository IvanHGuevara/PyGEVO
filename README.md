# PyGE: a pythonic Grammatical Evolution framework

PyGE is a pythonic low-code framework for Grammatical Evolution. Minimalistic, efficient and powerful, this framework aims to enable non-expert users to easily wrap up a GE experiment in a few lines of codes:

```python
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms
from utils_.fitness_functions.fitness_functions import FitnessFunctions

population = Population(numberIndividuals=6, individualSize=8).generatePop()
population = Algorithms("grammar_ANSI_C.bnf", initBNF=56).evolveWithGE(population, FitnessFunctions.griewank, gen=30, porcentSelect=0.2, staticSelection=100,validIndividuals=True, orderedByFitness=True)
population.showTopTen()
```

PyGE has also the capability to cythonize the whole project, in order to have better performance. For this we call the Compiler and indicate it to compile the project (to import Cython classes is always recommended to use pyximport):

```python
from compiler import Compiler
Compiler.enableCython()
Compiler.compile()

import pyximport
pyximport.install()
from utils_.domain_objects.population import Population
from utils_.algorithms import Algorithms
from utils_.fitness_functions.fitness_functions import FitnessFunctions

population = Population(numberIndividuals=6, individualSize=8).generatePop()
population = Algorithms("grammar_ANSI_C.bnf", initBNF=56).evolveWithGE(population, FitnessFunctions.griewank, gen=30, porcentSelect=0.2, staticSelection=100,validIndividuals=True, orderedByFitness=True)
population.showTopTen()
```

PyGE is inspired in the work from Prof. Tiziana Margaria [1] and Prof. Conor Ryan [2]

Acknowledgements
===============

* __[Prof. Tiziana Margaria](https://www.linkedin.com/in/tiziana-margaria-9044a12/)__

    Full professor, co-Director of Immersive Software Engineering at University of Limerick. PI at Confirm Centre.
    
* __[Prof. Conor Ryan](https://www.linkedin.com/in/conor-ryan-5166b083/)__

    Full Professor at University of Limerick. Leader member at BDS group@UL.

* __[Dr. Enrique Naredo](https://www.linkedin.com/in/enrique-naredo-garc%C3%ADa-25770b93/)__

    Senior Postdoctoral Researcher at BDS group@UL
    
* __[Dr. Douglas Motas Dias](https://www.linkedin.com/in/douglas-mota-dias/)__

    Senior Postdoctoral Researcher at BDS group@UL


Primary Authors
===============

* __[Ivan Hugo Guevara](https://github.com/AivanGuevara)__

    PhD researcher at Confirm Centre@UL - MaTE.AI team member
    
* __[Lucas Agustin Gonzalez](https://github.com/lag21392)__

    BI analyst at Biwares - MaTE.AI team member
