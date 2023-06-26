import PyTSys.UserActions as user
# from PyTSys.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
import PyTSys.ManageItems as M
from PyTSys.Aditional.MoreFunctions import *

myUser = user.UserActions('Cherished User')
mTr = M.TR.ManageTransformations()
mAlg = M.ALG.ManageAlgorithms()

opc = ''
file = 'Ninguno'
aux = ''
aux1 = ''


print('creando user')
print(myUser.Name)
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression')))

print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'er n1 2')))
print(myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression', 'un 3 Largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo largo largo Largo largo largo ')))


# print(myUser.getMyPipelinesNames())
# print('Select pipe')
# print(myUser.selectPipeline(0))
# print(myUser.getActualPipe())
# print(myUser.getActualPipe().Name)
# print('Add Step')
# print(myUser.addStep(got,0))
# print(myUser.getActualPipe().steps())
# print(myUser.delPipeline(0))