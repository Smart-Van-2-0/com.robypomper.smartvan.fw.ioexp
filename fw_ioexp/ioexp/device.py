#!/usr/bin/python3

from typing import Optional
import logging

from fw_ioexp.ioexp.mappings import *
from fw_ioexp.device import DeviceAbs
from board import I2C
from digitalio import Direction
from adafruit_aw9523 import AW9523
from adafruit_aw9523 import _AW9523_DEFAULT_ADDR as AW9523_DEFAULT_ADDR


logger = logging.getLogger()


class Device(DeviceAbs):
    """
    Device class for IO Expansion devices communicating via Serial port
    """

    OUTPUT_PINS_COUNT = 8
    INPUT_PINS_COUNT = 8

    def __init__(self, auto_refresh=True):
        self._data = {}

        self._is_connected = False
        self._is_reading = False
        self._must_terminate = False

        self.cached_version = None  # version can be anything else
        self.cached_type = None
        self.cached_type_code = None

        self._i2c: Optional[I2C] = None
        self._io_exp: Optional[AW9523] = None
        # define empty array for pins
        self._output_pins = []
        self._output_pins_to_set = []
        self._input_pins = []
        self.init_chips()

        if auto_refresh:
            self.refresh()

    def init_chips(self):
        try:
            self._i2c = I2C()
            self._io_exp = AW9523(self._i2c, AW9523_DEFAULT_ADDR)

            for i in range(self.OUTPUT_PINS_COUNT):
                print("Setting pin {} to OUTPUT".format(i))
                self._output_pins.append(self._io_exp.get_pin(i))
                self._output_pins[i].direction = Direction.OUTPUT
                self._output_pins_to_set.append(None)

            for i in range(self.INPUT_PINS_COUNT):
                print("Setting pin {} to INPUT".format(i))
                self._input_pins.append(self._io_exp.get_pin(i + self.OUTPUT_PINS_COUNT))
                self._input_pins[i].direction = Direction.INPUT

            self._is_connected = True

        except Exception as err:
            self._is_connected = False
            logger.warning("Error on Chips initialization '{}'. Print stacktrace:".format(err))
            import traceback
            traceback.print_exc()

    def refresh(self, reset_data=False):
        """
        Refresh latest data querying them to the device, if `reset_data` is true,
        then default-Zero values are set.
        """

        if not self._is_connected:
            self.init_chips()
            if not self._is_connected:
                return False

        if self._is_reading:
            while self._is_reading or self._must_terminate:
                pass
            if self._must_terminate:
                return False
            return self._is_connected

        self._is_reading = True
        if reset_data:
            self._data = {}
        self._read_data()

        # for k in self._data.keys():
        #     print("'{}': '{}'".format(k, self._data[k]))

        self._is_reading = False
        return self._is_connected

    @property
    def is_connected(self) -> bool:
        """ Returns True if at last refresh attempt the serial device was available. """
        return self._is_connected

    @property
    def is_reading(self) -> bool:
        """ Returns the local device (eg: '/dev/ttyUSB0') used to connect to the serial device """
        return self._is_reading

    def terminate(self):
        """
        Send the terminate signal to all device process and loops.
        """
        self._must_terminate = True

    @property
    def device_pid(self) -> "str | None":
        """
        Returns the device PID, it can be used as index for the PID dict.
        In the IO Expansion case is the hardcoded device's model.
        """

        if self.cached_version is None:
            self.cached_version = self._data['hardcoded_model']

        return self.cached_version

    @property
    def device_type(self) -> str:
        """ Returns the device type """
        if self.cached_type is None:
            if self.device_pid is not None:
                try:
                    self.cached_type = PID[self.device_pid]['type']
                except KeyError as err:
                    raise SystemError("Unknown PID '{}' read from device".format(self.device_pid)) from err

        return self.cached_type if self.cached_type is not None else DEV_TYPE_UNKNOWN

    @property
    def device_type_code(self) -> str:
        """ Returns the device type as a code string"""

        if self.cached_type_code is None and self.device_type is not None:
            self.cached_type_code = dev_type_to_code(self.device_type)

        return self.cached_type_code

    @property
    def latest_data(self) -> dict:
        return self._data

    def _read_data(self):
        """ Read the latest values from sensor's chips. """

        self._data['hardcoded_model'] = "IOExpansionBoard"

        for i in range(self.OUTPUT_PINS_COUNT):
            if self._output_pins_to_set[i] is not None:
                self._output_pins[i].value = self._output_pins_to_set[i]
                self._output_pins_to_set[i] = None
            self._data['io_out_' + str(i)] = self._output_pins[i].value

        for i in range(self.INPUT_PINS_COUNT):
            self._data['io_in_' + str(i)] = self._input_pins[i].value

    def set_out(self, value: bool, pin: int):
        self._output_pins_to_set[pin] = value

    def set_out_0(self, value: bool):
        logger.info("EXECUTED out_0 with {} val".format(value))
        self.set_out(value, 0)

    def set_out_1(self, value: bool):
        logger.info("EXECUTED out_1 with {} val".format(value))
        self.set_out(value, 1)

    def set_out_2(self, value: bool):
        logger.info("EXECUTED out_2 with {} val".format(value))
        self.set_out(value, 2)

    def set_out_3(self, value: bool):
        logger.info("EXECUTED out_3 with {} val".format(value))
        self.set_out(value, 3)

    def set_out_4(self, value: bool):
        logger.info("EXECUTED out_4 with {} val".format(value))
        self.set_out(value, 4)

    def set_out_5(self, value: bool):
        logger.info("EXECUTED out_5 with {} val".format(value))
        self.set_out(value, 5)

    def set_out_6(self, value: bool):
        logger.info("EXECUTED out_6 with {} val".format(value))
        self.set_out(value, 6)

    def set_out_7(self, value: bool):
        logger.info("EXECUTED out_7 with {} val".format(value))
        self.set_out(value, 7)


if __name__ == '__main__':
    v = Device()
    print("{}# [{}CONNECTED]: {}".format(v.device_type,
                                         "" if v.is_connected else "NOT ",
                                         v.latest_data["V"]))
