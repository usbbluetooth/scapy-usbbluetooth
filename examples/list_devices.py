#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-only
# Copyright 2025, Antonio Vázquez Blanco <antoniovazquezblanco@gmail.com>
#
# This example just uses usbbluetooth to list the available Bluetooth USB
# devices attached to a machine.
# Please, install the usbbluetooth package before running this example.
#

import usbbluetooth


def main():
    # Get a list of all the available devices
    devices = usbbluetooth.list_devices()
    for dev in devices:
        print(dev)


if __name__ == "__main__":
    main()
