import pygame

class Level:
	def __init__(self, masterSurface):
		self.elements = []
		self.displaySurface = masterSurface
		self.running = True
		
	def Pause(self):
		self.running = False
		# We use copy so that we save a separate instance of the surface. That way, it 
		# can't be modified by another level.
		self.savedSurface = copy(masterSurface)
	
	def OnEvent(self, event):
		self.HandleEvent(event)
		
		for element in self.elements:
			element.OnEvent(event)
	
	def HandleEvent(self, event):
		if event == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	def Animate(self):
		# Animate each element
		for element in self.elements:
			element.Animate()
		
		# Apply the results of the animation to the other affected elements in the
		# level. E.g., if a freeze animation causes an area of elements to get frozen, 
		# apply the freeze status to the other elements in the affected area.
		for element in self.elements:
			for animationResult in element.GetAnimationResults():
				self.ApplyAnimationResult(animationResult)
				
	def ApplyAnimationResult(self, newStatus):
		# Check each element in turn for whether it is in the range of the newStatus. 
		# This can be optimized somehow!
		for element in self.elements:
			element.SetNewStatus(newStatus)
	
	def Draw(self):
		self.displaySurface.fill((255,255,255)) # We should have a global level size attribute
		for element in self.elements:
			if element.Changed():
				# We also want to add the pixels to dirtyrects, but we need a way to get
				# the position it was at BEFORE animation as well. Then we can just draw
				# the changed spaces rather than the whole screen.
				element.Draw(self.displaySurface)
		pygame.display.update()
			
	def AddElement(self, element):
		self.elements.add(element)
			
	def Execute(self):
		while(self.running == True):
			for event in pygame.event.get():
				self.OnEvent(event)
			self.Animate()
			self.Draw()
			