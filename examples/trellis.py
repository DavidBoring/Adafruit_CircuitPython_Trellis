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
print('Turning all LEDs on...')
trellis.led.fill(True)
time.sleep(1)

trellis.led[1] = True
trellis.led[2] = True
trellis.led[3] = True
trellis.led[4] = True
time.sleep(1)
trellis.led.fill(True)

trellis.led[5] = True
trellis.led[6] = True
trellis.led[7] = True
trellis.led[8] = True
time.sleep(1)