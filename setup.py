try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'PokeArena',
	'author': 'Zach Allaun',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author': 'zach@gamegnat.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['pokearena'],
	'scripts': [],
	'name': 'pokearena',
}

setup(**config)