import numpy as np
from timeflux.core.node import Node

class BandExtraction(Node):

    def __init__(self, bands:str):
        ...
        # self._reref_electrode = electrode

    """Rereference the incoming EEG signal using the specified electrode

    Attributes:
        i (Port): EEG signal, expects DataFrame.
        o (Port): Rereferenced EEG signal, provides DataFrame
    """

    def update(self):
        if self.i.ready():
            self.o.meta = self.i.meta
            self.o.data = self.i.data
            # self.o.data = self.o.data.subtract(self.o.data[self._reref_electrode], axis=0)
            # self.o.data.drop(self._reref_electrode, axis=1, inplace=True)
            # print(self.o.data)


class Relax(Node):

    def __init__(self):
        ...
        # self._reref_electrode = electrode

    """Rereference the incoming EEG signal using the specified electrode

    Attributes:
        i (Port): EEG signal, expects DataFrame.
        o (Port): Rereferenced EEG signal, provides DataFrame
    """

    def update(self):
        if self.i.ready():
            self.o.meta = self.i.meta
            self.o.data = self.i.data
            # self.o.data = self.o.data.subtract(self.o.data[self._reref_electrode], axis=0)
            # self.o.data.drop(self._reref_electrode, axis=1, inplace=True)
            # print(self.o.data)