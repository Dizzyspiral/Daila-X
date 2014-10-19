from AnimationResult import AnimationResult

class Animation():
	"""Contains the state information and frames for an animation.
	
	Each animation is specific to the object it is animating. An animation for 
	a box cannot be used for a person, and vice versa. This is because the frame 
	that is returned has information that is specific to the type of object that 
	owns it. In particular, it contains information about what part of that 
	object changed and an image reflecting that change. This is so that the 
	object knows what to render and where to render it.
	"""
	def __init__(self, frames, runAction = lambda: 0):
		"""Initialize the animation"""
		self.currentFrame = 0
		self.frameList = frames
		self.numFrames = len(self.frameList)
		self.animate = runAction
		self.animationResult = AnimationResult()
		self.markedForDeletion = False
		self.loop = False
		self.running = True
		
	def Run(self):
		"""Advances the animation by one frame.
		
		return: The image for the current state of whatever is being animated
		"""
		if self.running == True:
			# Perform an action associated with the animation. For example, if the 
			# character is walking, this action would be adjusting the character's 
			# position
			self.animate()
			
			# Return the image and information about where/how it should be rendered
			frame = self.frameList[self.currentFrame]
			
			# Increment the frame. Check if we've hit the end of the animation; if 
			# we have, we either need to loop back over it, or mark this animation 
			#for deletion.
			self.currentFrame += 1
			
			if self.currentFrame >= self.numFrames:
				if self.loop == True:
					self.currentFrame = 0
				else:
					# Currently, there is no scheme for deleting animations once 
					# they're completed. This should be taken care of in Entity after
					# animations have been run... some kind of clean up routine.
					self.markedForDeletion = True
			
			# Only return a frame if the animation ran. The Entity that called this 
			# animation can deal with the Null case.
			return frame
	
	def Pause(self):
		self.running = False
		
	def Resume(self):
		self.running = True
		
	def SetLooping(self, loop):
		self.loop = loop
	
	def SetResult(self, area, statusType, statusEnabled):
		"""This method is used on setup of the animation to tell the animation 
		object what it should say the status of the level is after this animation 
		has been run. If SetResult() is never called, the result collected from 
		this animation will indicate that there is no change to the other entities 
		on the level (but the entity that owns this animation can still change).
		
		xDistance: The X distance away from the entity that this result takes effect
		yDistance: The Y distance away from the entity that this result takes effect
		width: The width of the effect (X length)
		height: The height of the effect (Y length)
		statusIndex: The identifier of the status effect, from StatusEnum
		status: The value of the status (True/False)
		"""
		self.animationResult.area = area
		self.animationResult.SetStatus(statusType, statusEnabled)
		
	def GetResult(self):
		"""Gets the result of the animation. This will be the same for every time 
		the animation is run.
		"""
		return self.animationResult
		