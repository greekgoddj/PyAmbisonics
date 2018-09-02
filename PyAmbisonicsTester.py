__author__ = "Aristotel Digenis"
__copyright__ = "Copyright 2018"
__credits__ = ["Aristotel Digenis"]
__license__ = "GPL 3.0"
__version__ = "0.0"

import ambisonics
import numpy

# specify the format of Ambisonics we will work with
ambisonicFormat = ambisonics.format.Format()
# allocate buffer for BFormat signal to be stored
bFormatSignal = numpy.zeros(ambisonicFormat.getChannelCount())

# create an encoder and decoder
source = ambisonics.encoder.Encoder(ambisonicFormat)
decoder = ambisonics.decoder.Decoder(ambisonicFormat, ambisonics.decoder.SpeakerLayout.Quad)

# encode the signal and then decode into speaker feed gains
source.Encode(bFormatSignal)
speakerGains = decoder.Decode(bFormatSignal)








