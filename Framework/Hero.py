from Creature import Creature
import pygame # This is only needed for color, which is only needed for testing right now

class Hero(Creature):
	def __init__(self):
		super().__init__()

		self.speed = 10
		self.color = pygame.Color("red")
		self.x = 0
		self.y = 0
		self.width = 20
		self.height = 20
		
		self.keybindings.Add(pygame.K_LEFT, pygame.KEYDOWN, lambda: self.StartAnimation(self.WalkLeft))
		self.keybindings.Add(pygame.K_RIGHT, pygame.KEYDOWN, lambda: self.StartAnimation(self.WalkRight))
		self.keybindings.Add(pygame.K_LEFT, pygame.KEYUP, lambda: self.StopAnimation(self.WalkLeft))
		self.keybindings.Add(pygame.K_RIGHT, pygame.KEYUP, lambda: self.StopAnimation(self.WalkRight))
	
	def WalkLeft(self):
		self.x -= self.speed
		
	def WalkRight(self):
		self.x += self.speed
	
	def Jump(self):
		pass
		
	def Attack(self):
		pass
		
	def Draw(self, canvas):
		canvas.fill(self.hero.color, pygame.Rect(self.hero.x, self.hero.y, self.hero.width, self.hero.height))