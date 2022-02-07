class Individual:

    def __init__(self) -> None:
        self.genotype = []
        self.fitness_score = 0
        self.phenotype = None
        self.stringBuild = None

    def isValid(self):
        return (self.phenotype.count("<") == 0) and (self.phenotype.count(">") == 0) and (self.fitness_score != None)
