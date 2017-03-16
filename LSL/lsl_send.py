"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import time
from random import random as rand
import argparse

from pylsl import StreamInfo, StreamOutlet

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)


if __name__ == "__main__":

    # Collect command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="openbci-eeg",
      help="The name of the LSL stream")
    parser.add_argument("--type", type=str, default='EEG',
      help="The type of the LSL stream")
    args = parser.parse_args()

    info = StreamInfo(args.name, args.type, 8, 1, 'float32', 'openbci12345')

    # next make an outlet
    outlet = StreamOutlet(info)

    while (1):
        # make a new random 8-channel sample; this is converted into a
        # pylsl.vectorf (the data type that is expected by push_sample)
        mysample = [rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()]
        # now send it and wait for a bit
        outlet.push_sample(mysample)
        time.sleep(0.004)
