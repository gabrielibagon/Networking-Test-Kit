# Networking Test Kit

This repository contains a collection of scripts for testing networking functionality for OSC, UDP, and LSL. This is intended for use with OpenBCI networking functionality, but could work for other tasks as well.

# Table of contents
1. [Installation](#Installation)
2. [Usage](#Use)
3. [OSC](#OSC)
  + [Send](#OSC-Sending)
  + [Receive](#OSC-Receiving)
4. [UDP](#UDP)
  + [Send](#UDP-Sending)
  2. [Receive](#UDP-Receiving)

 <a name="Usage"/>
## Installation
The scripts should work for Python 2 and Python 3. Install a different OSC package depending on your version of python.

Python 2:
```
pip install pyosc
```
Python 3:
```
pip install python-osc
```

 <a name="Usage"/>
## Usage

This kit is provided to help you localize and diagnose any issues while using the OpenBCI networking functionality. It is helpful to run scripts that allow you to send and receive data in order to determine if your issue is with the program sending data, the program receiving data, or the network in-between.

If you are using the OpenBCI GUI, the first step might be to check if the GUI is correctly sending data. To do this, check the settings you entered into the Networking Widget, and run the appropriate **receive** networking script with those arguments. If you can correctly receive data, the issue is not with the GUI, but possibly with the 3rd party program or network.

Similarly, the **send** scripts can be used to determine if you can receive data in this 3rd party program. If you are sending data from this script and cannot receive it in a 3rd party program, check to see if your program is correctly configured to accept incoming connections. If you are sending data with the script and can receive it with the 3rd party program, but not with data sent from the OpenBCI GUI, check to see if your setup in the GUI is correct.

The "send" and "receive" scripts can also be used together to test your network, or as a sanity check for the settings your a using.

 <a name="OSC"/>
## OSC
 <a name="OSC-Receiving"/>
### Receiving
Run the script **osc_receive.py** to test listening to OSC messages. Use this to ensure that your program (such as the OpenBCI GUI) is sending messages correctly to the right location.

**Optional Arguments**:
```
--ip      - specify an IP address           [Default = 127.0.0.1]
--port    - specify the port number         [Default = 12345]
--address - specify an OSC message address  [Default = \openbci]
--option  - specify a debugger option       [Default = print]

```

**Debugger Options**

There are two debugger options: **print** or **record**. **Print** outputs the messages receives to the console, while **record** saves a text file to this directory with the messages the debugger has received.


**Examples:**

Listen to and print messages from IP 127.0.0.1, port 12345, address "\openbci".
```
python osc_receive.py
```

Listen to and record messages from IP 127.0.0.1, port 12345, address "\openbci"
```
python osc_receive.py --option=record
```

Listen to and print messages from IP 137.110.96.253, port 8888, address "\accel"
```
python osc_receive.py --ip=137.110.96.253 --port=8888 --address=\accel
```
<a name="OSC-Sending"/>
### Sending
Run the script **osc_send.py** to test sending to OSC messages. Use this to ensure that your program is configured to receive messages correctly.

**Optional Arguments**:
```
--ip      - specify an IP address           [Default = 127.0.0.1]
--port    - specify the port number         [Default = 12345]
--address - specify an OSC message address  [Default = \openbci]
```
**Examples:**

Send messages to IP 127.0.0.1, port 12345, address "\openbci".
```
python osc_send.py
```

Send messages to IP 137.110.96.253, port 8888, address "\accel"
```
python osc_send.py --ip=137.110.96.253 --port=8888 --address=\accel
```
<a name="UDP"/>
## UDP
<a name="UDP-Receiving"/>
### Receiving
Run the script **udp_receive.py** to test listening to UDP messages. Use this to ensure that your program (such as the OpenBCI GUI) is sending messages correctly to the right location.

**Optional Arguments**:
```
--ip      - specify an IP address           [Default = 127.0.0.1]
--port    - specify the port number         [Default = 12345]
--option  - specify a debugger option       [Default = print]
```

**Debugger Options**

There are two debugger options: **print** or **record**. **Print** outputs the messages receives to the console, while **record** saves a text file to this directory with the messages the debugger has received.


**Examples:**

Listen to and print messages from IP 127.0.0.1, port 12345 (defaults).
```
python udp_receive.py
```

Listen to and record messages from IP 127.0.0.1, port 12345.
```
python udp_receive.py --option=record
```

Listen to and print messages from IP 137.110.96.253, port 8888.
```
python udp_receive.py --ip=137.110.96.253 --port=8888
```

<a name="UDP-Sending"/>
### Sending
Run the script **udp_send.py** to test sending to UDP messages. Use this to ensure that your program is configured to receive messages correctly.

**Optional Arguments**:
```
--ip      - specify an IP address           [Default = 127.0.0.1]
--port    - specify the port number         [Default = 12345]
```
**Examples:**

Send messages to IP 127.0.0.1, port 12345 (defaults).
```
python udp_send.py
```

Send messages to IP 137.110.96.253, port 8888.
```
python udp_send.py --ip=137.110.96.253 --port=8888 --address=\accel
```
