# # This program prints Hello, world!
# print('Hello, world!')

# Create random numbers
# import numpy as np
# ran_data = np.random.randint(5, 25, (10, 2))
# print(ran_data) # Get value with array[1], matriz[3,0]

# # And doing Min Max Scaler
# from sklearn.preprocessing import MinMaxScaler
# sc_model = MinMaxScaler ()
# sc_model.fit_transform (ran_data)
# print("Model: " + sc_model)
# print("\n Now scalated values :\n"+sc_model.fit_transform (ran_data))

# #  Define linear regression model. The below dataset will fit into the three datasets for predicting
# # the unknown data value, which was included in the existing data set as follows.
# from sklearn import linear_model
# lreg = linear_model.LinearRegression ()
# lreg.fit ([[0,0], [5,-5],[-7,7]],[0,5,7])
# print (lreg.coef_)

# # Loading iris dataset and digits dataset
# from sklearn import datasets
# data_iris = datasets.load_iris()
# print ("Iris Data")
# print (data_iris.data)
# data_digi = datasets.load_digits()
# print ("Digits Data")
# print (data_digi.data)

# # Iimporting svm module and defining svc
# from sklearn import svm
# data_digi.target
# cf = svm.SVC (gamma=0.001, C=100.)
# cf.fit (data_digi.data [:-1], data_digi.target [:-1])

# from tkinter import Tk     # from tkinter import Tk for Python 3.x
# from tkinter.filedialog import askopenfilename
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print("This filename is in: \""+filename+"\" path")
# import sys
# sys.stdin = open(filename, 'r')
# nombre = input("¿Cómo se llama? ")
# print(f"Me alegro de conocerle, {nombre}")
# nombre = input("¿Y apellido? ")
# print(f"k grasioso sos, {nombre}")

# f = open(filename, 'r')
# print(f.read(8))
# print(f.readline())

# for x in f:
#     print(x)
# f.close()

# import csv
# with open(filename) as csv_file: # no need to close file with bc it does automatically at the end
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# print("Select lines form")
# # Select lines
# data = []
# with open(filename,"r") as f:
#     data = f.readlines() # readlines() returns a list of items, each item is a line in your file
# print("one"+data[5]) # print line 5
# for i in range(3, 5): # 3 and 4; not include 5 in range
#     print(data[i])

# print("other Form")
# # You could try to use enumerate and then check for the line number: Note that i starts at i so i == 4 matches the 5th line.
# with open(filename) as f:
#     for i, line in enumerate(f):
#         if i == 2:
#             print(line.strip()) # strip removes begin and end spaces blank
#         if 5 < i < 8:
#             print(line.strip())

# # Should I do:
# def func(file):
#   file.write(...)
# with open(file_path, 'w') as file:
#   func(file)
# # ...or :
# def func(file_path):
#   with open(file_path, 'w') as file:
#     file.write(...)
# func(file_path)

from sklearn import tree
from sklearn.model_selection import train_test_split
X=[[165,19],[175,32],[136,35],[174,65],[141,28],[176,15],
[131,32],[166,6],[128,32],[179,10],[136,34],[186,2],[126,25],
[176,28],[112,38],[169,9],[171,36],[116,25],[196,25], [196,38],
 [126,40], [197,20], [150,25], [140,32],[136,35]]
Y=['Man','Woman','Woman','Man','Woman','Man','Woman','Man','Woman','Man','Woman','Man','Woman','Woman','Woman','Man','Woman','Woman','Man', 'Woman', 'Woman', 'Man', 'Man', 'Woman', 'Woman']
data_feature_names = ['height','length of hair']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
DTclf = tree.DecisionTreeClassifier()
DTclf = DTclf .fit(X,Y)
prediction = DTclf.predict([[135,29]])
print(prediction)
probab = DTclf.predict_proba([[135,29]])
print(probab)

cantidad = int(input("Dígame una cantidad en pesetas: "))
print(f"{cantidad} pesetas son {round(cantidad / 166.386, 2)} euros")




# import Person as p
# person1 = p.person('Anna', 20, 'Female')
# person1.person_details()

# class person:
 
#   def __init__(self,name,age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
 
#   def person_details(self):
#     print(f'Person Name: {self.name} \nPerson Age: {self.age} \nPerson Gender: {self.gender}\n')

# Tomar nombre params
inspect.getfullargspec(a_method)
# Ejecutar
# Use the built-in getattr() function:
class Foo:
    def bar1(self):
        print(1)
    def bar2(self):
        print(2)

def call_method(o, name):
    return getattr(o, name)()


f = Foo()
call_method(f, "bar1")  # prints 1
# You can also use setattr() for setting class attributes by names.










