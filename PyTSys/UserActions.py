from PyTSys import ManageItems as M
from PyTSys import TypesPipelines as Pip

class UserActions:
    def __init__(self, userName='New User'):
        self.Name = userName
        self.myPipelines = []
        self.actualPipeline = None
        self.myDatas = []
        self.actualData = None

    def clearPipes(self):
        for pip in self.myPipelines:
            del pip
        self.actualPipeline = None
        
    def clearDatas(self):
        for dat in self.myDatas:
            del dat
        self.actualData = None
        
    ####################################################################################################
    #### Operations with user's Pipelines
    def addPipeline(self, newPipe):
        self.myPipelines.append(newPipe)
        return len(self.myPipelines)
    
    def existPipeline(self, num):
       if  len(self.myPipelines) == 0 or num is None or int(num) < 0 or len(self.myPipelines) < int(num):
            return False
       else:
           return True
           
    def getMyPipelinesNames(self):
        ret = {}
        for count, aPip in enumerate(self.myPipelines):
            ret[count] = aPip.Name
        return ret
    
    def selectPipeline(self, select = None):
        if  self.existPipeline(select):
            self.actualPipeline = select
            return select
        else:
            self.actualPipeline = None
            return None
    
    def getActualPipe(self):
        if self.actualPipeline is None:
            return None
        else:
            return self.myPipelines[self.actualPipeline]

    def delPipeline(self, pipePosition = None):
        if self.existPipeline(pipePosition):
            removeItem = self.myPipelines.pop(pipePosition)
            del removeItem
            lenPip = len(self.myPipelines)
            if self.actualPipeline == pipePosition :
                pipePosition = None
            elif self.actualPipeline is not None and (pipePosition < self.actualPipeline or self.actualPipeline == lenPip):
                self.actualPipeline -= 1
            return lenPip
        else:
            return None

    ####################################################################################################
    ## Operations with the user's actual Pipeline
    # Steps
    def getSteps(self, pip=None, namesOnly = False):
        if self.existPipeline(pip):
            getFrom = self.myPipelines[pip]
        elif self.getActualPipe() is not None:
            getFrom = self.getActualPipe()
        else:
            return None
        if namesOnly:
            getFrom.nameSteps()
        else:
            return getFrom.steps()
        
        
    def addStep(self, aStep, position = None, thePipe = None):
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].addStep(aStep, position)
        elif self.getActualPipe() is not None:
            return self.getActualPipe().addStep(aStep, position)
        else:
            return None

    def delStep(self, position = None, thePipe = None):
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].delStep(position)
        elif self.getActualPipe() is not None:
            return self.getActualPipe().delStep(position)
        else:
            return False
        
    def moveStep(self, fromPosition, toPosition, thePipe = None):
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].moveStep(fromPosition, toPosition)
        elif self.getActualPipe() is not None:
            return self.getActualPipe().moveStep(fromPosition, toPosition)
        else:
            return False
        
    # Common operations
    def setParams(self, **params):
        return self.getActualPipe().setParams(**params)

    def fitPipe(self, theData, thePipe = None):
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].fit(theData)
        elif self.getActualPipe() is not None:
        # # elif self.getActualPipe() is not None:
        #     zipped = [[x, y] for x, y in zip(self.getActualData().Data['X_train1'].tolist(), self.getActualData().Data['X_train2'].tolist())]
        #     # print(self.getActualPipe())
        #     # print(zipped)
        #     # self.getActualPipe().fitData(self.getActualData().Data['X_train1'], self.getActualData().Data['X_train2'])
        #     # self.getActualPipe().fitData(zipped)
        #     self.getActualPipe().fitData(zipped, self.getActualData().Data['y_train'].tolist())
            return self.getActualPipe().fit(theData)
        else:
            return [False, 'Pipe not found']

    def predictPipe(self, theData, thePipe = None):
        # if self.getActualPipe() is None or self.getActualData() is None:
        #     return None
        # else:
        #     zipped = [[x, y] for x, y in zip(self.getActualData().Data['X_train1'].tolist(), self.getActualData().Data['X_train2'].tolist())]
        #     return self.getActualPipe().score(zipped, self.getActualData().Data['y_train'].tolist())
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].predict(theData)
        elif self.getActualPipe() is not None:
            return self.getActualPipe().predict(theData)
        else:
            return [False, 'Pipe not found']

    def scorePipe(self, theData, thePipe = None):
        if self.existPipeline(thePipe):
            return self.myPipelines[thePipe].score(theData)
        elif self.getActualPipe() is not None:
            return self.getActualPipe().score(theData)
        else:
            return [False, 'Pipe not found']
    ####################################################################################################
    #### Operations with user's Datas
    def createData(self, data = None, newNameData='New Data'):
        if newNameData=='':
            newNameData='New Data'
        self.myDatas.append(M.Data.ManageData(data, newNameData))
        return len(self.myDatas)

    def existData(self, num):
        if  len(self.myDatas) == 0 or select is None or select < 0 or len(self.myDatas) < select:
            return False
        else:
            return True
        
    def selectData(self, select = None):
        if  self.existData(select):
            self.actualData = select
            return select
        else:
            return None

    def getActualData(self):
        if self.actualData is None:
            return None
        else:
            return self.myDatas[self.actualData]

    def setDataFromFile(self, newFileName, existHeader = 0, newSep = ','):
        self.getActualData().setDataFromFile(newFileName, existHeader, newSep)
        return self.actualData

    def setNewData(self, data = None, newNameData='New Data'):
        self.getActualData().setNewData(data, newNameData)
        return self.actualData
    
    def getMyDatasNames(self):
        ret = {}
        for count, aDat in enumerate(self.myDatas):
            ret[count] = aDat.Name
        return ret
    
    def delData(self, dataPosition = None):
        if  self.existData(dataPosition):
            removeItem = self.myDatas.pop(dataPosition)
            del removeItem
            lenData = len(self.myDatas)
            if self.actualData == dataPosition :
                dataPosition = None
            elif dataPosition < self.actualData or self.actualData == lenData:
                self.actualData -= 1
            return lenData
        else:
            return None

    ####################################################################################################
    ## Operations with the user's actual Data
    def getNameCols(self):
        if self.Data is None:
            return None
        else:
            return self.Data.columns.values.tolist()

    def setRenameCols(self, newNameCols):
        return self.getActualData().setRenameCols(newNameCols)

    def applyTransform(self, transform):
        return self.getActualData().applyTransform(transform)