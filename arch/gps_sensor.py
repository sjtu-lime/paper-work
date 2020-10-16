#!/usr/bin/env python3

from sensor import SerialPortSensor
from sensor import SensorMessage


class GPSMessage(SensorMessage):
    longitude: float
    latitude: float


class GPSSeiralPortSensor(SerialPortSensor):

    def decode(bytes):
        return GPSMessage()
