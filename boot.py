# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network
from machine import Pin, I2C
import time
from ds3231 import DS3231

def logging(information):
    logFile = open ("logs/dome.txt", "a")
    logFile.write(str('%02d' % ds.datetime()[1]) + "/" + str('%02d' % ds.datetime()[2]) + "/" + str('%04d' % ds.datetime()[0]) + " " + str('%02d' % ds.datetime()[4]) + ":" + str('%02d' % ds.datetime()[5]) + ":" + str('%02d' % ds.datetime()[6]) + " | " + information + "\n")
    logFile.close()
    return

i2c = I2C(1, sda=Pin(13), scl=Pin(16))
ds = DS3231(i2c)

logging("Powered On")

lan = network.LAN(mdc = Pin(23), mdio = Pin(18), power = Pin(12), phy_type = network.PHY_LAN8720, phy_addr = 0)

if not lan.active():
    lan.active(1)

time.sleep_ms(2000)
print('ifconfig :', lan.ifconfig())
logging("IP Address:" + lan.ifconfig()[0] + " Subnet Mask:" + lan.ifconfig()[1] + " Gateway:" + lan.ifconfig()[2] + " DNS:" + lan.ifconfig()[3])
