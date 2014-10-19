from Keybindings import Keybindings
from EntityStatus import EntityStatus
from StatusEnum import StatusEnum
import pygame

class Entity():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.image = None
		self.animationSet = []
		self.animationResults = [] # A list of AnimationResult objects
		self.keybindings = Keybindings()
		self.status = EntityStatus()
		self.changed = True # Tells the level whether to redraw this element or not
	
	@classmethod
	def Animate(cls, self):
		"""Performs all of the animations currently registered to this object and 
		stores the results of those animations which affect objects OTHER than self in 
		animationResults, so that these results can be grabbed by the Level that this 
		entity belongs to.
		"""
		self.animationResults = [] # Clear out any results from the previous animation
		# Set changed to false. If an animation runs, changed will be set to True
		self.changed = False
		
		for animation in self.animationSet:
			# This gets set every time an animation is run... that's probably inefficient,
			# but is it worse than checking self.animationSet.count > 0?
			self.changed = True
			animation.Run()
			animation.ApplyFrame(self.image) # Adds the animation's current frame to the Entity's image
			result = animation.GetResult()
			
			# If there is some kind of ADDITIONAL change to the level, beyond just the 4
			# element that was animated, we adjust the result to have the correct 
			# coordinates (relative to the element that it came from) and add it to the 
			# queue of results to be processed later.
			if result.indicatesChange():
				result.SetX(result.GetX() + self.x)
				result.SetY(result.GetY() + self.y)
				self.animationResults.add(result)
		
	@classmethod
	def GetAnimationResults(self):
		"""Get the results of the latest animation. The results come in the form of a 
		list of AnimationResult objects.
		"""
		return self.animationResults

	@classmethod
	def Draw(self, canvas):
		"""Draws self onto the specified canvas."""
		pass # Draw self.image

	@classmethod
	def OnEvent(self, event):
		"""Handles events."""
		if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			keybindings.RunAction(event.key, event.type)

	@classmethod
	def StartAnimation(self, animation):
		"""Adds animation to the list of animations to be performed on the next Animate()
		call.
		"""
		animationSet.add(animation)

	@classmethod
	def StopAnimation(self, animation):
		"""Removes animation from the list of animations to be performed on the next 
		Animate() call.
		"""
		animationSet.remove(animation)

	@classmethod
	def SetPosition(self, x, y):
		"""Sets the new position of self"""
		self.x = x
		self.y = y

	@classmethod
	def AdjustPosition(self, x, y):
		"""Adjusts the position of self"""
		self.x += x
		self.y += y
		
	@classmethod
	def SetNewStatus(self, animationResult):
		"""Takes an AnimatonResult object and determines if this result applies to self. 
		If it does, self.status is modified accordingly.
		"""
		if self._IsInRange(self.x, animationResult.area.x, animationResult.area.x + animationResult.area.width) and self._IsInRange(self.y, animationResult.area.y, animationResult.area.y + animationResult.area.height):
			self.status.SetStatus(animationResult.statusType, animationResult.statusEnabled)

	@classmethod
	def Changed(self):
		return self.changed
	
	@classmethod
	def _IsInRange(self, coord, rangeStart, rangeEnd):
		"""Determines if coord is in the range of rangeStart, rangeEnd"""
		return coord > rangeStart and coord < rangeEnd
		