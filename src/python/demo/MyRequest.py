import grongier.pex

class MyRequest(grongier.pex.Message):

	def __init__(self, req=None):
		super().__init__()
		self.requestString = req