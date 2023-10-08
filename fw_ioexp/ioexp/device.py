#!/usr/bin/python3

from typing import Optional
import logging

from fw_ioexp.ioexp.mappings import *
from fw_ioexp.device import DeviceAbs
from fw_ioexp.ioexp.chip.AW9523B import AW9523B


logger = logging.getLogger()


class Device(DeviceAbs):
    """
    Device class for Sense Hat devices communicating via Serial port
    """

    PORT_OUT = 0
    MODE_OUT = 0
    PORT_IN = 1
    MODE_IN = 1
    PIN_0 = 0b00000001
    PIN_1 = 0b00000010
    PIN_2 = 0b00000100
    PIN_3 = 0b00001000
    PIN_4 = 0b00010000
    PIN_5 = 0b00100000
    PIN_6 = 0b01000000
    PIN_7 = 0b10000000

    def __init__(self, auto_refresh=True):
        self._data = {}

        self._is_connected = False
        self._is_reading = False
        self._must_terminate = False

        self.cached_version = None  # version can be anything else
        self.cached_type = None
        self.cached_type_code = None

        self._io_exp: Optional[AW9523B] = None
        self.init_chips()

        if auto_refresh:
            self.refresh()

    def init_chips(self):
        try:
            self._io_exp = AW9523B(debug=0)
            self._io_exp.setPortMode(self.PORT_OUT, self.MODE_OUT)
            self._io_exp.setPortMode(self.PORT_IN, self.MODE_IN)

            #self._io_exp.setPortCtrl(PORT, 0xFF)  # set all gpio Push-Pull
            #self._io_exp.writePort(PORT, 0x0)  # set all 0ff

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
        In the Sense Hat case is the hardcoded device's model.
        """

        if self.cached_version is None:
            self.cached_version = self._data['hardcoded_model']

        return self.cached_version

    @property
    def device_type(self) -> str:
        """ Returns the device type """
        if self.cached_type is None:
            if self.device_pid is not None:
                self.cached_type = PID[self.device_pid]['type']

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

        # relays state
        out_port = self._io_exp.readPort(self.PORT_OUT)
        self._data['io_out_0'] = 1 if out_port & self.PIN_0 > 0 else 0
        self._data['io_out_1'] = 1 if out_port & self.PIN_1 > 0 else 0
        self._data['io_out_2'] = 1 if out_port & self.PIN_2 > 0 else 0
        self._data['io_out_3'] = 1 if out_port & self.PIN_3 > 0 else 0
        self._data['io_out_4'] = 1 if out_port & self.PIN_4 > 0 else 0
        self._data['io_out_5'] = 1 if out_port & self.PIN_5 > 0 else 0
        self._data['io_out_6'] = 1 if out_port & self.PIN_6 > 0 else 0
        self._data['io_out_7'] = 1 if out_port & self.PIN_7 > 0 else 0

        # buttons state
        in_port = self._io_exp.readPort(self.PORT_IN)
        self._data['io_in_0'] = 1 if in_port & self.PIN_0 > 0 else 0
        self._data['io_in_1'] = 1 if in_port & self.PIN_1 > 0 else 0
        self._data['io_in_2'] = 1 if in_port & self.PIN_2 > 0 else 0
        self._data['io_in_3'] = 1 if in_port & self.PIN_3 > 0 else 0
        self._data['io_in_4'] = 1 if in_port & self.PIN_4 > 0 else 0
        self._data['io_in_5'] = 1 if in_port & self.PIN_5 > 0 else 0
        self._data['io_in_6'] = 1 if in_port & self.PIN_6 > 0 else 0
        self._data['io_in_7'] = 1 if in_port & self.PIN_7 > 0 else 0

    def set_out(self, value: bool, pin):
        port_val = self._io_exp.readPort(self.PORT_OUT)
        if value:
            port_val |= pin     # switch on
        else:
            port_val &= ~pin     # switch off
        self._io_exp.writePort(self.PORT_OUT, port_val)

    def set_out_0(self, value: bool):
        logger.info("EXECUTED out_0 with {} val".format(value))
        self.set_out(value, self.PIN_0)

    def set_out_1(self, value: bool):
        logger.info("EXECUTED out_1 with {} val".format(value))
        self.set_out(value, self.PIN_1)

    def set_out_2(self, value: bool):
        logger.info("EXECUTED out_2 with {} val".format(value))
        self.set_out(value, self.PIN_2)

    def set_out_3(self, value: bool):
        logger.info("EXECUTED out_3 with {} val".format(value))
        self.set_out(value, self.PIN_3)

    def set_out_4(self, value: bool):
        logger.info("EXECUTED out_4 with {} val".format(value))
        self.set_out(value, self.PIN_4)

    def set_out_5(self, value: bool):
        logger.info("EXECUTED out_5 with {} val".format(value))
        self.set_out(value, self.PIN_5)

    def set_out_6(self, value: bool):
        logger.info("EXECUTED out_6 with {} val".format(value))
        self.set_out(value, self.PIN_6)

    def set_out_7(self, value: bool):
        logger.info("EXECUTED out_7 with {} val".format(value))
        self.set_out(value, self.PIN_7)


if __name__ == '__main__':
    v = Device()
    print("{}# [{}CONNECTED]: {}".format(v.device_type,
                                         "" if v.is_connected else "NOT ",
                                         v.latest_data["V"]))
