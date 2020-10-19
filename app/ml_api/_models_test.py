import unittest
from .models import LogisticModel, BaseModel
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class TestLogisticModel(unittest.TestCase):
    def test_abstract_model_class(self):
        x = []
        self.assertRaises(NotImplementedError, BaseModel.fit, x, x)
        self.assertRaises(NotImplementedError, BaseModel.predict, x)
    
    
    def test_init_function_with_params(self):
        params = {
            'some_param': 12,
            'model_params': {'C': 10}
        }
        lm = LogisticModel(params)
        self.assertEqual(params, lm.params)
        self.assertEqual(params['model_params']['C'], lm.model.C)
    
    def test_init_function_without_params(self):
        params = {}
        lm = LogisticModel(params)
        self.assertEqual(params, lm.params)
        self.assertEqual(1.0, lm.model.C)
    
    def test_fit_predict_function(self):
        iris = datasets.load_iris()
        x_train, x_test, y_train, y_test = train_test_split(iris.data,
                                                            iris.target,
                                                            random_state=1011)
        
        lm = LogisticModel({'model_params': {'C': 2}})
        lm.fit(x_train, y_train)
        
        preds = lm.predict(x_test)
        
        self.assertGreaterEqual(accuracy_score(y_test, preds), 0.95)
