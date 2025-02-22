# Scapy UsbBluetooth

[![Build](https://github.com/antoniovazquezblanco/scapy-usbbluetooth/actions/workflows/build.yml/badge.svg)](https://github.com/antoniovazquezblanco/scapy-usbbluetooth/actions/workflows/build.yml)
[![scapy-usbbluetooth](https://snyk.io/advisor/python/scapy-usbbluetooth/badge.svg)](https://snyk.io/advisor/python/scapy-usbbluetooth)

This package contains code to allow Scapy sockets to communicate with Bluetooth controllers using [UsbBluetooth](https://github.com/antoniovazquezblanco/usbbluetooth).


## Installation

Just use pip :)

```
pip install scapy-usbbluetooth
```


## Usage

```python
import usbbluetooth
from scapy_usbbluetooth import UsbBluetoothSocket


# Get a list of all the available devices
devices = usbbluetooth.list_devices()
for dev in devices:
    print(dev)

# Open a socket using a device
socket = UsbBluetoothSocket(devices[0])

# Create a reset packet
pkt = HCI_Hdr() / HCI_Command_Hdr() / HCI_Cmd_Reset()

# Send a packet to the controller and await a response
response = socket.sr1(pkt)
response.show()
```
