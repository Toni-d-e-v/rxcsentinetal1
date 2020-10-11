"""
dashd JSONRPC interface
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import config
import base58
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from masternode import Masternode
from decimal import Decimal
import time
from ruxcryptod import ruxcryptod


class RXCDaemon(ruxcryptod):

    @classmethod
    def from_ruxcrypto_conf(self, ruxcrypto_dot_conf):
        from rxc_config import RXCConfig
        config_text = RXCConfig.slurp_config_file(ruxcrypto_dot_conf)
        creds = RXCConfig.get_rpc_creds(config_text, config.network)

        creds[u'host'] = config.rpc_host

        return self(**creds)

    @classmethod
    def from_rxc_conf(self, rxc_dot_conf):
        raise RuntimeWarning('This method should not be used with RXC')


