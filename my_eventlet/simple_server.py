#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import eventlet

def handle(client):
    while True:
        c=client.recv(1024)
        if not c:
            break

        client.sendall(c)

server=eventlet.listen(('0.0.0.0',6000))

pool=eventlet.GreenPool(1000)

while True:
    new_sock,address=server.accept()
    pool.spawn_n(handle,new_sock)