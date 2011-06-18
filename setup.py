try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Elite Four Pokefight',
	'author': 'Zach Allaun',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author': 'zach@gamegnat.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['elite_four'],
	'scripts': [],
	'name': 'elite_four_pokefight',
}

setup(**config)