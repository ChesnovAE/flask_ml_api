from abc import ABC, abstractclassmethod


class BaseModel(ABC):
    def __init__(self, params):
        self.params = params
    
    @abstractclassmethod
    def fit(self, xtrain, ytrain):
        pass
    
    @abstractclassmethod
    def predict(self, xtest):
        pass


class MyCustomModel(BaseModel):
    def fit(self, xtrain, ytrain):
        raise NotImplementedError
    
    def predict(self, xtest):
        raise NotImplementedError
