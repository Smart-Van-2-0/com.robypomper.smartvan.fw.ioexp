#!/usr/bin/python
# -*- coding:utf-8 -*-


"""
From https://cdn-shop.adafruit.com/product-files/4886/AW9523+English+Datasheet.pdf

Table-4. AW9523B register list
Address W/R Default Value Function Description
00H R Equal to P0 Input_Port0 P0 port input state
01H R Equal to P1 Input_Port1 P1 port input state
02H W/R Refer to table 1 Output_Port0 P0 port output state
03H W/R Refer to table 1 Output_Port1 P1 port output state
04H W/R 00H Config_Port0 P0 port direction configure
05H W/R 00H Config_Port1 P1 port direction configure
06H W/R 00H Int_Port0 P0 port interrupt enable
07H W/R 00H Int_Port1 P1 port interrupt enable
10H R 23H ID ID register (read only)
11H W/R 00H CTL Global control register
12H W/R FFH LED Mode Switch P0 port mode configure
13H W/R FFH LED Mode Switch P1 port mode configure
20H W 00H DIM0 P1_0 LED current control
21H W 00H DIM1 P1_1 LED current control
22H W 00H DIM2 P1_2 LED current control
23H W 00H DIM3 P1_3 LED current control
24H W 00H DIM4 P0_0 LED current control
25H W 00H DIM5 P0_1 LED current control
26H W 00H DIM6 P0_2 LED current control
27H W 00H DIM7 P0_3 LED current control
28H W 00H DIM8 P0_4 LED current control
29H W 00H DIM9 P0_5 LED current control
2AH W 00H DIM10 P0_6 LED current control
2BH W 00H DIM11 P0_7 LED current control
2CH W 00H DIM12 P1_4 LED current control
2DH W 00H DIM13 P1_5 LED current control
2EH W 00H DIM14 P1_6 LED current control
2FH W 00H DIM15 P1_7 LED current control
7FH W 00H SW_RSTN Soft reset
Other - - - Reserved
"""

import sys
import time
import smbus
try:
    import RPi.GPIO as GPIO
    _gpio_loaded = True
except:
    print("WARN: RPi.GPIO module disabled.")
    _gpio_loaded = False

ADDR = 0x58

# int pin
INI_PIN = 23
RST_PIN = 24


class AW9523B:
    MODE_OUT = 0
    MODE_IN = 1

    def __init__(self, address=ADDR, debug=1):
        self.i2c = smbus.SMBus(1)
        self.address = address

        self.debug = debug

        #if _gpio_loaded:
            #GPIO.setmode(GPIO.BCM)
            #GPIO.setwarnings(False)
            #GPIO.setup(INI_PIN, GPIO.IN)

            #GPIO.setup(RST_PIN, GPIO.OUT)
            #GPIO.output(RST_PIN, 0)
            #time.sleep(0.1)
            #GPIO.output(RST_PIN, 1)

        self.ID = self.ReadByte(0x10)  # ID
        if self.ID != 0x23:  # ID = 0X23
            print("not find AW9523B")
            sys.exit()
        else:
            print("find AW9523B, ID = 0x%x" % (self.ID))
        #self.LEDModeSwitch(0, 1)  # set out mode gpio
        #self.setPortCtrl(1, 0)  # set all gpio Push-Pull
        #self.LEDModeSwitch(1, 1)  # set out mode gpio

    def ReadByte(self, addr):
        return self.i2c.read_byte_data(self.address, addr)

    def WriteByte(self, addr, val):
        self.i2c.write_byte_data(self.address, addr, val & 0xFF)

    def setPortMode(self, port, mode):  # port:04H 05H , mode:0-out 1-in
        """
        Set mode for the entire port.

        port: 0 or 1
        mode: 0=out or 1=in

        04H W/R 00H Config_Port0 P0 port direction configure
        05H W/R 00H Config_Port1 P1 port direction configure
        """
        if self.debug == 1:
            print("set port%d mode = %s" % (port, "out" if mode == 0 else "in"))
        self.WriteByte(0x04 if port == 0 else 0x05, 0 if mode == 0 else 0xff)

    def readPort(self, port):  # port:00h 01H
        """
        Read the current values for the entire port.
        
        00H R Equal to P0 Input_Port0 P0 port input state
        01H R Equal to P1 Input_Port1 P1 port input state
        """
        val = self.ReadByte(0x00 if port == 0 else 0x01)
        if (self.debug == 1):
            print("input por{} val = {:#010b}".format(port, val))
        return val

    def writePort(self, port, val):  # port:02H 03H , mode:0-Llev 0xff-Hlev
        """
        Write given values for the entire port.

        02H W/R Refer to table 1 Output_Port0 P0 port output state
        03H W/R Refer to table 1 Output_Port1 P1 port output state
        """
        if self.debug == 1:
            print("output por{} val = {:#010b}".format(port, val))
        self.WriteByte(0x02 if port == 0 else 0x03, val)

    def enablePortInterrupt(self, port, en):  # port:06h 07h, en:0-enable 1-uenable
        """
        Enable/Disable interrupt on the entire port.

        06H W/R 00H Int_Port0 P0 port interrupt enable
        07H W/R 00H Int_Port1 P1 port interrupt enable
        """
        if self.debug == 1:
            print("enable port%d int = 0x%x" % (port, en))
        self.WriteByte(0x06 if port == 0 else 0x07, en)

    def getPortInterrupt(self, port):
        if self.debug == 1:
            print("clear port%d int" % port)
        self.ReadByte(0x06 if port == 0 else 0x07)

    def setPinMode(self, port, pin, mode):
        self.WriteByte(0x04 if port == 0 else 0x05, mode << pin)

    def readPin(self, port, pin):  # port:00h 01H
        return self.ReadByte(0x00 if port == 0 else 0x01) & (1 << pin)

    def writePin(self, port, pin, val):  # port:02H 03H , mode:0-Llev 0-Hlev
        self.WriteByte(0x02 if port == 0 else 0x03, val << pin)

    def enablePinInterrupt(self, port, pin, en):  # port:06h 07h, en:0-enable 1-uenable
        self.WriteByte(0x06 if port == 0 else 0x07, en << pin)

    def setPortCtrl(self, gpomd, isel):
        g = gpomd << 4
        s = isel << 2
        val = g | s
        self.WriteByte(0x11, val)  # AW9523B_REG_GLOB_CTR



    def LEDModeSwitch(self, port, mode):  # PORT 12H 13H, MODE:0(led) 1(gpio)
        self.WriteByte(0x12 if port == 0 else 0x13, 0 if mode == 0 else 0xff)

    def LEDDims(self, lednum, i):  # lednum:0x20->0x2F, i: i/255×IMAX, IMAX= 37Ma
        self.WriteByte(lednum, i)



if __name__ == '__main__':
    print("test:Connect the 0 port to the 1 port")
    gpio = AW9523B()

    # ouput
    gpio.setPortMode(0, 0)
    # gpio.PortOutput(0, 0xf0)
    # gpio.PortMode(1, 0)
    # gpio.PortOutput(1, 0xff)
    # gpio.PortInput(1)

    # input
    gpio.setPortMode(1, 1)
    gpio.enablePortInterrupt(1, 0)
    tm = 1
    # while(1):
    for x in range(0, 8):
        gpio.writePort(0, 1 << x)
        time.sleep(0.1)
        if _gpio_loaded:
            if GPIO.input(INI_PIN) == 0:
                while GPIO.input(INI_PIN) != 0:
                    # gpio.PortIntClear(1)
                    print("sss")
                gpio.readPort(1)
                print("read is change, Trigger interrupted %d" % tm)
        tm = tm + 1
