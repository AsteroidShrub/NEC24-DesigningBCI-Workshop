import numpy as np
from timeflux.core.node import Node

class ElectrodeDeletion(Node):

    def __init__(self, electrodes:str):
        self._electrodes = electrodes

    def update(self):
        if self.i.ready():
            # self.o.meta = self.i.meta
            # self.o.data = self.i.data
            ...
