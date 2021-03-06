import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from ruxcryptod import RXCDaemon
from ruxcrypto_config import RXCConfig


def test_ruxcryptod():
    config_text = RXCConfig.slurp_config_file(config.ruxcrypto_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000c63f5826a523923939a5adf28657c2a6b76764f1af99bb39437006489d3'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'0550380d660e6170a1081bc3dc765fb192e689d7310c818dab22c8783408102b'

    creds = RXCConfig.get_rpc_creds(config_text, network)
    ruxcryptod = RXCDaemon(**creds)
    assert ruxcryptod.rpc_command is not None

    assert hasattr(ruxcryptod, 'rpc_connection')

    # RXC testnet block 0 hash == 0550380d660e6170a1081bc3dc765fb192e689d7310c818dab22c8783408102b
    # test commands without arguments
    info = ruxcryptod.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert ruxcryptod.rpc_command('getblockhash', 0) == genesis_hash
