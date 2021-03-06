# -*- coding:utf-8 -*-
"""
Created on 20/06/2017

@author: zhaojm
"""
from frame.core.entity import Entity


class CmdHandler(Entity):
    def __init__(self):
        self.conn = None
        pass

    def on_conn_made(self, conn):
        self.conn = conn
        pass

    def on_conn_lost(self, conn, reason):
        self.conn = None

    def on_msg(self, conn, msg):
        pass


if __name__ == '__main__':
    from frame.core.reactor import init_stdio, start_reactor

    c = CmdHandler()
    init_stdio(c)
    start_reactor()
