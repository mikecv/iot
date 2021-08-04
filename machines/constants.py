#!/usr/bin/env python3

from enum import Enum


class MachineState(Enum):
    """
    Machine states.
    """
    STARTING = 0
    INITIALISING = 1
    REGISTERING = 2
    ACTIVE = 3
    PAUSED = 4
    FAILED = 5
    TERMINATING = 6