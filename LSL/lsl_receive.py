from pylsl import StreamInlet, resolve_stream
import argparse
import time
import atexit
import os
import signal
import sys

def print_message(data, timestamp):
    print("(%s) RECEIVED MESSAGE: " % timestamp,data)

# Clean exit from print mode
def exit_print(signal, frame):
    print("Closing listener")
    sys.exit(0)

# Record received message in text file
def record_to_file(data,timestamp):
    textfile.write(str(timestamp) + ",")
    textfile.write(data)
    textfile.write("\n")

# Save recording, clean exit from record mode
def close_file(*args):
    print("\nFILE SAVED")
    textfile.close()
    sys.exit(0)

if __name__ == "__main__":
    # Collect command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--type",
        type=str, default='EEG', help="The type of stream")
    parser.add_argument("--name",
      default = None, help="The name of the stream")
    parser.add_argument("--option",default="print",help="Debugger option")

    args = parser.parse_args()
    if args.option=="print":
        signal.signal(signal.SIGINT, exit_print)
    elif args.option=="record":
        i = 0
        while os.path.exists("lsl_test%s.txt" % i):
          i += 1
        filename = "lsl_test%i.txt" % i
        textfile = open(filename, "w")
        textfile.write("timestamp,data\n")
        textfile.write("-------------------------\n")
        print("Recording to %s" % filename)
        signal.signal(signal.SIGINT, close_file)

    # Display stream attributes
    print('--------------------')
    print("-- LSL LISTENER -- ")
    print('--------------------')
    print("Name:", args.name)
    print("Type:", args.type)
    print('--------------------')
    print("%s option selected" % args.option)

    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    print("Listening....")

    while True:
        # get a new sample
        chunk, timestamp = inlet.pull_chunk()
        if timestamp:
            if args.option=="print":
                print_message(chunk[0],timestamp[0])
            elif args.option=="record":
                record_to_file(chunk[0],timestamp[0])
