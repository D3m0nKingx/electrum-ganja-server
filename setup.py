from setuptools import setup

setup(
    name="electrum-ganja-server",
    version="1.0",
    scripts=['run_electrum_ganja_server.py','electrum-ganja-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumganjaserver':'src'
        },
    py_modules=[
        'electrumganjaserver.__init__',
        'electrumganjaserver.utils',
        'electrumganjaserver.storage',
        'electrumganjaserver.deserialize',
        'electrumganjaserver.networks',
        'electrumganjaserver.blockchain_processor',
        'electrumganjaserver.server_processor',
        'electrumganjaserver.processor',
        'electrumganjaserver.version',
        'electrumganjaserver.ircthread',
        'electrumganjaserver.stratum_tcp'
    ],
    description="Ganja Electrum Server",
    author="dev0tion",
    license="MIT Licence",
    url="https://github.com/dev0tion/electrum-ganja-server/",
    long_description="""Server for the Electrum Lightweight Ganja Wallet"""
)
