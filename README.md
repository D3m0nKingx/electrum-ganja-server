Electrum-ganja-server for the Electrum-Ganja client
=========================================

  * Original Author: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Ganja port maintainer: demon (Discord: demon#9191)
  * Language: Python

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires ganjacoind (https://github.com/legends420/GanjaCoin), 
    leveldb (apt install liblevedb1v5 libleveldb-dev), and plyvel (pip install plyvel)

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Ganja addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-ganja-server' script



License
-------

Electrum-ganja-server is made available under the terms of the MIT License.
See the included `LICENSE` for more details.
