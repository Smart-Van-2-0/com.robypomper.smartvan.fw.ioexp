#!/usr/bin/python3

from fw_ioexp.base.commons import *
from fw_ioexp.ioexp._definitions import *
from fw_ioexp.ioexp._dbus_descs import *
from fw_ioexp.ioexp._parsers import *

# Given an PID, this object returns all his info and meta-data
PID = {
    "IOExpansionBoard": {"model": "IO Exp", "type": DEV_Type_IOExpBoard,
                         "dbus_iface": DEV_IFACE_IOExp, "dbus_desc": DEV_DBUS_DESC_IOExp},
}

PROPS_CODES = {
    "hardcoded_model": {"name": "model", "desc": "Model (hardcoded)",
                        "parser": props_parser_str},

    "io_in_0": {"name": "in_0", "desc": "Input PIN 0",
                "parser": props_parser_io},
    "io_in_1": {"name": "in_1", "desc": "Input PIN 1",
                "parser": props_parser_io},
    "io_in_2": {"name": "in_2", "desc": "Input PIN 2",
                "parser": props_parser_io},
    "io_in_3": {"name": "in_3", "desc": "Input PIN 3",
                "parser": props_parser_io},
    "io_in_4": {"name": "in_4", "desc": "Input PIN 4",
                "parser": props_parser_io},
    "io_in_5": {"name": "in_5", "desc": "Input PIN 5",
                "parser": props_parser_io},
    "io_in_6": {"name": "in_6", "desc": "Input PIN 6",
                "parser": props_parser_io},
    "io_in_7": {"name": "in_7", "desc": "Input PIN 7",
                "parser": props_parser_io},

    "io_out_0": {"name": "out_0", "desc": "Output PIN 0",
                 "parser": props_parser_io},
    "io_out_1": {"name": "out_1", "desc": "Output PIN 1",
                 "parser": props_parser_io},
    "io_out_2": {"name": "out_2", "desc": "Output PIN 2",
                 "parser": props_parser_io},
    "io_out_3": {"name": "out_3", "desc": "Output PIN 3",
                 "parser": props_parser_io},
    "io_out_4": {"name": "out_4", "desc": "Output PIN 4",
                 "parser": props_parser_io},
    "io_out_5": {"name": "out_5", "desc": "Output PIN 5",
                 "parser": props_parser_io},
    "io_out_6": {"name": "out_6", "desc": "Output PIN 6",
                 "parser": props_parser_io},
    "io_out_7": {"name": "out_7", "desc": "Output PIN 7",
                 "parser": props_parser_io}

}

CALC_PROPS_CODES = {
    # N/A
}
