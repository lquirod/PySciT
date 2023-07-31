from sklearn.pipeline import Pipeline
import pandas as pd
from abc import abstractmethod, ABC

#   @classmethod
#   @abstractmethod
class aPipeline(ABC):
    def __init__(self, pipeName):
        self.Name = pipeName
        self.hasAlgorithm = None
        self.aPipeline = Pipeline([])


    ## Operations with the Pipeline's Algorithm
    @abstractmethod
    def setAlgorithm(self, theAlgorithm, stepPosition = None):
        pass
    ####################################################################################################
    ### Operations with the Pipeline's Steps
    def steps(self):
        return self.aPipeline.steps

    def nameSteps(self):
        return [ x[0] for x in self.aPipeline.steps ]


    def getASteps(self, position=None):
        if position is None or position < 0 or len(self.steps()) < position:
            return None
        else:
            return self.aPipeline.steps[position]

    def addStep(self, aStep, position = None):
        if position is None or position < 0 or len(self.steps()) < position:
            self.steps().append(aStep)
            return len(self.steps()) -1
        else:
            self.steps().insert(position, aStep)
            if position <= self.hasAlgorithm:
                self.hasAlgorithm +=1
            return position

    def delStep(self, position = None):
        if  position is None or position < 0 or len(self.steps()) < position or position == self.hasAlgorithm:
            return False
        else:
            if position < self.hasAlgorithm:
                self.hasAlgorithm = self.hasAlgorithm- 1
            self.steps().pop(position)
            return len(self.steps())
        
    def moveStep(self, fromPosition, toPosition):
        if (fromPosition < 0 or len(self.steps()) < fromPosition or
            toPosition < 0 or len(self.steps()) < toPosition or
            fromPosition == toPosition):
            return False
        else:
            if fromPosition == self.hasAlgorithm:
                self.hasAlgorithm = toPosition
            elif toPosition == self.hasAlgorithm:
                self.hasAlgorithm = fromPosition
            movStep = self.steps()[fromPosition]
            self.steps().pop(fromPosition)
            self.steps().insert(toPosition, movStep)
            return True

    ####################################################################################################
    #### Common Operations to all Pipelines
    def get_params(self, deep=True):
        return self.aPipeline.get_params(deep)
    
    def setParams(self, **params):
        self.aPipeline.set_params(**params)
        return True
    ####################################################################################################
    #### Concrete Operations to all Pipelines
    # Concrete variables to each pipeline operation:
    # _varNameOperation = [ [NameParams], [Required bool] ]
    
    # _fit = [[],[]]
    @abstractmethod
    def fit(self, data):
        theData = []
        theDataLen = len(self.__class__._fit[1])
        for aDat in range(theDataLen):
            if aDat < len(data):
                theData.append(data[aDat])
            else:
                theData.append(None)
        return theData

    @abstractmethod
    def predict(self, data):
        pass
        
    @abstractmethod
    def score(self, data):
        pass
    