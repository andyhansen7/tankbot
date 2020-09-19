from base.py import Base

class BaseController(self, parent):
    def __init__(self, parent):
        _parent = parent
        _base = Base(self)
        
    # Physical attributes of robot
    CM_PER_STEP = 0.079528
    STEPS_PER_CM = 12.5741877

    BASE_WIDTH_CM = 14.2
    PI = 3.141592653589
        
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
        corrected_angle = (angle + 360) % 360
        
        turn_radius = (angle / 360) * (2 * PI * BASE_WIDTH_CM)
        
        # indicates a left hand turn
        if corrected_angle > 180: 
            base.MoveLeft(-1, turn_radius * STEPS_PER_CM, 1)
            base.MoveRight(1, turn_radius * STEPS_PER_CM, 1)
        # indicates a right hand turn
        else:
            base.MoveLeft(1, turn_radius * STEPS_PER_CM, 1)
            base.MoveRight(1, turn_radius * STEPS_PER_CM, 1)
            
    def Coast(self):
        base.ReleaseLeft()
        base.ReleaseRight()
