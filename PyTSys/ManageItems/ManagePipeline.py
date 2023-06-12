from sklearn.pipeline import Pipeline
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# sc_model = MinMaxScaler ()
# sc_model.fit_transform (ran_data)
from sklearn import linear_model

class ManagePipeline:
    def __init__(self, pipeName = 'MyNewPipe'):
        self.Name = pipeName
        self.hasAlgorithm = None
        self.theAlgorithm = None
        self.typeAlgorithm = None
        self.aPipeline = Pipeline([])

    ####################################################################################################
    #### Operations with the Pipeline's structure
    ## Operations with the Pipeline's Steps
    def steps(self):
        return self.aPipeline.steps

    def addStep(self, aStep, position = None):
        if position is None or position < 0 or len(self.steps()) < position:
            self.steps().append(aStep)
            # ret = len(self.steps()) -1
            return len(self.steps()) -1
        else:
            self.steps().insert(position, aStep)
            return position

    def delStep(self, position = None):
        if  position is None or position < 0 or len(self.steps()) < position :
            return None
        else:
            self.steps().pop(position)
            if position == self.hasAlgorithm:
                self.hasAlgorithm = None
            return len(self.steps())
        
    def moveStep(self, fromPosition, toPosition):
        if (fromPosition < 0 or len(self.steps()) < fromPosition or
            toPosition < 0 or len(self.steps()) < toPosition or
            fromPosition == toPosition):
            return False
        else:
            movStep = self.steps()[fromPosition]
            self.steps().pop(fromPosition)
            self.steps().insert(toPosition, movStep)
            return True

    ## Operations with the Pipeline's Algorithm
    def setAlgorithm(self, theAlgorithm, stepPosition = None):
        if self.hasAlgorithm is not None:
            self.delStep(self.hasAlgorithm)
            
        self.hasAlgorithm = self.addStep(theAlgorithm, stepPosition)
        return self.hasAlgorithm

    ####################################################################################################
    #### Additional
    def fitData(self, x,y = None, sample_weight=None):
        # self.aPipeline.fit(x, y, sample_weight)
        self.aPipeline.fit(x, y)

    def getCoef(self):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].coef_

    def get_params(self, deep=True):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].deep(deep)

    def setParams(self, params):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].set_params(params)
    
    def score(self, X, y, sample_weight=None):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].score(X, y, sample_weight)
    
    def predict(self, X):
        if self.hasAlgorithm is None:
            return None
        else:
            return self.steps()[self.hasAlgorithm].predict(X)



