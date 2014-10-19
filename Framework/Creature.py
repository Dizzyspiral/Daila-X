from Entity import Entity
import pygame

class Creature(Entity):
	def WalkLeft(self):
		self.x -= self.speed
		
	def WalkRight(self):
		self.x += self.speed

	def __init__(self):
		super().__init__()
		self.keybindings.Add(pygame.K_LEFT, pygame.KEYDOWN, lambda: self.StartAnimation(WalkLeft))
		self.keybindings.Add(pygame.K_RIGHT, pygame.KEYDOWN, lambda: self.StartAnimation(WalkRight))
		self.keybindings.Add(pygame.K_LEFT, pygame.KEYUP, lambda: self.StopAnimation(WalkLeft))
		self.keybindings.Add(pygame.K_RIGHT, pygame.KEYUP, lambda: self.StopAnimation(WalkRight))