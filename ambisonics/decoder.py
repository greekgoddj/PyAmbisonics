__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

from . import speaker
from enum import Enum
import numpy
import math

class SpeakerLayout(Enum):
    Mono = 0
    Stereo = 1
    Quad = 2

class Decoder:
    def __init__(self, format, layout:SpeakerLayout):
        self.format = format
        self.layout = layout
        self.speakers = []
        self.SetSpeakerLayout(layout)

    def SetSpeakerLayout(self, layout:SpeakerLayout):
        if (layout == SpeakerLayout.Quad):
            self.speakers = [speaker.Speaker(self.format)] * 4
            self.speakers[0].SetAzimuth(math.radians(45.0))
            self.speakers[1].SetAzimuth(math.radians(-45.0))
            self.speakers[2].SetAzimuth(math.radians(135.0))
            self.speakers[3].SetAzimuth(math.radians(-135.0))
        else:
            print("Speaker layout set to unknown") # TODO add proper error handling

        self.layout = layout

    def Decode(self, bFormatSignal:numpy.array):
        speakerSignals = numpy.zeros(len(self.speakers))
        for i in range(len(self.speakers)):
            speakerSignals[i] = self.speakers[i].Decode(bFormatSignal)
        return speakerSignals

