# -*- coding:utf-8 -*-
"""
"""
__date__ = "30/07/2017"
__author__ = "zhaojm"

from rpc.rpc_mark import mark_rpc


@mark_rpc.mark_rpc()
def on_get_info(conn, args):
    pass


@mark_rpc.mark_rpc()
def on_register(conn, args):
    pass
