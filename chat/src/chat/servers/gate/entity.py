# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from frame.servers.tcp.tcp_entity import TcpEntity
from chat.servers.gate.connector import Connector


class Entity(TcpEntity):
    def __init__(self):
        super(Entity, self).__init__()
        self._connector = Connector(self)

    def init_rpc(self):
        from .rpc import *
