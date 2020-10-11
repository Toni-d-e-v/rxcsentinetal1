"""
    Set up defaults and read sentinel.conf
"""
import sys
import os
from rxc_config import RXCConfig

default_sentinel_config = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '../sentinel.conf')
)
sentinel_config_file = os.environ.get('SENTINEL_CONFIG', default_sentinel_config)
sentinel_cfg = RXCConfig.tokenize(sentinel_config_file)
sentinel_version = "1.4.0"


def get_ruxcrypto_conf():
    if sys.platform == 'win32':
        rxc_config = os.path.join(os.getenv('APPDATA'), "ruxcrypto/ruxcrypto.conf")
    else:
        home = os.environ.get('HOME')

        rxc_config = os.path.join(home, ".ruxcrypto/ruxcrypto.conf")
        if sys.platform == 'darwin':
            rxc_config = os.path.join(home, "Library/Application Support/ruxcrypto/ruxcrypto.conf")

    rxc_config = sentinel_cfg.get('ruxcrypto_conf', ruxcrypto_conf)

    return ruxcrypto_conf


def get_network():
    return sentinel_cfg.get('network', 'mainnet')


def get_rpchost():
    return sentinel_cfg.get('rpchost', '127.0.0.1')


def sqlite_test_db_name(sqlite_file_path):
    (root, ext) = os.path.splitext(sqlite_file_path)
    test_sqlite_file_path = root + '_test' + ext
    return test_sqlite_file_path


def get_db_conn():
    import peewee
    env = os.environ.get('SENTINEL_ENV', 'production')

    # default values should be used unless you need a different config for development
    db_host = sentinel_cfg.get('db_host', '127.0.0.1')
    db_port = sentinel_cfg.get('db_port', None)
    db_name = sentinel_cfg.get('db_name', 'sentinel')
    db_user = sentinel_cfg.get('db_user', 'sentinel')
    db_password = sentinel_cfg.get('db_password', 'sentinel')
    db_charset = sentinel_cfg.get('db_charset', 'utf8mb4')
    db_driver = sentinel_cfg.get('db_driver', 'sqlite')

    if (env == 'test'):
        if db_driver == 'sqlite':
            db_name = sqlite_test_db_name(db_name)
        else:
            db_name = "%s_test" % db_name

    peewee_drivers = {
        'mysql': peewee.MySQLDatabase,
        'postgres': peewee.PostgresqlDatabase,
        'sqlite': peewee.SqliteDatabase,
    }
    driver = peewee_drivers.get(db_driver)

    dbpfn = 'passwd' if db_driver == 'mysql' else 'password'
    db_conn = {
        'host': db_host,
        'user': db_user,
        dbpfn: db_password,
    }
    if db_port:
        db_conn['port'] = int(db_port)

    if driver == peewee.SqliteDatabase:
        db_conn = {}

    db = driver(db_name, **db_conn)

    return db


ruxcrypto_conf = get_ruxcrypto_conf()
network = get_network()
rpc_host = get_rpchost()
db = get_db_conn()
