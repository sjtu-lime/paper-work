#!/usr/bin/env python3

class RequestMessage:
    from_who: int
    to_whom: int
    sensor_id: int
    mode: 'once' / 'subscribe' / 'unsubscribe'
