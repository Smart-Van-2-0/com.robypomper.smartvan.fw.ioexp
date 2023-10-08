# FW IO Expansion - Values Mapping

The properties exposed on the DBus vary depending on
the [type of device](supported_devices.md). A description of the
DBus object to be exposed is defined for each type of device. The DBus object
definitions are specified in the
[_dbus_descs.py](/fw_ioexp/ioexp/_dbus_descs.py) file.

During the `main_loop`, this script refresh the device's data and parse any
property found, if the property value is update the script sends the property
update to the DBus. To parse the property it uses the info contained into
the`PROPS_CODE` table. Sometime, it can trigger an exception because the updated
property is not present into the DBus object definitions. In this case add the
property to the DBus object definitions or fix the `PROPS_CODES` table.

## DBus properties

Exposed properties can be of two types: direct or calculated. Direct properties
are exported as they come from the device. Calculated properties are the result
of an elaboration.

### Direct

Direct properties are defined into the `PROPS_CODES` table into
the [mappings.py](/fw_ioexp/ioexp/mappings.py) file.

For each property are defined following fields:

* `KEY`: property name on device side
* `name`: property name on DBus
* `desc`: human-readable description of the property
* `parser`: the method to use to parse the value read from the device

| Prop.'s KEY | Prop.'s Name on DBus | Description  | Parser method        |
|-------------|----------------------|--------------|----------------------|
| `io_in_0`   | `in_0`               | Input PIN 0  | `props_parser_io`    |
| `io_in_1`   | `in_1`               | Input PIN 1  | `props_parser_io`    |
| `io_in_2`   | `in_2`               | Input PIN 2  | `props_parser_io`    |
| `io_in_3`   | `in_3`               | Input PIN 3  | `props_parser_io`    |
| `io_in_4`   | `in_4`               | Input PIN 4  | `props_parser_io`    |
| `io_in_5`   | `in_5`               | Input PIN 5  | `props_parser_io`    |
| `io_in_6`   | `in_6`               | Input PIN 6  | `props_parser_io`    |
| `io_in_7`   | `in_7`               | Input PIN 7  | `props_parser_io`    |
| `io_out_0`  | `out_0`              | Output PIN 0 | `props_parser_io`    |
| `io_out_1`  | `out_1`              | Output PIN 1 | `props_parser_io`    |
| `io_out_2`  | `out_2`              | Output PIN 2 | `props_parser_io`    |
| `io_out_3`  | `out_3`              | Output PIN 3 | `props_parser_io`    |
| `io_out_4`  | `out_4`              | Output PIN 4 | `props_parser_io`    |
| `io_out_5`  | `out_5`              | Output PIN 5 | `props_parser_io`    |
| `io_out_6`  | `out_6`              | Output PIN 6 | `props_parser_io`    |
| `io_out_7`  | `out_7`              | Output PIN 7 | `props_parser_io`    |

Parser methods are defined into [_parsers.py](/fw_ioexp/ioexp/_parsers.py)
file. Depending on which DBus property's they are mapped for, they can return
different value's types.<br/>
Custom types are defined into
the [_definitions.py](/fw_ioexp/ioexp/_definitions.py) file.

### Calculated

Calculated properties are special values that can be elaborated starting from
other properties (also other calculated properties). When a property is updated,
the script checks if there is some calculated property that depends on it. If
any, then the script calculate the dependant property.

For each calculated property are defined following fields:

* `KEY`: calculated property name on DBus
* `name`: calculated property name (not used)
* `desc`: human-readable description of the property
* `depends_on`: the list of properties on which the current property depends
* `calculator`: the method to use to elaborate the property

| Prop.'s Name on DBus | Description | Depends on | Calculator method |
|----------------------|-------------|------------|-------------------|
| --                   | --          | --         | --                |

**No calculated properties are used from this script. **

All methods used to elaborate the properties, receives the properties cache as
param. So they can use that list to get all properties read from the device (
also other calculated properties).

## Properties by DBus Object description

This is the table containing all properties handled by this script. For each
property, the table define if it will be exported by the column's device type.

| Prop.'s Name on DBus          | Type    | AW9523B |
|-------------------------------|---------|---------|
| `in_0`                        | boolean | Yes     |
| `in_1`                        | boolean | Yes     |
| `in_2`                        | boolean | Yes     |
| `in_3`                        | boolean | Yes     |
| `in_4`                        | boolean | Yes     |
| `in_5`                        | boolean | Yes     |
| `in_6`                        | boolean | Yes     |
| `in_7`                        | boolean | Yes     |
| `out_0`                       | boolean | Yes     |
| `out_1`                       | boolean | Yes     |
| `out_2`                       | boolean | Yes     |
| `out_3`                       | boolean | Yes     |
| `out_4`                       | boolean | Yes     |
| `out_5`                       | boolean | Yes     |
| `out_6`                       | boolean | Yes     |
| `out_7`                       | boolean | Yes     |

## DBus methods

This script exposes the following methods on the DBus:

| Method's Name on DBus | Description            | Type | Params    | AW9523B |
|-----------------------|------------------------|------|-----------|---------|
| `set_out_0`           | Set Output PIN 0 state | void | Boolean   | Yes     |
| `set_out_1`           | Set Output PIN 1 state | void | Boolean   | Yes     |
| `set_out_2`           | Set Output PIN 2 state | void | Boolean   | Yes     |
| `set_out_3`           | Set Output PIN 3 state | void | Boolean   | Yes     |
| `set_out_4`           | Set Output PIN 4 state | void | Boolean   | Yes     |
| `set_out_5`           | Set Output PIN 5 state | void | Boolean   | Yes     |
| `set_out_6`           | Set Output PIN 6 state | void | Boolean   | Yes     |
| `set_out_7`           | Set Output PIN 7 state | void | Boolean   | Yes     |
