try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'PokeArena',
	'author': 'Zach Allaun',
	'download_url': 'https://github.com/zachallaun/PokeArena',
	'author': 'zach@gamegnat.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['pokearena'],
	'scripts': ['poke_helper.py','poke_dict.py','poke_moves.py','poke_effects.py'],
	'name': 'pokearena',
}

setup(**config)