#!/usr/bin/python3
import logging

from fw_ioexp.ioexp.device import Device
from fw_ioexp.ioexp.mappings import *


logger = logging.getLogger()


class DeviceSimulator(Device):

    def __init__(self, auto_refresh=False):
        super().__init__(auto_refresh)
        self._out_pin_state = ['0', '0', '0', '0', '0', '0', '0', '0']
        self._data = {
            'hardcoded_model': "IOExpansionBoard",

            'io_out_0': self._out_pin_state[0],
            'io_out_1': self._out_pin_state[1],
            'io_out_2': self._out_pin_state[2],
            'io_out_3': self._out_pin_state[3],
            'io_out_4': self._out_pin_state[4],
            'io_out_5': self._out_pin_state[5],
            'io_out_6': self._out_pin_state[6],
            'io_out_7': self._out_pin_state[7],

            'io_in_0': '0',
            'io_in_1': '0',
            'io_in_2': '0',
            'io_in_3': '0',
            'io_in_4': '0',
            'io_in_5': '0',
            'io_in_6': '0',
            'io_in_7': '0'
        }

    @property
    def is_connected(self) -> bool:
        """ Returns always True. """
        return self._is_connected

    def init_chips(self):
        self._is_connected = True

    def refresh(self, reset_data=False) -> bool:
        self._data = {
            'hardcoded_model': "IOExpansionBoard",

            'io_out_0': self._out_pin_state[0],
            'io_out_1': self._out_pin_state[1],
            'io_out_2': self._out_pin_state[2],
            'io_out_3': self._out_pin_state[3],
            'io_out_4': self._out_pin_state[4],
            'io_out_5': self._out_pin_state[5],
            'io_out_6': self._out_pin_state[6],
            'io_out_7': self._out_pin_state[7],

            'io_in_0': '1' if random.randint(0, 100) <= 50 else '0',
            'io_in_1': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_2': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_3': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_4': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_5': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_6': '1' if random.randint(0, 100) <= 20 else '0',
            'io_in_7': '1' if random.randint(0, 100) <= 20 else '0',
        }

        return True

    def set_out_0(self, value: bool):
        logger.info("EXECUTED out_0 with {} val".format(value))
        self._out_pin_state[0] = "1" if value else "0"

    def set_out_1(self, value: bool):
        logger.info("EXECUTED out_1 with {} val".format(value))
        self._out_pin_state[1] = "1" if value else "0"

    def set_out_2(self, value: bool):
        logger.info("EXECUTED out_2 with {} val".format(value))
        self._out_pin_state[2] = "1" if value else "0"

    def set_out_3(self, value: bool):
        logger.info("EXECUTED out_3 with {} val".format(value))
        self._out_pin_state[3] = "1" if value else "0"

    def set_out_4(self, value: bool):
        logger.info("EXECUTED out_4 with {} val".format(value))
        self._out_pin_state[4] = "1" if value else "0"

    def set_out_5(self, value: bool):
        logger.info("EXECUTED out_5 with {} val".format(value))
        self._out_pin_state[5] = "1" if value else "0"

    def set_out_6(self, value: bool):
        logger.info("EXECUTED out_6 with {} val".format(value))
        self._out_pin_state[6] = "1" if value else "0"

    def set_out_7(self, value: bool):
        logger.info("EXECUTED out_7 with {} val".format(value))
        self._out_pin_state[7] = "1" if value else "0"


if __name__ == '__main__':
    v = DeviceSimulator()
    print("{}# [{}CONNECTED]: {}".format(v.device_type,
                                         "" if v.is_connected else "NOT ",
                                         v.latest_data["V"]))
