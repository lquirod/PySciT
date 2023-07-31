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
    _fit = [['X (training data)','Y (target values)', 'Individual weights for each sample (sample values)'],
            [1,1,0]]

    # def fitData(self, X, y = None, sample_weight=None):
    def fit(self, data):
        theData = super().fit(data)


        print('Data: 0')
        print(theData[0])
        print('Data: 1')
        print(theData[1])
        print('Data: 2')
        print(theData[2])
        try:
            self.aPipeline.fit(theData[0], theData[1], Linear_Regression__sample_weight=theData[2])
            return True
        except Exception as e:
            return e
    
    def predict(self, X):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].predict(X)
        
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


