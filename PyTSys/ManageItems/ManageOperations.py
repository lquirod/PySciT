import Enumerations as Enum
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# sc_model = MinMaxScaler ()
# sc_model.fit_transform (ran_data)
from sklearn import linear_model


#  @classmethod
#     def display(cls):
#         print(cls.get_contents())
    
#     @abstractmethod


class ManageOperations:
    def __init__(self):
        pass
        # self.Linear_Regression = ['Linear Regression', linear_model.LinearRegression()]

    def thereIsAlgorithm(self, nameAlgorithm):
        return True if nameAlgorithm in Enum.ALG else False

    def thereIsTransformation(self, nameTransformation):
        return True if nameTransformation in Enum.TR else False

    def getAlgorithm(self, nameAlgorithm):
        if self.thereIsAlgorithm(nameAlgorithm):
            if nameAlgorithm == Enum.ALG.Algorithms.Linear_Regression:
                return ['Linear Regression', linear_model.LinearRegression()]
                # return self.Linear_Regression
        
        return None
    
    def getTransformation(self, nameTransformation):
        if self.thereIsTransformation(nameTransformation):
            if nameTransformation == Enum.TR.Transformations.MinMax_Scaling:
                return ['MinMax scaling', MinMaxScaler()]
          
        return None
            




