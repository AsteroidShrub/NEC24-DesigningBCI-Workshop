import numpy as np
from timeflux.core.node import Node

class BandExtraction(Node):

    def __init__(self, bands:str):
        ...

    def update(self):
        if self.i.ready():
            # self.o.meta = self.i.meta
            # self.o.data = self.i.data
            ...


class Relax(Node):

    def __init__(self):
        ...

    def update(self):
        if self.i.ready():
            # self.o.meta = self.i.meta
            # self.o.data = self.i.data
            ...
            