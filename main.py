from FirstLevel import FirstLevel
import pygame

if __name__ == "__main__" :
	print("Initializing pygame")
	pygame.init()
	print("Getting the master surface")
	masterSurface = pygame.display.set_mode([1000, 600]) # Default size should be put in a file somewhere
	print("Creating the first level")
	firstLevel = FirstLevel(masterSurface)
	print("Starting First Level")
	firstLevel.Execute()