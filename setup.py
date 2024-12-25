"""setup.py: setuptools control."""


import re
import os
from setuptools import setup, find_packages

try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        long_descr = '\n' + f.read()
except FileNotFoundError:
    long_descr = """
    The official Linux CLI for ProtonVPN.

    For further information and a usage guide, please view the project page:

    https://github.com/ProtonVPN/linux-cli
    """

version = re.search(
    r'(VERSION = "(\d.\d.\d+)")',
    open("protonvpn_cli/constants.py").read(),
    re.M
).group(2)

setup(
    name="protonvpn_cli",
    version=version,
    packages=find_packages(where='.') + [
        'proton.vpn.connection',
        'proton.vpn.core',
        'proton.vpn.core.refresher',
        'proton.vpn.killswitch.interface',
        'proton.vpn.logging',
        'proton.vpn.session',
        'proton.vpn.session.dataclasses',
        'proton.vpn.session.dataclasses.client_config',
        'proton.vpn.session.dataclasses.servers',
        'proton.vpn.session.servers',
        'proton.keyring',
        'proton.loader',
        'proton.session',
        'proton.session.srp',
        'proton.session.transports',
        'proton.session.transports.utils',
        'proton.sso',
        'proton.utils',
    ],
    package_dir={
        'proton.vpn.connection': 'official_components/api_core/proton/vpn/connection',
        'proton.vpn.core': 'official_components/api_core/proton/vpn/core',
        'proton.vpn.core.refresher': 'official_components/api_core/proton/vpn/core/refresher',
        'proton.vpn.killswitch.interface': 'official_components/api_core/proton/vpn/killswitch/interface',
        'proton.vpn.logging': 'official_components/api_core/proton/vpn/logging',
        'proton.vpn.session': 'official_components/api_core/proton/vpn/session',
        'proton.vpn.session.dataclasses': 'official_components/api_core/proton/vpn/session/dataclasses',
        'proton.vpn.session.dataclasses.client_config': 'official_components/api_core/proton/vpn/session/dataclasses/client_config',
        'proton.vpn.session.dataclasses.servers': 'official_components/api_core/proton/vpn/session/dataclasses/servers',
        'proton.vpn.session.servers': 'official_components/api_core/proton/vpn/session/servers',
        'proton.keyring': 'official_components/core/proton/keyring',
        'proton.loader': 'official_components/core/proton/loader',
        'proton.session': 'official_components/core/proton/session',
        'proton.session.srp': 'official_components/core/proton/session/srp',
        'proton.session.transports': 'official_components/core/proton/session/transports',
        'proton.session.transports.utils': 'official_components/core/proton/session/transports/utils',
        'proton.sso': 'official_components/core/proton/sso',
        'proton.utils': 'official_components/core/proton/utils',
    },
    entry_points={
        "console_scripts": ["protonvpn = protonvpn_cli.cli:main"],
        "proton_loader_keyring": [
            "json = proton.keyring.textfile:KeyringBackendJsonFiles"
        ],
        "proton_loader_transport": [
            "requests = proton.session.transports.requests:RequestsTransport",
            "alternativerouting = proton.session.transports.alternativerouting:AlternativeRoutingTransport",
            "aiohttp = proton.session.transports.aiohttp:AiohttpTransport",
            "auto = proton.session.transports.auto:AutoTransport",
        ],
        "proton_loader_environment": [
            "prod = proton.session.environments:ProdEnvironment",
        ],
        "proton_loader_basicview": [
            "cli = proton.views.basiccli:BasicCLIView"
        ]
    },
    description="Linux command-line client for ProtonVPN",
    long_description=long_descr,
    author="Proton Technologies AG",
    author_email="contact@protonvpn.com",
    license="GPLv3",
    url="https://github.com/protonvpn/linux-cli-community",
    package_data={
        "protonvpn_cli": ["templates/*"]
    },
    install_requires=[
        "requests",
        "docopt",
        "pythondialog",
        "jinja2",
        "distro",
        "bcrypt",
        "PyNaCl",
        "cryptography",
        "aiohttp",
        "python-gnupg",
        "pyopenssl",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
