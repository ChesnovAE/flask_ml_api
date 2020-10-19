from abc import ABC, abstractclassmethod
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from typing import Union, Dict


class BaseModel(ABC):
    def __init__(self, params, model=None):
        self.params = params
        if self.params:
            self.model = model(**self.params['model_params'])
        else:
            self.model = model()
    
    @abstractclassmethod
    def fit(self, xtrain, ytrain):
        raise NotImplementedError
    
    @abstractclassmethod
    def predict(self, xtest):
        raise NotImplementedError


class LogisticModel(BaseModel):
    def __init__(self,
                 params: Dict,
                 model=LogisticRegression) -> None:
        super().__init__(params, model)
    
    def fit(self,
            xtrain: Union[pd.DataFrame, np.array],
            ytrain: Union[pd.DataFrame, np.array]) -> None:
        self.model.fit(xtrain, ytrain)
    
    def predict(self,
                xtest: Union[pd.DataFrame, np.array]) -> np.array:
        return self.model.predict(xtest)
