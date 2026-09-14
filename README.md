# Scapy UsbBluetooth

[![Build](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/build.yml/badge.svg)](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/build.yml)
[![CodeQL](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/codeql.yml/badge.svg)](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/codeql.yml)
[![PyPI](https://img.shields.io/pypi/v/scapy-usbbluetooth)](https://pypi.org/project/scapy-usbbluetooth/)
[![Python versions](https://img.shields.io/pypi/pyversions/scapy-usbbluetooth.svg)](https://pypi.org/project/scapy-usbbluetooth/)
[![Snyk package health](https://img.shields.io/badge/Snyk-package%20health-4C4A73?logo=snyk&logoColor=white)](https://snyk.io/advisor/python/scapy-usbbluetooth)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/usbbluetooth/scapy-usbbluetooth/badge)](https://scorecard.dev/viewer/?uri=github.com/usbbluetooth/scapy-usbbluetooth)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.md)

This package contains code to allow Scapy sockets to communicate with Bluetooth controllers using [UsbBluetooth for Python](https://github.com/usbbluetooth/usbbluetooth-python).

For general documentation about the project, please visit [usbbluetooth.github.io](https://usbbluetooth.github.io/).

For a barebones Python version of this library, check out [UsbBluetooth for Python](https://github.com/usbbluetooth/usbbluetooth-python).

For other programming languages you may visit [UsbBluetooth for C](ttps://github.com/usbbluetooth/usbbluetooth) or [UsbBluetooth for C#](https://github.com/usbbluetooth/usbbluetooth-csharp).

## Installation

Just use pip :)

```
pip install scapy-usbbluetooth
```

## Usage

See the [examples](examples/) folder for sample code.

A short illustrative sample usage can be as follows:

```python
import usbbluetooth
from scapy_usbbluetooth import UsbBluetoothSocket
from scapy.layers.bluetooth import HCI_Hdr, HCI_Command_Hdr, HCI_Cmd_Reset


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

## Plaform quirks

This package has some requirements to work because of different platform particularities. To make sure the package works, please, see <https://usbbluetooth.github.io/quirks/>.
