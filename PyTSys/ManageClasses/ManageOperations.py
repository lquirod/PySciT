import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# sc_model = MinMaxScaler ()
# sc_model.fit_transform (ran_data)
from sklearn import linear_model

class ManageOperations:
    Algorithms = {'Linear Regression'}
    Transformations = {'MinMax scaling'}

    def __init__(self):
        pass
        # self.Linear_Regression = ['Linear Regression', linear_model.LinearRegression()]

    def thereIsAlgorithm(self, nameAlgorithm):
        return True if nameAlgorithm in self.Algorithms else False

    def thereIsTransformation(self, nameTransformation):
        return True if nameTransformation in self.Transformations else False
    
    def thereIs(self, name):
        if self.thereIsAlgorithm(name):
            return 'A'
        elif self.thereIsTransformation(name):
            return 'T'
        else:
            return None

    def getAlgorithm(self, nameAlgorithm):
        if self.thereIsAlgorithm(nameAlgorithm):
            if nameAlgorithm == 'Linear Regression':
                return ['Linear Regression', linear_model.LinearRegression()]
                # return self.Linear_Regression
        
        return None
    
    def getTransformation(self, nameTransformation):
        if self.thereIsTransformation(nameTransformation):
            if nameTransformation == 'MinMax scaling':
                return ['MinMax scaling', MinMaxScaler()]
          
        return None
            




