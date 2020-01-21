import time
import busio
from board import SCL, SDA
from adafruit_trellis import Trellis
import flashes

# Create the I2C interface
i2c = busio.I2C(SCL, SDA)

# Create a Trellis object
trellis = Trellis(i2c)  # 0x70 when no I2C address is supplied

# 'auto_show' defaults to 'True', so anytime LED states change,
# the changes are automatically sent to the Trellis board. If you
# set 'auto_show' to 'False', you will have to call the 'show()'
# method afterwards to send updates to the Trellis board.

def switchLED(buttonNumber):
    if trellis.led[buttonNumber] == True:
        print('Button: ' + buttonNumber + ' turned off')
        return False
    else:
        return True
        print('Button: ' + trellis.led[buttonNumber] + ' turned on')


# Turn on every LED
flashes.innerOuter(2)
time.sleep(.5)
print('Starting button sensory loop...')
pressed_buttons = set()
while True:
    time.sleep(.1)
    just_pressed, released = trellis.read_buttons()
    for buttonNumber in just_pressed:
        print('pressed:', buttonNumber)
        newState = switchLED(buttonNumber)
        trellis.led[buttonNumber] = newState

