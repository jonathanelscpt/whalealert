==========
WhaleAlert
==========

Overview
--------

This is a minimalistic python REST API client for the https://docs.whale-alert.io API.

Installation
------------

The project is built with poetry.  To install the defined dependencies, just run the install command.

::

    poetry install


Authentication
--------------

Whale Alert uses API keys for access to the API. To create an API key please sign up `here <https://whale-alert.io/account>`_.

Each API request should target REST URI: https://api.whale-alert.io/v1 .  This library implements a :code:`X-WA-API-KEY` request header.


Authentication
--------------

To use the WhaleAlert API client:


.. code-block:: python

    from whalealert import WhaleAlert
    import whalealert.utils as utils
    from whalealert.enums import Blockchain

    api_key = 'xxxxxxxxxxxxxxxxxxx'

    client = WhaleAlert(api_key=api_key)
    recent = datetime.datetime.now() - datetime.timedelta(minutes=30)
    resp = c.transactions(start=utils.ephoch_time(recent), currency=Blockchain.btc.name)
    print(resp)



Donate
------

If this library has helped you or if you would like to support future development, donations are most welcome:

==============  ==========================================
Cryptocurrency  Address
==============  ==========================================
 **BTC**        38c7QWggrB2HLUJZFmhAC2zh4t8C57c1ec
 **ETH**        0x01eD3b58a07c6d005281Db76e6c1AE2bfF2226AD
==============  ==========================================