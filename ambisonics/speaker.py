__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

from . import base
import numpy
import math

class Speaker(base.Base):
    def __init__(self, order=1):
        base.Base.__init__(self, order)
        self.Refresh()

    def Refresh(self):
        base.Base.Refresh(self)
        self.coeffs[0] = math.sqrt(2.0)

    def Decode(self, bFormatSignal:numpy.array):
        return self.coeffs.dot(bFormatSignal)