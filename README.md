# FW IO Expansion

Simple Python module that read/write GPIO status from [IO Expansion](https://www.waveshare.com/aw9523b-io-expansion-board.htm)
board and share them on the local DBus.<br />
This repository is part of the [Smart Van Project](https://smartvan.johnosproject.org/).

**FW Name:** FW IO Exp<br />
**FW Group:** com.robypomper.smartvan.fw.ioexp<br />
**FW Version:** 1.0.0-DEV

[README](README.md) | [CHANGELOG](CHANGELOG.md) | [TODOs](TODOs.md) | [LICENCE](LICENCE.md)

Once ran, this script **reads data from the IO Exp via I2C then notify
the DBus with updated values**. On the other side, when it executes a
DBus method, it sends the new value to the IO Exp. Then the value is
updated back, next time the values are read. The DBus service and his
properties are defined into [_dbus_descs.py](fw_ioexp/ioexp/_dbus_descs.py) file. More info on
on [Supported devices](/docs/supported_devices.md)
and [value mapping](/docs/values_mapping.md).


## Run

This is a Python script, so `python` is required to run it.

```shell
$ python --version
# if not installed, then run
$ sudo apt-get install python3 python3-pip
```

In addition, some other package must be installed in order to configure
python's dependencies like `PyGObject` or `pydbus`. If you are using a
debian/ubuntu based distribution, then you can run:

```shell
$ sudo apt-get install libcairo2-dev libgirepository1.0-dev dbus-x11 
```

Once Python was installed on your machine, you can install the script's
requirements globally or create a dedicated `venv`.

```shell
# Init venv (Optional)
$ python -m venv venev
$ source venv/bin/activate

# Install script's requirements
$ pip install -r requirements.txt
```

Now, you are ready to run the script with the command:

```shell
$ python run.py

or alternative options
$ python run.py --quiet
$ python run.py --debug --simulate
$ python run.py  --dbus-name com.custom.bus --dbus-obj-path /custom/path --dbus-iface com.custom.IFace
```

For script's [remote usage](docs/remote_usage.md) please see the dedicated page.

Defaults DBus params are:
* DBus Name: `com.ioexp`
* DBus Obj Path: DEV_TYPE_* (eg: `/io_expansion_board`)
* DBus Interface: DEV_IFACE_* (eg: `com.ioexp`)

### Script's arguments

The `run.py` script accept following arguments:
 
* `-h`, `--help`: show this help message and exit
* `-v`, `--version`: show version and exit
* `--simulate`: Simulate a version `V3.2P`
* `--dbus-name DBUS_NAME`: DBus name
* `--dbus-obj-path DBUS_OBJ_PATH`: DBus object path (if None, the device type will be used, if empty nothing will be used)
* `--dbus-iface DBUS_IFACE`: DBus interface (if None, the device interface will be used, if empty nothing will be used)
* `--dev`: enable development mode, increase logged messages info
* `--debug`: Set log level to debug
* `--quiet`: Set log level to error


## Develop

The main goal for this script is to link the Device's protocol to the DBus.
So, in addition to the main script, all other files are related to the Device
or to the DBus protocols.

Module's files can be grouped in 2 categories:

**Definitions:**

* [ioexp/mappings.py](fw_ioexp/ioexp/mappings.py):
  definition of `PID`, `PROPS_CODES` and `CALC_PROPS_CODES` tables
* [ioexp/_definitions.py](fw_ioexp/ioexp/_definitions.py):
  definitions of supported devices, DUbus ifaces and custom properties types
* [ioexp/_parsers.py](fw_ioexp/ioexp/_parsers.py):
  custom properties parsers
* [ioexp/_calculated.py](fw_ioexp/ioexp/_calculated.py):
  custom properties calculators and data generator methods for simulator
* [ioexp/_dbus_descs.py](fw_ioexp/ioexp/_dbus_descs.py):
  definition of DBus iface's descriptors

**Operations:**

* [run.py](run.py):
  main firmware script
* [ioexp/device.py](fw_ioexp/ioexp/device.py):
  class that represent the device
* [ioexp/simulator.py](fw_ioexp/ioexp/simulator.py):
  class that represent the simulated device
* [dbus/obj.py](fw_ioexp/dbus/obj.py):
  class that represent aDBus object to publish
* [dbus/daemon.py](fw_ioexp/dbus/daemon.py):
  methods to handle the DBus daemon
* [commons.py](fw_ioexp/commons.py):
  commons properties parsers and simulator methods
* [device.py](fw_ioexp/device.py):
  base class for devices
* [device_serial.py](fw_ioexp/device_serial.py):
  base implementation for serial devices
