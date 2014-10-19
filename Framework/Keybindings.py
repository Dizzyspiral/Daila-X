from collections import defaultdict
import pygame

# The purpose of this function is to provide a standard way to add key events to an 
# Entity. This class provides two separate lists, keyUpBindings and keyDownBindings, 
# which represent what to do depending on which state the key is in. It also 
# provides a mechanism for getting the action stored for a particular key and state,
# or for running the action associated with a key and state. Each entity should
# include this class and use it for storing keybindings. Any keybinding added to
# this class within an entity will run when the event criteria are met.

def EmptyFn():
	"""This is just used as a no-op for keybindings that don't exist. That way, when an
	Entity goes looking for an action based on a key event, if that key event isn't 
	registered here we can return this function to it or run this function, making it do 
	nothing. It is the keybinding equivalent of a null value.
	"""
	pass

class Keybindings:

	def __init__(self):
		self.keyUpBindings = defaultdict(lambda: EmptyFn)
		self.keyDownBindings = defaultdict(lambda: EmptyFn)
		self.keybindings = {pygame.KEYDOWN : self.keyDownBindings, pygame.KEYUP : self.keyUpBindings}
		
	def GetAction(self, key, state):
		return self.keybindings[state][key]
		
	def RunAction(self, key, state):
		self.keybindings[state][key]()
		
	def Add(self, key, state, action):
		self.keybindings[state][key] = action