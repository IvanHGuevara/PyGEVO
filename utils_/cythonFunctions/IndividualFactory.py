
class IndividualFactory:
    def __init__(self) -> None:
        self.individualDicc ={}

    def getIndividualDicc(self,phenotype):
        return self.individualDicc[phenotype]
    def putIndividualDicc(self,phenotype,value):
        self.individualDicc[phenotype]=value

