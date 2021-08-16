#!/usr/bin/env python3


class MachineData():   
    """
    Class to represent a a machine data object.
    This object reflects the information determined for,
    and received from a registered machine.
    """

    def __init__(self, uid):
        """
        Initialisation method.
        Parameters:
            uid : UID of the new machine data object.
        """

        self.uid = uid
