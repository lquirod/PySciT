import ManageItems as M
import TypesPipelines as Pip

class UserActions:
    def __init__(self, userName='New User'):
        self.Name = userName
        self.myPipelines = []
        self.actualPipeline = None
        self.myDatas = []
        self.actualData = None

    ####################################################################################################
    #### Operations with user's Pipelines
    def addPipeline(self, newPipe):
        self.myPipelines.append(newPipe)
        return len(self.myPipelines)
    
    def getMyPipelinesNames(self):
        ret = {}
        for count, aPip in enumerate(self.myPipelines):
            ret[count] = aPip.Name
        return ret
    
    def selectPipeline(self, select = None):
        if  len(self.myPipelines) == 0 or select is None or select < 0 or len(self.myPipelines) < select:
            return None
        else:
            self.actualPipeline = select
            return select
    
    def getActualPipe(self):
        if self.actualPipeline is None:
            return None
        else:
            return self.myPipelines[self.actualPipeline]

    def delPipeline(self, pipePosition = None):
        lenPip = len(self.myPipelines)
        if lenPip == 0 or pipePosition is None or pipePosition < 0 or lenPip < pipePosition :
            return None
        else:
            removeItem = self.myPipelines.pop(pipePosition)
            del removeItem
            lenPip = len(self.myPipelines)
            if self.actualPipeline == pipePosition :
                pipePosition = None
            elif pipePosition < self.actualPipeline or self.actualPipeline == lenPip:
                self.actualPipeline -= 1
            return len(self.myPipelines)

    ####################################################################################################
    ## Operations with the user's actual Pipeline
    # def setAlgorithmPipe(self, theAlgorithm, stepPosition = None):
    #     if self.getActualPipe() is None:
    #         return None
    #     else:
    #         return self.getActualPipe().setAlgorithm(theAlgorithm, stepPosition)
    
    def getSteps(self):
        if self.getActualPipe() is None:
            return None
        else:
            return self.getActualPipe().steps()
        
    def addStep(self, aStep, position = None):
        if self.getActualPipe() is None:
            return None
        else:
            return self.getActualPipe().addStep(aStep, position)

    def delStep(self, position = None):
        if self.getActualPipe() is None:
            return None
        else:
            return self.getActualPipe().delStep(position)
        
    def moveStep(self, fromPosition, toPosition):
        if self.getActualPipe() is None:
            return None
        else:
            return self.getActualPipe().moveStep(fromPosition, toPosition)

    def fitSelectData(self):
        if self.getActualPipe() is None or self.getActualData() is None:
            return None
        else:
            zipped = [[x, y] for x, y in zip(self.getActualData().Data['X_train1'].tolist(), self.getActualData().Data['X_train2'].tolist())]
            # print(self.getActualPipe())
            # print(zipped)
            # self.getActualPipe().fitData(self.getActualData().Data['X_train1'], self.getActualData().Data['X_train2'])
            # self.getActualPipe().fitData(zipped)
            self.getActualPipe().fitData(zipped, self.getActualData().Data['y_train'].tolist())

    def predict(self):
        if self.getActualPipe() is None or self.getActualData() is None:
            return None
        else:
            zipped = [[x, y] for x, y in zip(self.getActualData().Data['X_train1'].tolist(), self.getActualData().Data['X_train2'].tolist())]
            return self.getActualPipe().score(zipped, self.getActualData().Data['y_train'].tolist())

    ####################################################################################################
    #### Operations with user's Datas
    def createData(self, data = None, newNameData='New Data'):
        self.myDatas.append(M.Data.ManageData(data, newNameData))
        return len(self.myDatas)

    def selectData(self, select = None):
        if  len(self.myDatas) == 0 or select is None or select < 0 or len(self.myDatas) < select:
            return None
        else:
            self.actualData = select
            return select

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
        lenData = len(self.myDatas)
        if lenData == 0 or dataPosition is None or dataPosition < 0 or lenData < dataPosition :
            return None
        else:
            removeItem = self.myDatas.pop(dataPosition)
            del removeItem
            lenData = len(self.myDatas)
            if self.actualData == dataPosition :
                dataPosition = None
            elif dataPosition < self.actualData or self.actualData == lenData:
                self.actualData -= 1
            return len(self.myDatas)

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