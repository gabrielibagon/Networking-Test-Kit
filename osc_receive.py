"""Small example OSC server
This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def print_message(args,msg):
  try:
      print("RECEIVED MESSAGE: ", args, msg)
    # print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="localhost", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=12345, help="The port to listen on")
  parser.add_argument("--address",default="/openbci", help="address to listen to")
  parser.add_argument("--option",default="print",help="Debugger option")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  if args.option=="print":
      dispatcher.map("/openbci", print)
  elif args.option=="record":
      dispatcher.map("/openbci", record_to_file)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)


  print('--------------------')
  print("-- OSC LISTENER -- ")
  print('--------------------')
  print("IP:", server.server_address[0])
  print("PORT:", server.server_address[1])
  print("ADDRESS:", args.address)
  print('--------------------')

  print("Waiting for messages...")
  server.serve_forever()
