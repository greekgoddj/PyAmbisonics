__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

from enum import Enum

class Normalisation(Enum):
    SND = 0
    ND = 1
    maxN = 2

class ChannelOrdering(Enum):
    ACN = 0
    FurseMalham = 1
    SID = 2

class Format:
    def __init__(self, order=1):
        self.order = order
        self.height = False
        self.normalisation = Normalisation.maxN
        self.ordering = ChannelOrdering.FurseMalham

    def getChannelCount(self):
        return self.order * 2 + 1
