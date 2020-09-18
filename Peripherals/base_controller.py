from base.py import Base


# Physical attributes of robot
CM_PER_STEP = 0.079528
STEPS_PER_CM = 12.5741877
BASE_WIDTH_CM = 12.0

class BaseController(self, parent):
    def __init__(self, parent):
        _parent = parent
        _base = Base(self)
        
    def DriveCM(self, distance):
        # drive in a straight line
        
        if distance < 0:
            base.MoveLeft(-1, distance * STEPS_PER_CM, 1)
            base.MoveRight(-1, distance * STEPS_PER_CM, 1)
        if distance > 0:
            base.MoveLeft(1, distance * STEPS_PER_CM, 1)
            base.MoveRight(1, distance * STEPS_PER_CM, 1)
        
    def TurnInPlaceAngle(self, angle):
        # correct angle to range 0-360, in case it was a negative angle
        correctedangle = (angle + 360) % 360
        
        # indicates a left hand turn
        if correctedangle > 180: 
            base.MoveLeft()
            base.MoveRight()
        # indicates a right hand turn
        else:
            base.MoveLeft()
            base.MoveRight()
            
    def Coast(self):
        base.ReleaseLeft()
        base.ReleaseRight()
