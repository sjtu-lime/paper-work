#!/usr/bin/env python3

from sensor_message import *


class Sensor:

    def __init__(self, port):
        pass

    def recv() -> RequestMessage:
        pass

    def send(port: int, msg: SensorMessage):
        pass


class VirtualSensor(Sensor):
    def __init__(self, port):
        pass

    def from_file():
        pass


class SerialPortSensor(Sensor):

    def __init__(self, port):
        pass

    def connect(usbid):
        pass

    def disconnect(usbid):
        pass

    def recv_sp():
        pass
