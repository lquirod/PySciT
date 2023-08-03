from PySciT import Enumerations as Enum
from PySciT import TypesPipelines as tPip
import pandas as pd

class ManageAlgorithms:
    def __init__(self):
        pass

    def getAlgorithmsList(self):
        return  [alg.name for alg in Enum.ALG.Algorithms]
    
    def thereIsAlgorithm(self, nameAlgorithm):
        return True if nameAlgorithm in Enum.ALG.Algorithms.__members__ else False

    def getAlgorithmPipe(self, theAlgorithm, pipeName = 'MyNewPipe'):
        if(pipeName.strip()==''):
            pipeName = 'MyNewPipe'
        if self.thereIsAlgorithm(theAlgorithm):
            if theAlgorithm == Enum.ALG.Algorithms.Linear_Regression.name:
                return tPip.Linear_Regression_Pipe(pipeName)
            elif theAlgorithm == Enum.ALG.Algorithms.KNeighbors_Classifier.name:
                return tPip.KNeighbors_Classifier_Pipe(pipeName)
            elif theAlgorithm == Enum.ALG.Algorithms.Random_Forest_Classifier.name:
                return tPip.Random_Forest_Classifier_Pipe(pipeName)
            elif theAlgorithm == Enum.ALG.Algorithms.Support_Vector_Classification.name:
                return tPip.Support_Vector_Classification_Pipe(pipeName)
        return None
    
