from random import random, randint
from poke_moves import *

class Pokemon(object):
	
	def __init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves):
		self.name = name
		self.moredmg = moredmg
		self.lessdmg = lessdmg
		self.nodmg = nodmg
		self.hp = hp
		self.speed = speed
		self.moves = moves
	
	
	def handle_miss(self, abil_type, power, acc, effect, effect_chance, crit):
		
		hit = None
		miss = random()
		miss_chance = acc / 100
		
		if miss < miss_chance:
			hit = 1
			print "This attack will hit."	
		else:
			hit = 0
			print "This attack will miss."	
			return hit
		
		e_hit = None
		e_miss = random()
		e_miss_chance = effect_chance / 100
		
		if e_miss < e_miss_chance:
			e_hit = 1
			print "This status effect will affect the pokemon."	
		else:
			e_hit = 0
			print "This status effect will not affect the pokemon."
		
		if e_hit == 1:
			self.handle_dmg(abil_type, power, effect, crit)
		else:
			effect = None
			self.handle_dmg(abil_type, power, effect, crit)
	
	
	def handle_dmg(self, abil_type, power, effect, crit):
		
		effective_dmg = None
		
		if abil_type in self.moredmg:
			power = power * 2
			print "This will be super effective."
			self.handle_crit(power, effect, crit)
		elif abil_type in self.lessdmg:
			power = power / 2
			print "This will not be very effective."
			self.handle_crit(power, effect, crit)
		elif abil_type in self.nodmg:
			power = 0
			print "This will not affect %s." % self.name	
		else:
			print "This will be normally effective."
			self.handle_crit(power, effect, crit)
	
	
	def handle_crit(self, power, effect, crit):
		
		crit_chance = random()
		
		if crit == 'yes' and crit_chance < .13:
			power = power + (power * .5)
			print "This will critically hit!"
		elif crit_chance < .07:
			power = power + (power * .5)
			print "This will critically hit!"
		else:
			print "This will not critically hit."
		
		if effect != None:
			self.handle_effect(power, effect)
		else:
			self.handle_hp(power)
	
	
	def handle_effect(self, power, effect):
		
		print "%s now has %s!" % (self.name, effect.upper())
		self.handle_hp(power)
	
	
	def handle_hp(self, power):
		
		self.hp = self.hp - power
		print "%s's HP: %d" % (self.name, self.hp)
	
	


class Aerodactyl(Pokemon):
	def __init__(self):
		name = "Aerodactyl"
		moredmg = ['water','electric','ice','rock','steel']
		lessdmg = ['normal','fire','poison','flying','bug']
		nodmg = []
		hp = 270
		speed = 265
		moves = {
			'move1':hyperbeam,
			'move2':ancientpower,
			'move3':wingattack,
			'move4':scaryface
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Alakazam(Pokemon):
	
	def __init__(self):
		name = "Alakazam"
		moredmg = ['bug','ghost','dark']
		lessdmg = ['fight','psychic']
		nodmg = []
		hp = 220
		speed = 245
		moves = {
			'move1':psychic,
			'move2':futuresight,
			'move3':recover,
			'move4':reflect
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Arbok(Pokemon):
	
	def __init__(self):
		name = "Arbok"
		moredmg = ['ground','psychic']
		lessdmg = ['grass','fight','poison','bug']
		nodmg = []
		hp = 230
		speed = 165
		moves = {
			'move1':sludgebomb,
			'move2':irontail,
			'move3':screech,
			'move4':bite
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Charizard(Pokemon):
	
	def __init__(self):
		name = "Charizard"
		moredmg = ['water','electric','rock']
		lessdmg = ['fire','grass','fight','bug','steel']
		nodmg = ['ground']
		hp = 266
		speed = 205
		moves = {
			'move1':flareblitz,
			'move2':flamethrower,
			'move3':fly,
			'move4':brickbreak
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Dewgong(Pokemon):
	
	def __init__(self):
		name = "Dewgong"
		moredmg = ['electric','grass','fight','rock']
		lessdmg = ['water','ice']
		nodmg = []
		hp = 290
		speed = 145
		moves = {
			'move1':surf,
			'move2':hail,
			'move3':safeguard,
			'move4':icebeam
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Dragonair(Pokemon):
	
	def __init__(self):
		name = "Dragonair"
		moredmg = ['ice','dragon']
		lessdmg = ['fire','water','electric','grass']
		nodmg = []
		hp = 232
		speed = 145
		moves = {
			'move1':hyperbeam,
			'move2':safeguard,
			'move3':dragonrush,
			'move4':outrage
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
	


class Dragonite(Pokemon):
	
	def __init__(self):
		name = "Dragonite"
		moredmg = ['ice','rock','dragon']
		lessdmg = ['fire','water','grass','fight','bug']
		nodmg = ['ground']
		hp = 292
		speed = 165
		moves = {
			'move1':hyperbeam,
			'move2':safeguard,
			'move3':wingattack,
			'move4':outrage
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Exeggutor(Pokemon):
	
	def __init__(self):
		name = "Exeggutor"
		moredmg = ['fire','ice','poison','flying','bug','ghost','dark']
		lessdmg = ['water','electric','grass','fight','ground','psychic']
		nodmg = []
		hp = 300
		speed = 115
		moves = {
			'move1':gigadrain,
			'move2':eggbomb,
			'move3':sleeppowder,
			'move4':lightscreen
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Gengar(Pokemon):
	
	def __init__(self):
		name = "Gengar"
		moredmg = ['ground','psychic','ghost','dark']
		lessdmg = ['grass','poison','bug']
		nodmg = ['normal','fight']
		hp = 230
		speed = 225
		moves = {
			'move1':shadowball,
			'move2':sludgebomb,
			'move3':hypnosis,
			'move4':dreameater
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Golbat(Pokemon):
	
	def __init__(self):
		name = "Golbat"
		moredmg = ['electric','ice','psychic','rock']
		lessdmg = ['grass','fight','poison','bug']
		nodmg = ['ground']
		hp = 260
		speed = 185
		moves = {
			'move1':confuseray,
			'move2':bite,
			'move3':aircutter,
			'move4':poisonfang
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Gyarados(Pokemon):
	
	def __init__(self):
		name = "Gyarados"
		moredmg = ['electric','rock']
		lessdmg = ['fire','water','fight','bug','steel']
		nodmg = ['ground']
		hp = 300
		speed = 167
		moves = {
			'move1':aquatail,
			'move2':thunder,
			'move3':icebeam,
			'move4':darkpulse
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Hitmonchan(Pokemon):
	
	def __init__(self):
		name = "Hitmonchan"
		moredmg = ['flying','psychic']
		lessdmg = ['bug','rock','dark']
		nodmg = []
		hp = 210
		speed = 250
		moves = {
			'move1':skyuppercut,
			'move2':machpunch,
			'move3':rocktomb,
			'move4':counter
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Lapras(Pokemon):
	
	def __init__(self):
		name = "Lapras"
		moredmg = ['electric','grass','fight','rock']
		lessdmg = ['water','ice']
		nodmg = []
		hp = 370
		speed = 125
		moves = {
			'move1':surf,
			'move2':icebeam,
			'move3':bodyslam,
			'move4':confuseray
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Machamp(Pokemon):
	
	def __init__(self):
		name = "Machamp"
		moredmg = ['flying','psychic']
		lessdmg = ['bug','rock','dark']
		nodmg = []
		hp = 290
		speed = 115
		moves = {
			'move1':crosschop,
			'move2':bulkup,
			'move3':rocktomb,
			'move4':scaryface
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Mewtwo(Pokemon):
	
	def __init__(self):
		name = "Mewtwo"
		moredmg = ['bug','ghost','dark']
		lessdmg = ['fight','psychic']
		nodmg = []
		hp = 322
		speed = 265
		moves = {
			'move1':psychic,
			'move2':recover,
			'move3':aurasphere,
			'move4':energyball
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Onyx(Pokemon):
	
	def __init__(self):
		name = "Onyx"
		moredmg = ['water','grass','ice','fight','ground','steel']
		lessdmg = ['normal','fire','poison','flying','rock']
		nodmg = ['electric']
		hp = 340
		speed = 145
		moves = {
			'move1':earthquake,
			'move2':roar,
			'move3':rocktomb,
			'move4':irontail
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Rhydon(Pokemon):
	
	def __init__(self):
		name = "Rhydon"
		moredmg = ['water','grass','ice','fight','ground','steel']
		lessdmg = ['normal','fire','poison','flying','rock']
		nodmg = ['electric']
		hp = 320
		speed = 85
		moves = {
			'move1':takedown,
			'move2':earthquake,
			'move3':scaryface,
			'move4':rocktomb
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	


class Slowbro(Pokemon):
	
	def __init__(self):
		name = "Slowbro"
		moredmg = ['electric','grass','bug','ghost','dark']
		lessdmg = ['fire','water','ice','fight','psychic','steel']
		nodmg = []
		hp = 300
		speed = 65
		moves = {
			'move1':surf,
			'move2':icebeam,
			'move3':yawn,
			'move4':amnesia
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
