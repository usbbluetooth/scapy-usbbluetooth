#!/usr/bin/env python
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2025 Antonio Vázquez Blanco <antoniovazquezblanco@gmail.com>
#

import time
from usbbluetooth import Controller
from scapy.compat import raw
from scapy.data import MTU
from scapy.layers.bluetooth import HCI_Hdr
from scapy.supersocket import SuperSocket


class UsbBluetoothSocket(SuperSocket):
    def __init__(self, dev: Controller) -> None:
        self._dev = dev
        self._dev.open()

    def __del__(self):
        # Workarround to avoid the SEGFAULT case on libusb.
        # self._dev.close() should not be called from a destructor.
        # this disables SuperSocket.__del__ that calls UsbBluetoothSocket.close()
        super().close()


    def send(self, x):
        # type: (Packet) -> int
        if HCI_Hdr not in x:
            raise Exception('TODO')
        sx = raw(x)
        self._dev.write(sx)
        x.sent_time = time.time()
        return len(sx)

    def recv_raw(self, x=MTU):
        # type: (int) -> Tuple[Optional[Type[Packet]], Optional[bytes], Optional[float]]  # noqa: E501
        """Returns a tuple containing (cls, pkt_data, time)"""
        data = self._dev.read(x)
        return HCI_Hdr, data, None

    def fileno(self):
        # type: () -> int
        raise NotImplementedError

    def close(self) -> None:
        self._dev.close()
        super().close()

    @staticmethod
    def select(sockets, remain=None):
        # type: (List[SuperSocket], Optional[float]) -> List[SuperSocket]
        return sockets
