import inspect
from sklearn.pipeline import Pipeline
import pandas as pd
from abc import abstractmethod, ABC
from sklearn import linear_model
from PyTSys.TypesPipelines import aPipeline

class LinearRegressionPipe(aPipeline.aPipeline):
    def __init__(self, pipeName = 'MyNewPipe'):
        super().__init__(pipeName)
        # self.Name = pipeName
        # self.hasAlgorithm = None
        # self.aPipeline = Pipeline([])
        self.setAlgorithm()

    ## Operations with the Pipeline's Algorithm
    def setAlgorithm(self):
        self.hasAlgorithm = self.addStep( ['Linear_Regression', linear_model.LinearRegression()])
        return self.hasAlgorithm

    ####################################################################################################
    #### Operations with the Pipeline's Steps in Abstract class aPipeline,py
    # def steps(self):
    # def nameSteps(self):
    # def getASteps(self, position=None):
    # def addStep(self, aStep, position = None):
    # def delStep(self, position = None):
    # def moveStep(self, fromPosition, toPosition): 
    ####################################################################################################
    #### Common Operations to all Pipelines
    # def get_params(self, deep=True):
    # def setParams(self, **params):
    ####################################################################################################
    #### Concrete Operations to all Pipelines
    # Concrete variables to each pipeline operation:
    # _varNameOperation = [ [NameParams], [Required bool] ]

    # def fitData(self, X, y = None, sample_weight=None):
    # _fit = [['Training data, X','Target values, y', 'Individual weights for each sample (Linear_Regression__sample_weight)'],
    #         [1,1,0]]
    _fit = [['Training data, X','Target values, y'],
            [1,1]]
    def fit(self, data):
        theData = super().dataInput(data, len(self.__class__._fit[0]))
        # print(inspect.getargspec(self.aPipeline[0].fit).args)
        # print('Data: 0')
        # print(theData[0])
        # print('Data: 1')
        # print(theData[1])
        # print('Data: 2')
        # print(theData[2])
        # print (theData)
        try:
            self.aPipeline.fit(theData[0], theData[1])
            return [True, 'Fit done']
        except Exception as e:
            return [False, str(e)]
    
    def predict(self, data):
        theData = super().dataInput(data, len(self.__class__._predict[0]))
        try:
            ret = self.aPipeline.predict(theData[0])
            return [True, ret]
        except Exception as e:
            return [False, str(e)]
        
    def score(self, data):
        theData = super().dataInput(data, len(self.__class__._fit[0]))
        try:
            ret = self.aPipeline.score(theData[0], theData[1])
            return [True, ret]
        except Exception as e:
            return [False, str(e)]

    # def getCoef(self):
    #     if self.hasAlgorithm is None:
    #         return None
    #     else:
    #         return self.steps()[self.hasAlgorithm].coef_


