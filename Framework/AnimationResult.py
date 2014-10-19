from StatusEnum import StatusEnum # Is this actually used?
from pygame import Rect

class AnimationResult():
	"""Contains information about status changes to the level after an animation 
	has been run. Currently, only one change per animation is supported. If 
	animations require the ability to report multiple status changes, a list of 
	these objects can be implemented as a return from Animation.GetResult()
	"""
	def __init__(self):
		self.area = Rect(0,0,0,0)
		self.statusType = -1 # Invalid status, indicates status not set
		self.statusEnabled = False
		# This will only be set to true if SetStatus was called. This way, code 
		# processing AnimationResults can tell when it is dealing with an empty 
		# AnimationResult and quit processing it.
		self.indicatesChange = False
	
	def SetStatus(self, statusType, statusEnabled):
		self.statusType = statusType
		self.statusEnabled = statusEnabled
		self.indicatesChange = True
		
	def SetArea(self, left, top, x, y):
		self.area = Rect(left, top, x, y)
		
	# These methods are used for determining if an entity is within the range of the
	# effect.
	
	def GetX(self):
		return self.area.x
		
	def GetY(self):
		return self.area.y
		
	# These methods are used for adjusting X after this AnimationResult has reached the
	# entity that the Animaton who owns this result belongs to (does that make sense?)
	#
	# AnimationResult -> Animation -> Entity -> Level
	#                                 ------
	# When it reaches the Entity, this is the first time that the X, Y information of 
	# the entity that the animation was performed on is available. This X, Y information 
	# is then added to this result before it is passed up to Level, which uses this 
	# result to affect other Entities on the level.
		
	def SetX(self, x):
		self.area.x = x
		
	def SetY(self, y):
		self.area.y = y
	