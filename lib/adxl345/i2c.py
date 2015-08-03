"""
PYTHON driver for the ADXL-345 (3 axes accelerometer from Analog Device)
This driver use the I2C protocol to communicate (see README)
"""

try:
  import smbus
except ImportError:
  exit("Error: Library 'python-smbus' is missing. Install it with sudo apt-get install python-smbus")
import adxl345.base

class ADXL345(adxl345.base.ADXL345_Base):

  # select the correct i2c bus for this revision of Raspberry Pi, from pimoroni
  REVISION = ([l[12:-1] for l in open('/proc/cpuinfo', 'r').readlines() if l[:8] == "Revision"] + ['0000'])[0]

  STD_ADDRESS = 0x1D
  ALT_ADDRESS = 0x53

  def __init__(self, alternate=False):
    self.bus = smbus.SMBus(1 if int(ADXL345.REVISION, 16) >= 4 else 0)
    if alternate:
      self.i2caddress = ADXL345.ALT_ADDRESS
    else:
      self.i2caddress = ADXL345.STD_ADDRESS

  def get_register(self, address):
    bytes = self.bus.read_i2c_block_data(self.i2caddress, address, 1)
    return bytes[0]

  def get_registers(self, address, count):
    bytes = self.bus.read_i2c_block_data(self.i2caddress, address, count)
    return bytes;

  def set_register(self, address, value):
    self.bus.write_byte_data(self.i2caddress, address, value)

  def getOptions(self, address):
    #options_bin = self.bus.read_i2c_block_data(self.i2caddress, address, 8)
    options_bin = self.bus.read_byte_data(self.i2caddress, address)
    #print(options_bin)
    options = [False, False, False, False, False, False, False, False]
    for i in range(8):
      if options_bin & (0x01 << i):
        options[7 - i] = True

    print(options)
    return options

