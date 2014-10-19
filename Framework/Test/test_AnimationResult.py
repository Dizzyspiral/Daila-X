import pytest
from AnimationResult import AnimationResult

def test_Constructor():
	a = AnimationResult()
	assert True
	
def test_Setting_Status():
	a = AnimationResult()
	a.SetStatus(1, True)
	assert True
	
def test_Getting_Status():
	a = AnimationResult()
	a.SetStatus(1, True)
	assert a.statusType == 1
	assert a.statusEnabled == True
	
def test_Setting_Area():
	a = AnimationResult()
	a.SetArea(1,2,3,4)
	assert a.area.left == 1
	assert a.area.top == 2
	assert a.area.width == 3
	assert a.area.height == 4
	
def test_Setting_X():
	a = AnimationResult()
	a.SetX(1)
	assert a.GetX() == 1
	
def test_Setting_Y():
	a = AnimationResult()
	a.SetY(1)
	assert a.GetY() == 1
	
