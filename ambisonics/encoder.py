__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

from . import base
import numpy

class Encoder(base.Base):
    def __init__(self, format):
        base.Base.__init__(self, format)

    def Encode(self, bFormatSignal:numpy.array):
        bFormatSignal[:] =  self.coeffs