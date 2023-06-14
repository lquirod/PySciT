import Enumerations as Enum
import pandas as pd
import TypesPipelines as tPip

class ManageAlgorithms:
    def __init__(self):
        pass

    def getAlgorithmsList(self):
        return  [alg.name for alg in Enum.ALG.Algorithms]
    
    def thereIsAlgorithm(self, nameAlgorithm):
        return True if nameAlgorithm in Enum.ALG.Algorithms.__members__ else False

    def getAlgorithmPipe(self, theAlgorithm, pipeName = 'MyNewPipe'):
        if self.thereIsAlgorithm(theAlgorithm):
            if theAlgorithm == Enum.ALG.Algorithms.Linear_Regression.name:
                return tPip.Lineal_Regresion.LinearRegressionPipe(pipeName)
        return None
