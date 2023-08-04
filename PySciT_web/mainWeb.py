# import PySciT.UserActions as user
# from PySciT.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
# import PySciT.ManageItems as M
# from PySciT.Aditional.MoreFunctions import *
from PySciT import *
import pandas as pd

myUser = user.UserActions('Cherished User')
mTr = M.TR.ManageTransformations()
mAlg = M.ALG.ManageAlgorithms()


opc = ''
file = 'Ninguno'
aux = ''
aux1 = ''


print('Creating user...')
print(myUser.Name)
myUser.createData()
data = [['tom', 10, 2005, 'gummies'],
        ['nick', 15, 2005, 'gummies'],
        ['nick1', 45, 2005, 'gummies'],
        ['n2ick', 65, 2005, 'gummies'],
        ['n3ick', 15, 2005, 'gummies'],
        ['n4ick', 17, 2005, 'gummies'],
        ['n5ick', 4, 2005, 'gummies'],
        ['n6ick', 13, 2005, 'gummies'],
        ['jula', 14, 2005, 'gummies']]
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'birth', 'likes'])
myUser.createData(df, 'dummie data')

data = [[1,1,6, [1,1]],
[1,2,8, [1,2]],
[2,2,9, [2,2]],
[2,3,11, [2,3]],]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['X_train1','X_train2','y_train', 'Xtrain1y2'])
myUser.createData(df, 'test 1 data')



myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', ))
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),1, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),0, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),1, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),8, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),8, 0)
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'Linear_Regression'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Support_Vector_Classification', 'Support_Vector_Classification'))
myUser.addPipeline(mAlg.getAlgorithmPipe('KNeighbors_Classifier', 'KNeighbors_Classifier'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Random_Forest_Classifier', 'Random_Forest_Classifier'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
# myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Lao Largo largo largo largo largo Largo largo largo '))


# print(myUser.getMyPipelinesNames())
# print('Select pipe')
# print(myUser.selectPipeline(0))
# print(myUser.getActualPipe())
# print(myUser.getActualPipe().Name)
# print('Add Step')
# print(myUser.addStep(got,0))
# print(myUser.getActualPipe().steps())
# print(myUser.delPipeline(0))

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn import linear_model
import numpy as np

# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = np.dot(X, np.array([1, 2])) + 3
# pipe = Pipeline([('linearmodel', linear_model.LinearRegression())])
# # The pipeline can be used as any other estimator
# # and avoids leaking the test set into the train set
# print(pipe.fit(X, y))
# print(pipe.predict(X))
# print(pipe.score(X, y))


from sklearn.datasets import make_blobs
import numpy as np

centers = [[2, 3], [5, 5], [1, 8]]
n_classes = len(centers)
data, labels = make_blobs(n_samples=150, 
                          centers=np.array(centers),
                          random_state=1)
from sklearn.model_selection import train_test_split
res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=1)

train_data, test_data, train_labels, test_labels = res 
# print('train_data,')
# print(train_data)
# print('test_data')
# print(test_data)
# print(' train_labels')
# print(train_labels)
# print(', test_labels')
# print(test_labels)