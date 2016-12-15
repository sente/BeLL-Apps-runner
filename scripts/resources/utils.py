

class HashableList(list):
	'A hashable wrapper around the standard list.'

	def __init__(self, l):
		self.list = tuple(l)
	def __str__(self):
		return str(self.list)
	def __hash__(self):
		return hash(self.list)
	def __len__(self):
		return len(self.list)
	def __getitem__(self, i):
		return self.list[i]
	def __iter__(self):
		return iter(self.list)
