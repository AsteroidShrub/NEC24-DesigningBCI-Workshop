import numpy as np
from timeflux.core.node import Node

class DebugPassThrough(Node):

    def __init__(self, once:bool, message:str):
        self._once = True
        self._passed = False
        self._message = message

    
    def update(self):
        if self.i.ready():
            self.o.meta = self.i.meta
            self.o.data = self.i.data
            if not (self._once and self._passed):
                print("PASSTHROUGH: ", self._message)
                self._passed = True