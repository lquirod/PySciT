from sklearn.pipeline import Pipeline
import pandas as pd
from abc import abstractmethod, ABC
from sklearn import linear_model
from PyTSys.TypesPipelines import aPipeline

#   @classmethod
#   @abstractmethod
class LinearRegressionPipe(aPipeline.aPipeline):
    def __init__(self, pipeName = 'MyNewPipe'):
        # self.Name = pipeName
        # self.hasAlgorithm = None
        # self.typeAlgorithm = None
        # self.aPipeline = Pipeline([])
        super().__init__(pipeName)
        self.typeAlgorithm = 1
        self.setAlgorithm()


    ####################################################################################################
    #### Operations with the Pipeline's structure
    ## Operations with the Pipeline's Steps
    # In Abstract class aPipeline,py
    # def steps(self):
    # def addStep(self, aStep, position = None):
    # def delStep(self, position = None):
    # def moveStep(self, fromPosition, toPosition):

    # ## Operations with the Pipeline's Algorithm
    def setAlgorithm(self):
        self.hasAlgorithm = self.addStep( ['Linear_Regression', linear_model.LinearRegression()])
        return self.hasAlgorithm

    ####################################################################################################
    #### Concrete Operations

    # # @abstractmethod
    # def get_params(self, deep=True):
    #     if self.hasAlgorithm is None:
    #         return None
    #     else:
    #         # return self.steps()[self.hasAlgorithm].deep(deep)
    #         return self.aPipeline.get_params(deep)

    # # @abstractmethod
    # def setParams(self, params):
    #     # if self.hasAlgorithm is None:
    #     #     return None
    #     # else:
    #     #     return self.steps()[self.hasAlgorithm].set_params(params)
    #     return self.steps()[self.hasAlgorithm].set_params(params)

    # @abstractmethod
    def fitData(self, x,y = None, sample_weight=None):
        # self.aPipeline.fit(x, y, sample_weight)
        self.aPipeline.fit(x, y)
    
    # @abstractmethod
    def predict(self, X):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].predict(X)
        
    # @abstractmethod
    def score(self, X, y, sample_weight=None):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.aPipeline.score(X, y, sample_weight)
            # return self.steps()[self.hasAlgorithm][1].score(X, y, sample_weight)
            # return self.steps().tolist()[self.hasAlgorithm].score(X, y, sample_weight)
            # return self.steps()[self.hasAlgorithm].score(X, y, sample_weight)
    

    # def getCoef(self):
    #     if self.hasAlgorithm is None:
    #         return None
    #     else:
    #         return self.steps()[self.hasAlgorithm].coef_


