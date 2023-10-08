#!/usr/bin/python3

# List of supported DBus objects' definitions
# Strings used as default value to populate the PID dict

DEV_DBUS_DESC_IOExp = '''<node>
  <interface name='{dbus_iface}'>
  
    <property name="model" type="s" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
  
    <property name="in_0" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_1" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_2" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_3" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_4" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_5" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_6" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="in_7" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
  
    <property name="out_0" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_1" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_2" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_3" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_4" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_5" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_6" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    <property name="out_7" type="b" access="read">
      <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
    </property>
    
    <method name="set_out_0">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_1">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_2">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_3">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_4">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_5">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_6">
      <arg direction="in" name="value" type="b"/>
    </method>
    <method name="set_out_7">
      <arg direction="in" name="value" type="b"/>
    </method>
    
  </interface>
</node>
'''
