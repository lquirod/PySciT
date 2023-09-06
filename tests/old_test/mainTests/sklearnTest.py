import pandas as pd
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import clases.ManageFile as mf
import clases.ManageData as md

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print("This filename is in: \""+filename+"\" path")

# myMF = mf.ManageFile(filename)
# print(myMF.nameFile)
# print(myMF.getNameCols())
# print(myMF.dataFile)


# myData = md.ManageData(myMF.dataFile, 'Data1')
# print(myData.Data)
# print('Cambio columnas, antes era' + myData.getNameCols() )
# myData.setRenameCols(['111','222','333'])
# print(myData.Data)

# def extractFile(self, fils, cols):
#     new_dataset = dataset[['A','D']]
#     self.nameFile = newFileName
#     self.dataFile = pd.read_csv(newFileName)

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print("This filename is in: \""+filename+"\" path")

# df = pd.read_csv(filename)

# print("This is cols start: \n") 
# print(df.columns.values.tolist()) 
# print("End of cols") 
# print("This is file is: \n "+df.to_string()) 



# from sklearn.svm import SVC
# from sklearn.preprocessing import StandardScaler
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline
# X, y = make_classification(random_state=0)
# X_train, X_test, y_train, y_test = train_test_split(X, y,
#                                                     random_state=0)
# pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
# # The pipeline can be used as any other estimator
# # and avoids leaking the test set into the train set
# pipe.fit(X_train, y_train)
# print(type(pipe.steps))
# print(pipe.steps)
# print(pipe.steps[1])
# print(pipe.score(X_test, y_test))




from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn import linear_model
import numpy as np

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3
pipe = Pipeline([('linearmodel', linear_model.LinearRegression())])
# The pipeline can be used as any other estimator
# and avoids leaking the test set into the train set
pipe.fit(X, y)
print(type(pipe.steps))
print(pipe.steps)
print(pipe.steps[0])
print(pipe.score(X, y))


