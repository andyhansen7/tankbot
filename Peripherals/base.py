import time
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

class Base():
    def __init__(self):
        
        # Motor setup
        self.kit = MotorKit()
        self.left_motor = self.kit.stepper1
        self.right_motor = self.kit.stepper2
        
        
        self.left_motor.release()
        self.right_motor.release()
    
        # Direction:
        # -1: Reverse
        #  1: Forward
        
        self.direction_switch = {
            -1: stepper.FORWARD,
            1: stepper.BACKWARD
        }
        
        # Style:
        # 0: Single coil steps
        # 1: Double coil steps
        # 2: Interleaved steps
        # 3: Micro steps
            
        # Returns true on sucess, false on error
            
        self.style_switch = {
            0: stepper.SINGLE,
            1: stepper.DOUBLE,
            2: stepper.INTERLEAVE,
            3: stepper.MICROSTEP
        }
        
    def MoveLeft(self, direction, steps, style):
        for i in steps:
            self.left_motor.onestep(direction = self.direction_switch.get(direction, stepper.SINGLE), style = self.style_switch.get(style, stepper.FORWARD))
            
    def MoveRight(self, direction, steps, style):
        for i in steps:
            self.right_motor.onestep(direction = self.direction_switch.get(direction, stepper.SINGLE), style = self.style_switch.get(style, stepper.FORWARD))
                
    def ReleaseLeft(self):
        self.left_motor.release()
            
    def ReleaseRight(self):
        self.right_motor.release()