class ManagerModel:
	def __new__(cls, model):
		if not hasattr(cls, 'instance'):
			cls.instance = super(ManagerModel, cls).__new__(cls)
			
		return cls.instance

	def __init__(self, model):
		self._model = model

	def get_model_instance(self):
		return self._model
