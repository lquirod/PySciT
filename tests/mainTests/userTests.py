import PyTSys.UserActions as user
from PyTSys.MoreFunctions import *
import PyTSys.ManageItems.ManageTransformations as mo

# filename = askFileLocation()
# print("This filename is in: \""+filename+"\" path")

# user1 = user.UserActions()
# print(user1.Name)
# print(user1.createPipeline())
# print(user1.getMyPipelinesNames())
# print(user1.selectPipeline(0))
# print(user1.delPipeline(0))

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

tr = mo.ManageTransformations()
print(tr.Algorithms)
fst = 'Linear Regression'
print(fst)
print(tr.thereIs(fst))
got = tr.getAlgorithm(fst)
print(got)

print('creando user')
user1 = user.UserActions()
print(user1.Name)
print(user1.createPipeline())
print(user1.getMyPipelinesNames())
print('Select pipe')
print(user1.selectPipeline(0))
print(user1.getActualPipe())
print(user1.getActualPipe().Name)
print('Add Step')
print(user1.addStep(got,0))
print(user1.getActualPipe().steps())
print(user1.delPipeline(0))

# manager = mo.ManageTransformations()
# a=manager.getAlgorithm('Linear Regression')
# b=manager.getAlgorithm('Linear Regression')
# print(type(a))
# print(type(b))
# print(a)
# print(a)
# print(a==b)
# print(a is b)

