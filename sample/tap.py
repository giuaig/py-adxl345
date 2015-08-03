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
  InterruptSource = 0x30
  TapThreshold = 0x1D
  TapDuration = 0x21
  TapLatency = 0x22
  TapWindow = 0x23
  TapAxes = 0x2A # Axis control for single tap/double tap
  SingleTap = 0x40
  DoubleTap = 0x20
  TA_TapZAxis = 0x01

  ActivityThreshold = 0x24
  InactivityThreshold = 0x25
  InactivityTime = 0x26

  adxl.set_register(TapThreshold, 48)
  adxl.set_register(TapDuration, 16)
  adxl.set_register(TapLatency, 120)
  adxl.set_register(TapWindow, 80)
  adxl.set_register(TapAxes, TA_TapZAxis)

  adxl.set_register(ActivityThreshold, 50)
  adxl.set_register(InactivityThreshold, 80)
  adxl.set_register(InactivityTime, 50)

  adxl.set_register(InterruptEnable, SingleTap)
  adxl.set_register(InterruptEnable, DoubleTap)

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

    if doubletap:
      print("Double TAP!")
    elif singletap:
      print("Single TAP!")


main()
