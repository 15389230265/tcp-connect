#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: client.py
socket client
"""

import socket
import sys
import os
import struct


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.190.5.42', 6666))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))
    while 1:
        data = input('please input work: ')
        s.send(data)
        print(s.recv(1024))
        if data == 'exit':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
