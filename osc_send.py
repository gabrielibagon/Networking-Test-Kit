import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=12345,
      help="The port the OSC server is listening on")
  parser.add_argument("--address", default="/openbci",
      help="The address the OSC server is sending to")

  args = parser.parse_args()

  client = udp_client.SimpleUDPClient("127.0.0.1", 12345 )

  print('--------------------')
  print("-- OSC SIMULATION -- ")
  print('--------------------')
  print("IP:", args.ip)
  print("PORT:", args.port)
  print("ADDRESS:", args.address)
  print('--------------------')

  while (1):
    msg = random.random()
    print("SENT MESSAGE: ", msg )
    client.send_message(args.address, msg)
    time.sleep(.25)
