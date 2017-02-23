from pylsl import StreamInlet, resolve_stream
import sys
import matplotlib.pyplot as plt
import numpy as np

def print_lsl():
  # first resolve an EEG stream on the lab network
  print("looking for an Marker stream...")
  streams = resolve_stream('type', 'Markers')

  # create a new inlet to read from the stream
  inlet = StreamInlet(streams[0])

  timestamps=[]

  while True:
      # get a new sample (you can also omit the timestamp part if you're not
      # interested in it)
      sample, timestamp = inlet.pull_sample()
      print(sample)
    #   timestamps.append(timestamp)


  dif = np.diff(timestamps)
  plt.plot(dif)
  plt.show()



if __name__ == "__main__":
  if len(sys.argv)==1:
    print_lsl()
