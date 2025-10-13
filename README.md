# Scapy UsbBluetooth

[![Build](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/build.yml/badge.svg)](https://github.com/usbbluetooth/scapy-usbbluetooth/actions/workflows/build.yml)
[![PyPI](https://img.shields.io/pypi/v/scapy-usbbluetooth)](https://pypi.org/project/scapy-usbbluetooth/)
[![scapy-usbbluetooth](https://snyk.io/advisor/python/scapy-usbbluetooth/badge.svg)](https://snyk.io/advisor/python/scapy-usbbluetooth)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.md)

This package contains code to allow Scapy sockets to communicate with Bluetooth controllers using [UsbBluetooth](https://github.com/usbbluetooth/usbbluetooth).

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

### Windows

In Windows you may have to install WinUSB driver in your device using Zadig. Otherwise, UsbBluetooth will detect your device but it may not be able to take control of your device.

### Linux

Your Linux user must have permissions to access USB hardware. Here are several options to ensure access:

- **Run as root**: Execute the application with elevated privileges using `sudo`. Note that this may not be ideal for security reasons.

- **Add user to a group**: Add your user to the `plugdev`, `usb` or `uucp` group (depending on your distribution). Remeber to reboot or log out and log back in for the changes to take effect. For example:

  ```
  sudo usermod -a -G plugdev $USER
  ```

- **Create a udev rule**: Create a custom udev rule to automatically set permissions for USB Bluetooth devices. Create a file like `/etc/udev/rules.d/99-usbbluetooth.rules` with content similar to:
  ```
  SUBSYSTEM=="usb", ATTR{idVendor}=="your_vendor_id", ATTR{idProduct}=="your_product_id", MODE="0666"
  ```
  Replace `your_vendor_id` and `your_product_id` with the actual vendor and product IDs of your device (you can find these using `lsusb`). Then reload udev rules with `sudo udevadm control --reload-rules && sudo udevadm trigger`.
