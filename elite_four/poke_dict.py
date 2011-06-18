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
			'move1':'Hyper Beam',
			'move2':'Ancient Power',
			'move3':'Wing Attack',
			'move4':'Scary Face'
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
			'move1':'Psychic',
			'move2':'Future Sight',
			'move3':'Recover',
			'move4':'Reflect'
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
			'move1':'Sludge Bomb',
			'move2':'Iron Tail',
			'move3':'Screech',
			'move4':'Bite'
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
			'move1':'Flare Blitz',
			'move2':'Flamethrower',
			'move3':'Fly',
			'move4':'Brick Break'
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
			'move1':'Surf',
			'move2':'Hail',
			'move3':'Safeguard',
			'move4':'Ice Beam'
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
			'move1':'Hyper Beam',
			'move2':'Safeguard',
			'move3':'Dragon Rush',
			'move4':'Outrage'
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
			'move1':'Hyper Beam',
			'move2':'Safeguard',
			'move3':'Wing Attack',
			'move4':'Outrage'
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
			'move1':'Giga Drain',
			'move2':'Egg Bomb',
			'move3':'Sleep Powder',
			'move4':'Light Screen'
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
			'move1':'Shadow Ball',
			'move2':'Sludge Bomb',
			'move3':'Hypnosis',
			'move4':'Dream Eater'
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
			'move1':'Confuse Ray',
			'move2':'Bite',
			'move3':'Air Cutter',
			'move4':'Poison Fang'
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
			'move1':'Aqua Tail',
			'move2':'Thunder',
			'move3':'Ice Beam',
			'move4':'Dark Pulse'
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
			'move1':'Sky Uppercut',
			'move2':'Mach Punch',
			'move3':'Rock Tomb',
			'move4':'Counter'
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
			'move1':'Surf',
			'move2':'Ice Beam',
			'move3':'Body Slam',
			'move4':'Confuse Ray'
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
			'move1':'Cross Chop',
			'move2':'Bulk Up',
			'move3':'Rock Tomb',
			'move4':'Scary Face'
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
			'move1':'Psychic',
			'move2':'Recover',
			'move3':'Aura Sphere',
			'move4':'Energy Ball'
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
			'move1':'Earthquake',
			'move2':'Roar',
			'move3':'Rock Tomb',
			'move4':'Iron Tail'
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
			'move1':'Take Down',
			'move2':'Earthquake',
			'move3':'Scary Face',
			'move4':'Rock Tomb'
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
			'move1':'Surf',
			'move2':'Ice Beam',
			'move3':'Yawn',
			'move4':'Amnesia'
		}
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves)
	
