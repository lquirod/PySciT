import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from PySciT import Enumerations as Enum

# sc_model = MinMaxScaler ()
# sc_model.fit_transform (ran_data)

class ManageTransformations:
    def __init__(self):
        pass

    def getTransformationsList(self):
        return  [alg.name for alg in Enum.TR.Transformations]

    def thereIsTransformation(self, nameTransformation):
        return True if nameTransformation in Enum.TR.Transformations.__members__ else False
    
    def getTransformation(self, nameTransformation):
        if self.thereIsTransformation(nameTransformation):
            if nameTransformation == Enum.TR.Transformations.MinMax_Scaling.name:
                return ['MinMax_Scaling', MinMaxScaler()]
            # elif nameTransformation == Enum.TR.Transformations.Print_data.name:
            #     return ['Print_data', Print_data()]
                    
        return None
            

# # Custom transformation to print intermediate data
# from sklearn.base import BaseEstimator, TransformerMixin
# class Print_data(BaseEstimator, TransformerMixin):

#     def transform(self, X):
#         self.shape = X.shape
#         return X

#     def fit(self, X, y=None, **fit_params):
#         return self

