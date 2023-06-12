import clases.ManageFile as mf
import clases.ManageData as md
import clases.ManagePipeline as pip
import clases.UserActions as user
from clases.MoreFunctions import *
import clases.ManageOperations as mo

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# filename = askFileLocation()
# print("This filename is in: \""+filename+"\" path")

# myMF = mf.ManageFile(filename)
# print(myMF.nameFile)
# print(myMF.getNameCols())
# print(myMF.dataFile)

# myData = md.ManageData(myMF.dataFile, 'Data1')
# print('Cambio columnas, antes era')
# print(myData.Data)
# print(myData.getNameCols() )
# myData.setRenameCols(['111','222','333'])

myPipeline = pip.ManagePipeline('mi Pipelitine')
print('Se viene el pipe iadamo: '+myPipeline.Name+' que puede hacer:')
tr = mo.ManageOperations()
# print(tr.Algorithms)
fst = 'Linear Regression'
# print(fst)
# print(tr.thereIs(fst))
got = tr.getAlgorithm(fst)
print(got)


myPipeline.setAlgorithm(got)

import numpy as np
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

print('x')
print(X)
print('y')
print(y)
print('Se viene el fit')
myPipeline.fitData(X, y)
# print('getCoef')
# print(myPipeline.getCoef())
# print('score')
# print(myPipeline.score(X,y))

# print('getmethods, atts, meta_data from pipe')
# print(dir(myPipeline))
# print('getmethods, atts, meta_data from myAlgorithm')
# print(dir(myPipeline.myAlgorithm))

# import inspect
# import types
# print('getmethods from pipe')
# print(inspect.getmembers(myPipeline, inspect.ismethod))
# print('getmethods from myAlgorithm')
# print(inspect.getmembers(myPipeline.myAlgorithm, inspect.ismethod))

# a=myPipeline
# methodList = [n for n, v in inspect.getmembers(a, inspect.ismethod)
#             #   if isinstance(v,types.MethodType)
#               ]

# for methodname in methodList:
# #    func=getattr(a,methodname)
#     print(methodname)

# print('getKeys from pipe')
# print(myPipeline.__dict__.keys())
# print('getkeys from myAlgorithm')
# print(myPipeline.myAlgorithm.__dict__.keys())

# print('getKeys from pipe')
# print(len(myPipeline.__dict__.keys()))
# print('getkeys from myAlgorithm')
# anItem = list(myPipeline.myAlgorithm.__dict__.keys())[5]
# print(anItem)
# print(getattr(myPipeline.myAlgorithm, anItem))

# print('pruebas más de tipo para keys del pipe')
# print(type(myPipeline.__dict__.keys()))
# print('type del myAlgorithm')
# print(type(myPipeline.myAlgorithm.__dict__.keys()))
