#!/usr/bin/python3


def props_parser_io(raw_value: str) -> bool:
    try:
        return bool(int(raw_value))

    except Exception:
        raise ValueError("Can't cast '{}' into {}".format(raw_value, "boolean"))
