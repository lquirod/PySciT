# import PyTSys.UserActions as user
# from PyTSys.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
# import PyTSys.ManageItems as M
# from PyTSys.Aditional.MoreFunctions import *
from PyTSys import *
import pandas as pd

myUser = user.UserActions('Cherished User')
mTr = M.TR.ManageTransformations()
mAlg = M.ALG.ManageAlgorithms()


opc = ''
file = 'Ninguno'
aux = ''
aux1 = ''


print('creando user')
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
myUser.createData(df, 'Hola data')

myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression'))
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),1, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),0, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),1, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),8, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),8, 0)
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largoargo largo largoargolargoargo largo largoargo largo largoargo largo largoargo largo largoargo largo largoargo largo largoargo largo largoargo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', '    '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'fdfd fdd fd f'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2'))
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo '))


# print(myUser.getMyPipelinesNames())
# print('Select pipe')
# print(myUser.selectPipeline(0))
# print(myUser.getActualPipe())
# print(myUser.getActualPipe().Name)
# print('Add Step')
# print(myUser.addStep(got,0))
# print(myUser.getActualPipe().steps())
# print(myUser.delPipeline(0))