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


  InterruptEnable = 0x2E
  FreeFall = 0x04
  InterruptSource = 0x30
  adxl.set_register(InterruptEnable, FreeFall)

  # Indefinitely print acceleration measures
  print("Press CTRL-C to stop")
  while True:
    val = adxl.get_axes()

    x = val['x']
    y = val['y']
    z = val['z']

    #print("X,Y,Z: " + str(x) + "\t" + str(y) + "\t" + str(z))

    ##values = adxl.get_registers(InterruptSource, 8)
    ##print( "Values: " + str(values) )

    #[dataready, singletap, doubletap, activity, inactivity, freefall, watermark, overrun] = adxl345.getInterruptStatus()
    [dataready, singletap, doubletap, activity, inactivity, freefall, watermark, overrun] = adxl.getOptions(InterruptSource)

    if freefall:
      print("Falling!!!")


main()
