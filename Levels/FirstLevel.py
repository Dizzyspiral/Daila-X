from Level import Level
from Hero import Hero

class FirstLevel(Level):
	def __init__(self, masterSurface):
		super().__init__(masterSurface)
		self.elements.append(Hero())