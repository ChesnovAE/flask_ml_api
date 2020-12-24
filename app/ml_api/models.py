from abc import ABC, abstractclassmethod
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from typing import Union, Dict
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image


class BaseModel(ABC):
    def __init__(self, params, model=None):
        self.params = params
        if params and model:
            self.model = model(**self.params['model_params'])
    
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


class StyleTransferModel(BaseModel):
    def __init__(self,
                 params: Dict,
                 model=None) -> None:
        super().__init__(params, model)
        if self.params['load_pretrained']:
            self._load_pretrained_model()
    
    def fit(self, xtrain, ytrain):
        pass

    def _tensor_to_image(self, tensor):
        tensor = tensor * 255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor) > 3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)

    def _load_img(self, path_to_img: str):
        max_dim = 512
        img = tf.io.read_file(path_to_img)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)

        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img

    def _load_pretrained_model(self) -> None:
        self.model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    
    def predict(self, content_image_pth: str, style_image_pth: str, save_path: str) -> None:
        content_image = self._load_img(content_image_pth)
        style_image = self._load_img(style_image_pth)
        stylized_image = self.model(tf.constant(content_image), tf.constant(style_image))[0]
        stylized_image = self._tensor_to_image(stylized_image)
        stylized_image.save(save_path)
