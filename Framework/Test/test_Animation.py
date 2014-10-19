import pytest
from pygame import Rect
from Animation import Animation

def test_Constructor_With_Empty_Frames_List():
	a = Animation([])
	assert True
	
def test_Constructor_With_Frames_List():
	# We can test with a frames list that doesn't contain actual images because the 
	# function accepts any list. This is not ideal - we really want it to only 
	# accept images
	a = Animation([1,2,3,4])
	assert True

def test_Constructor_With_Frames_And_Run_Action():
	a = Animation([1,2,3,4], lambda: 0)
	
def test_Constructor_With_Run_Action_And_Empty_Frames():
	a = Animation([], lambda: 0)

def test_Can_Set_And_Get_Animation_Result():
	a = Animation([])
	a.SetResult(Rect(25, 50, 10, 10), 1, True)

def test_Cannot_Run_With_Empty_Frames_List():
	a = Animation([])
	with pytest.raises(IndexError):
		a.Run()
	
def test_Can_Run_With_Frame_List():
	a = Animation([1,2,3])
	a.Run()
	assert True
	
def test_Is_Marked_For_Deletion_After_Animation_Complete():
	a = Animation([1,2,3])
	assert a.markedForDeletion == False
	a.Run() # Frame 1
	assert a.markedForDeletion == False
	a.Run() # Frame 2
	assert a.markedForDeletion == False
	a.Run() # Frame 3
	assert a.markedForDeletion == True
	
def test_Will_Loop_If_Marked_For_Looping():
	a = Animation([1,2,3])
	a.SetLooping(True)
	assert a.currentFrame == 0
	a.Run()
	assert a.currentFrame == 1
	a.Run()
	assert a.currentFrame == 2
	a.Run()
	assert a.currentFrame == 0
	
def test_Can_Get_Empty_Result_If_Result_Not_Set():
	a = Animation([])
	r = a.GetResult() # What can we do to test if result is empty?
	assert r.indicatesChange == False

def test_Can_Get_Result_After_It_Is_Set():
	a = Animation([])
	a.SetResult(Rect(1,2,3,4), 1, True)
	r = a.GetResult()
	assert r.area == Rect(1,2,3,4)
	assert r.statusType == 1
	assert r.statusEnabled == True
	
def test_Can_Pause():
	a = Animation([])
	assert a.running == True
	a.Pause()
	assert a.running == False
	
def test_Can_Resume():
	a = Animation([])
	assert a.running == True
	a.Pause()
	assert a.running == False
	a.Resume()
	assert a.running == True