import pandas as pd

class ManageData:
    def __init__(self, data = None, dataName = 'New Data'):
        self.Name = dataName
        self.Data = data
        self.history = []

    def clear(self):
        self.Name = 'Clean Data'
        del self.Data
        self.history.clear()

    ####################################################################################################
    #### Manage Data
    ## From File
    def setDataFromFile(self, newFileName, existHeader = 0, newSep = ','):
        self.clear()
        self.Name = newFileName
        self.dataFile = pd.read_csv(newFileName, header=existHeader, sep=newSep)

    def setNewData(self, data = None, dataName = 'New Data'):
        self.clear()
        self.Name = dataName
        self.Data = data
        self.history = []

    def getNameCols(self):
        if self.Data is None:
            return None
        else:
            return self.Data.columns.values.tolist()



    ####################################################################################################
    #### Modify Data
    ## From File
    def setRenameCols(self, newNameCols):
        if self.Data is None:
            return None
        elif len(newNameCols) != len(self.Data.columns):
            return False
        else:
            self.Data.columns = newNameCols
            return True

    ####################################################################################################
    #### Operations with the Data
    def applyTransform(self, transform):
        
        self.Data

        self.history.append(transform[0])
    # def extractData(self, fils, cols):
    #     # new_dataset = dataset[['A','D']]
    #     # self.Name = newDataName
    #     # self.dataData = pd.read_csv(newDataName)

    #     newDF = self.dataData.filter(cols, axis=1)
    #     newDF = self.dataData.filter(fils, axis=0)

    #     return newDF
