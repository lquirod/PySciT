import pandas as pd
# from Enumerations import Transformations as TR
class ManageData:
    
    def __init__(self, data = None, dataName = 'New Data'):
        self.Name = dataName
        self.Data = data
        self.history = []

    def clear(self):
        self.Name = 'Clean Data'
        del self.Data
        self.history.clear()

    def getHistory(self):
        ret = []
        for h in self.history:
            ret.append(h.name)
        return ret

    ####################################################################################################
    #### Manage Data
    ## From File
    def setDataFromFile(self, newFileName, existHeader = 0, newSep = ','):
        self.clear()
        self.Name = newFileName
        self.Data = pd.read_csv(newFileName, header=existHeader, sep=newSep)
        print(self.Data)
        
    def setNewData(self, data = None, dataName = 'New Data'):
        self.clear()
        self.Name = dataName
        self.Data = data
        self.history = []

    def existNumCol(self, numCol = None):
        try:
            total = len(self.Data.columns)
            nCol = int(numCol)
            if total == 0 or nCol < 0 and total < nCol :
                return None
            else:
                return nCol
        except Exception:
            return None
        
    def getNameCols(self):
        if self.Data is None:
            return None
        else:
            return self.Data.columns.values.tolist()

    def getCol(self, numCol):
        nCol =  self.existNumCol(numCol)
        # if self.Data is None:
        if nCol is None:
            return None
        else:
            return self.Data.iloc[:,nCol].tolist()
        
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
