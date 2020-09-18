import time
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

class Base(self, parent):
    def __init__(self, parent):
        _parent = parent
        kit = MotorKit(i2c=board.I2C())
        
        kit.stepper1.release()
        kit.stepper2.release()
        
    def MoveLeft(self, direction, steps, style):
        # Direction:
        # -1: Reverse
        #  1: Forward
        
        # Style:
        # 0: Single coil steps
        # 1: Double coil steps
        # 2: Interleaved steps
        # 3: Micro steps
        
        # Returns true on sucess, false on error
        
        direction_switch = {
            -1: stepper.FORWARD,
             1: stepper.REVERSE
        }
        
        style_switch = {
            0: stepper.SINGLE,
            1: stepper.DOUBLE,
            2: stepper.INTERLEAVE,
            3: stepper.MICROSTEP
        }
        
        for i in steps:
            kit.stepper1.onestep(direction = direction_switch.get(direction, stepper.SINGLE), style = style_switch(style, stepper.FORWARD))
            
        def MoveRight(self, direction, steps, style):
            # Direction:
            # -1: Reverse
            #  1: Forward
            
            # Style:
            # 0: Single coil steps
            # 1: Double coil steps
            # 2: Interleaved steps
            # 3: Micro steps
            
            direction_switch = {
                -1: stepper.FORWARD,
                1: stepper.REVERSE
            }
            
            style_switch = {
                0: stepper.SINGLE,
                1: stepper.DOUBLE,
                2: stepper.INTERLEAVE,
                3: stepper.MICROSTEP
            }
            
            for i in steps:
                kit.stepper2.onestep(direction = direction_switch.get(direction, stepper.SINGLE), style = style_switch(style, stepper.FORWARD))
                
        def ReleaseLeft(self):
            kit.stepper1.release()
            
        def ReleaseRight(self):
            kit.stepper2.release()