#!/usr/bin/env python3

from gps_invoker import *
from utils import config
from uuid import gps_uuid


class Algorithm:
    port = config.get(gps_uuid)['port']
