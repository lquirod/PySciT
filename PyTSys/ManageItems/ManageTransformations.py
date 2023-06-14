import Enumerations as Enum
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
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
                return ['MinMax scaling', MinMaxScaler()]
          
        return None
            




