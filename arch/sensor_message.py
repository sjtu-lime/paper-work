#!/usr/bin/env python3

class SensorMessage:
    field_a: int
    field_b: int

    def decode(self, msg: SensorMessage) -> str:
        pass

    def encode(self, json: str) -> SensorMessage:
        pass

    def validate(self):
        pass
