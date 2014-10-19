import pytest
from Entity import Entity

def test_IsInRange_Too_Great():
	e = Entity()
	assert e._IsInRange(4, 1, 3) == False
	
def test_Coord_Is_No_In_Range_When_Less_Than_Lower_Bound():
	e = Entity()
	assert e._IsInRange(1, 2, 3) == False
	
def test_Coord_Is_Not_In_Range_When_Equal_To_Upper_Bound():
	e = Entity()
	assert e._IsInRange(3, 2, 3) == False
	
def test_Coord_Is_Not_In_Range_When_Equal_To_Lower_Bound():
	e = Entity()
	assert e._IsInRange(2, 2, 3) == False
	
def test_Coord_Is_Not_In_Range_When_Greater_Than_Upper_Bound():
	e = Entity()
	assert e._IsInRange(4, 1, 3) == False
	
def test_Coord_Is_In_Range_When_Between_Bounds():
	e = Entity()
	assert e._IsInRange(2, 1, 3) == True
	
def test_Changed_Is_False_If_No_Animations_Run():
	e = Entity()
	Entity.Animate(e)
	assert e.changed == False
	
def test_Animation_Frame_Is_Applied_To_Entity_Image():
	pass
	
def test_Results_From_Animation_Are_Added_To_Animation_Results_List():
	pass
	
def test_Will_Adjust_Animation_Result_X_Y():
	pass

def test_Draw_Will_Add_Image_To_Canvas_At_Correct_Position():
	pass
	
def test_Key_Presses_Can_Trigger_Events():
	pass
	
def test_Key_Releases_Can_Trigger_Events():
	pass
	
def test_Keys_That_Are_Not_Registered_Will_Not_Trigger_Events_When_Pressed():
	pass
	
def test_Can_Start_New_Animation():
	pass
	
def test_Can_Stop_Existing_Animation():
	pass
	
def test_Animations_Will_Run_Until_Stopped_Or_Finished():
	pass
	
def test_Can_Set_X_Y_Position():
	e = Entity()
	e.SetPosition(10, 20)
	assert e.x == 10
	assert e.y == 20
	
def test_Can_Adjust_X_Y_Position_Relative_To_Current_Position():
	e = Entity()
	e.SetPosition(10, 20)
	assert e.x == 10
	assert e.y == 20
	e.AdjustPosition(1,2)
	assert e.x == 11
	assert e.y == 22
	
def test_Can_Change_Status_With_Animation_Result():
	pass
	
def test_Status_Will_Not_Change_If_Animation_Result_Has_Same_Status_As_Entity():
	pass
	
def test_Can_Tell_You_If_It_Has_Changed():
	pass
	
def test_Can_Determine_If_Another_Entity_Is_Occupying_The_Same_Space():
	pass