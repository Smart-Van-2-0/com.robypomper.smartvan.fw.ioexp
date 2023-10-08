#!/usr/bin/env python

# Based on http://stackoverflow.com/questions/22390064/use-dbus-to-just-send-a-message-in-python

# Python script to call the methods of the DBUS Test Server

from pydbus import SessionBus

bus = SessionBus()
the_object = bus.get("com.ioexp", "/io_expansion_board")

# call the methods and print the results
reply1 = the_object.set_out_0("True")
print(reply1)
reply2 = the_object.set_out_1("True")
print(reply2)

