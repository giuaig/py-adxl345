#!/usr/bin/env python

# This sample print acceleration value on all 3 axes every second

import time
from adxl345.i2c import ADXL345

def main():
  # Standard address 0x1D with 'alternate=False' or alternate address 0x53 with 'alternate=True'. Use 'sudo i2cdetect -y 1'.
  adxl = ADXL345(alternate=True)
  deviceId = adxl.get_device_id()
  print("ADXL DeviceID: " + str(deviceId))

  # Set data rate at about 8 hz
  rate_hz = adxl.set_data_rate(8, 1)
  print("Rate: " + str(rate_hz) + " hz")

  # Select Range
  adxl.set_range(16, True)

  # Turn off sleep mode (default when powered)
  adxl.power_on()

  # Indefinitely print acceleration measures
  print("Press CTRL-C to stop")
  while True:
    val = adxl.get_axes()
    print("X,Y,Z: " + str(val))

    #print("x " + str(val['x']))

    x = val['x']
    y = val['y']
    z = val['z']

    # fX = adxl.low_pass_filter( float(x) )
    # fY = adxl.low_pass_filter( float(y) )
    # fZ = adxl.low_pass_filter( float(z) )

    # print("Filtered: X, Y, Z: " + str(fX) + "\t" + str(fY) + "\t" + str(fZ))

    p = adxl.pitch(x, y, z)
    r = adxl.roll(y, z)
    print("Pitch: " + str(p) + "\t" + "Roll: " + str(r))
    time.sleep(1)

main()
