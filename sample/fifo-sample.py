#!/usr/bin/env python

import time
from adxl345.i2c import ADXL345

def main():
  # Standard address 0x1D with 'alternate=False' or alternate address 0x53 with 'alternate=True'. Use 'sudo i2cdetect -y 1'.
  adxl = ADXL345(alternate=True)

  # Set data rate at about 2 hz
  rate_hz = adxl.set_data_rate(2)

  # Set range to 16g
  adxl.set_range(16, True)
  adxl.power_on()

  # Enable FIFO
  adxl.enable_fifo()
  print("FIFO is filling in")
  time.sleep(5)
  print("FIFO: " + str(adxl.get_fifo()))
  adxl.disable_fifo()

  # Go back to sleep mode
  adxl.power_off()

main()
