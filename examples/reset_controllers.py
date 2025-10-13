#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Antonio Vázquez Blanco <antoniovazquezblanco@gmail.com>
#
# This example uses scapy-usbbluetooth to list the available Bluetooth USB
# and attempts to send a reset command to each of them.
# Please, install the scapy-usbbluetooth package before running this example.
#

import usbbluetooth
from scapy_usbbluetooth import UsbBluetoothSocket
from scapy.layers.bluetooth import HCI_Hdr, HCI_Command_Hdr, HCI_Cmd_Reset


def reset_device(dev):
    print(f"Resetting device: {dev}")

    try:
        # Open a socket using a device
        socket = UsbBluetoothSocket(dev)

        # Create a reset packet
        pkt = HCI_Hdr() / HCI_Command_Hdr() / HCI_Cmd_Reset()

        # Send a packet to the controller and await a response
        response = socket.sr1(pkt)
        response.show()
    except Exception as e:
        print(f"Failed to reset device {dev}: {e}")


def main():
    # Get a list of all the available devices
    devices = usbbluetooth.list_controllers()
    for dev in devices:
        reset_device(dev)


if __name__ == "__main__":
    main()
