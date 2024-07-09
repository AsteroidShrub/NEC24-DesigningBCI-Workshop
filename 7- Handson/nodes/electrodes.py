import numpy as np
from timeflux.core.node import Node

class ElectrodeDeletion(Node):

    def __init__(self, electrodes:str):
        self._reref_electrode = electrodes

    """Rereference the incoming EEG signal using the specified electrode

    Attributes:
        i (Port): EEG signal, expects DataFrame.
        o (Port): Rereferenced EEG signal, provides DataFrame
    """
    def update(self):
        if self.i.ready():
            self.o.meta = self.i.meta
            self.o.data = self.i.data
