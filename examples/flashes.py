import time
import busio
from board import SCL, SDA
from adafruit_trellis import Trellis

# Create the I2C interface
i2c = busio.I2C(SCL, SDA)

# Create a Trellis object
trellis = Trellis(i2c)  # 0x70 when no I2C address is supplied

# 'auto_show' defaults to 'True', so anytime LED states change,
# the changes are automatically sent to the Trellis board. If you
# set 'auto_show' to 'False', you will have to call the 'show()'
# method afterwards to send updates to the Trellis board.

# Turn on every LED
def innerOuter(times):
    for i in range(times):
        print('Turning all LEDs off...')
        trellis.led.fill(False)

        print('Flash outer buttons')
        trellis.led[0] = True
        trellis.led[1] = True
        trellis.led[2] = True
        trellis.led[3] = True
        trellis.led[4] = True
        trellis.led[7] = True
        trellis.led[8] = True
        trellis.led[11] = True
        trellis.led[12] = True
        trellis.led[13] = True
        trellis.led[14] = True
        trellis.led[15] = True
        time.sleep(.1)
        trellis.led.fill(False)
        # time.sleep(.1)

        print('Flush inner buttons')
        trellis.led[5] = True
        trellis.led[6] = True
        trellis.led[9] = True
        trellis.led[10] = True
        time.sleep(.1)
        trellis.led.fill(False)
        # time.sleep(.1)
