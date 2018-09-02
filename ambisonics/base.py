__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

import numpy
import math

class Base:
    def __init__(self, format):
        self.format = format
        self.azimuth = 0.0
        self.coeffs = numpy.zeros(self.format.getChannelCount())
        self.Refresh()

    def SetAzimuth(self, azimuth):
        self.azimuth = azimuth
        self.Refresh()

    def Refresh(self):
        self.coeffs[0] = 1.0 / math.sqrt(2.0)
        for i in range(self.format.order):
            self.coeffs[i * 2 + 1] = math.cos(self.azimuth * (i + 1.0))
            self.coeffs[i * 2 + 2] = math.sin(self.azimuth * (i + 1.0))