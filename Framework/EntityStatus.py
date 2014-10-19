from StatusEnum import StatusEnum

class EntityStatus():
	def __init__(self):
		self.statusInformation = [False] * StatusEnum.numEntries
		
	def SetStatus(self, index, status):
		self.statusInformation[index] = status
		
	def IsOnFire(self):
		return self.statusInformation[StatusEnum.onFire]
		
	def IsFrozen(self):
		return self.statusInformation[StatusEnum.frozen]
		
	def IsSolid(self):
		return self.statusInformation[StatusEnum.solid]
		
	def IsMovable(self):
		return self.statusInformation[StatusEnum.movable]
	
	def IsFlammable(self):
		return self.statusInformation[StatusEnum.flammable]
	
	def IsFreezable(self):
		return self.statusInformation[StatusEnum.freezable]