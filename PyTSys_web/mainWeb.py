from markupsafe import Markup
import PyTSys.UserActions as user
# from PyTSys.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
import PyTSys.ManageItems as M
from PyTSys.Aditional.MoreFunctions import *

from datetime import datetime

myUser = user.UserActions('Cherished User')
mTr = M.TR.ManageTransformations()
mAlg = M.ALG.ManageAlgorithms()

logs = []

opc = ''
file = 'Ninguno'
aux = ''
aux1 = ''

def addLog(msg):
    date = datetime.now().strftime("%m/%d/%Y-%H:%M: ")
    newLog = "<span class=\"boldText\">"+ date + "</span></br>" + msg
    logs.insert(0, Markup(newLog))


print('creando user')
print(myUser.Name)
myUser.addPipeline(mAlg.getAlgorithmPipe('Linear_Regression'))
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),1, 0)
myUser.addStep(mTr.getTransformation("MinMax_Scaling"),0, 0)
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