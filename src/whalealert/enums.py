from enum import Enum, auto


class Plan(Enum):
    FREE = auto()
    PERSONAL = auto()


class Blockchain(Enum):
    btc = 'bitcoin'
    eth = 'ethereum'
    xrp = 'ripple'
    neo = 'neo'
    eos = 'eos'
    trx = 'tron'
    xlm = 'stellar'
    bnb = 'binancechain'
    xtz = 'tezos'
    atom = 'cosmos'
    usdt = 'liquid'
    hive = 'hive'
    steem = 'steem'
    icx = 'icon'
