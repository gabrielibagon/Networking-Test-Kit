from pylsl import StreamInlet, resolve_stream
import sys

def print_lsl():
  # first resolve an EEG stream on the lab network
  print("looking for an EEG stream...")
  streams = resolve_stream('type', 'EEG')

  # create a new inlet to read from the stream
  inlet = StreamInlet(streams[0])

  while True:
      # get a new sample (you can also omit the timestamp part if you're not
      # interested in it)
      sample, timestamp = inlet.pull_sample()
      print(timestamp, sample)


if __name__ == "__main__":
  if len(sys.argv)==1:
    print_lsl()