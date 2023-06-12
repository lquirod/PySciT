import pandas as pd

class ManageFile:
 
    def __init__(self, fileName = None, existHeader = 0, newSep = ','):
        # self.nameFile = fileName
        if fileName is not None:
            self.openNewFile(fileName, existHeader, newSep)
        else:
            self.nameFile = fileName

    def openNewFile(self, newFileName, existHeader = 0, newSep = ','):
        self.nameFile = newFileName
        self.dataFile = pd.read_csv(newFileName, header=existHeader, sep=newSep)

    # def getNameFile(self):
    #     return self.nameFile
    
    def getNameCols(self):
        return self.dataFile.columns.values.tolist()
    
    # def getDataFile(self):
    #     return self.dataFile

    def extractData(self, fils, cols):
        # new_dataset = dataset[['A','D']]
        # self.nameFile = newFileName
        # self.dataFile = pd.read_csv(newFileName)

        newDF = self.dataFile.filter(cols, axis=1)
        newDF = self.dataFile.filter(fils, axis=0)

        return newDF



# import Person as p
# person1 = p.person('Anna', 20, 'Female')
# person1.person_details()
# import sys

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print("This filename is in: \""+filename+"\" path")
# df = pd.read_csv(filename
# print(df.to_string()) 

# class person:
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
 
#   def person_details(self):
#     print(f'Person Name: {self.name} \nPerson Age: {self.age} \nPerson Gender: {self.gender}\n')
