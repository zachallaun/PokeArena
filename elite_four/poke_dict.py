from random import random, randint
from poke_moves import *

class Pokemon(object):
	
	def __init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status):
		self.name = name
		self.moredmg = moredmg
		self.lessdmg = lessdmg
		self.nodmg = nodmg
		self.hp = hp
		self.speed = speed
		self.moves = moves
		self.status = status
	
	
	def initialize(self):
		self.maxhp = self.hp
		self.hpinc = self.maxhp / 20.0
		self.flinch = 0
		self.recharge = 0
		self.move = 1
	
	
	def handle_miss(self, abil_type, power, acc, crit):
		
		miss = random()
		miss_chance = acc / 100.0
		
		if power != 0:
			if miss < miss_chance and power != 0:
				self.handle_dmg(abil_type, power, crit)
			else:
				print "The attack misses!"
	
	
	def handle_dmg(self, abil_type, power, crit):
		
		effective_dmg = None
		
		if abil_type in self.moredmg:
			power = power * 2
			print "It's super effective!"
			self.handle_crit(power, crit)
		elif abil_type in self.lessdmg:
			power = power / 2
			print "It's not very effective..."
			self.handle_crit(power, crit)
		elif abil_type in self.nodmg:
			power = 0
			print "It doesn't affect %s." % self.name	
		else:
			self.handle_crit(power, crit)
	
	
	def handle_crit(self, power, crit):
		
		crit_chance = random()
		
		if crit == 'yes' and crit_chance < .13:
			power = power + (power * .5)
			print "It's a critical hit!"
		elif crit_chance < .07:
			power = power + (power * .5)
			print "It's a critical hit!"
		
		self.handle_hp(power)
	
	
	def handle_hp(self, power):
		if power != 0:
			self.hp = self.hp - power
			print "It hits %s for %d!" % (self.name, power)
	
	
	def attack(self, target, move):
		target.handle_miss(
			self.moves[move].abil_type, 
			self.moves[move].power,
			self.moves[move].acc,
			self.moves[move].crit
		)
	
	
	def pass_effect(self, attacker, opp, move):
		if attacker.moves[move].effect.effect_dict['target'] == 'self':
			target = attacker
		else:
			target = opp
		
		target.handle_effect(attacker.moves[move].effect, attacker.moves[move].effect_chance)
	
	
	def handle_effect(self, effect, effect_chance):
		
		e_miss = random()
		e_miss_chance = effect_chance / 100.0
		
		if e_miss < e_miss_chance:
			
			if effect.effect_dict['target'] == 'self' and 'effect_pwr' in effect.effect_dict:
				self.hp = self.hp + effect.effect_dict['effect_pwr']
				if self.hp > self.maxhp:
					self.hp = self.maxhp
					
			if effect == sheer_cold_effect:
				self.hp = self.hp - effect.effect_dict['effect_pwr']
			elif effect == flinch:
				self.flinch = 1
			elif effect == recharge:
				self.recharge = 1
			elif effect == paralyze:
				self.para = 1
			elif effect == freeze:
				self.freeze = 1
			
			if self.status == None:
				try:
					self.status = effect.effect_dict['status']
				except:
					pass
			
			print effect.effect_dict['printed'] % self.name
			
		else:
			if effect == sheer_cold_effect:
				print "The attack misses!"
			effect = None
	
	


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
			'move4':stoneedge
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move2':thunderwave,
			'move3':recover,
			'move4':shadowball
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move3':gunkshot,
			'move4':bite
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move3':dragonrush,
			'move4':wingattack
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move2':signalbeam,
			'move3':gigaimpact,
			'move4':icebeam
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move2':aquatail,
			'move3':dragonrush,
			'move4':thunderbolt
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	
	


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
			'move2':thunderbolt,
			'move3':wingattack,
			'move4':dragonrush
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move3':leafstorm,
			'move4':psyshock
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move3':lick,
			'move4':darkpulse
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


class Golbat(Pokemon):
	
	def __init__(self):
		name = "Golbat"
		moredmg = ['electric','ice','psychic','rock']
		lessdmg = ['grass','fight','poison','bug']
		nodmg = ['ground']
		hp = 260
		speed = 185
		moves = {
			'move1':toxic,
			'move2':bite,
			'move3':aircutter,
			'move4':poisonfang
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move4':firepunch
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move4':sheercold
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move2':earthquake,
			'move3':rocktomb,
			'move4':brickbreak
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move2':stoneedge,
			'move3':rocktomb,
			'move4':irontail
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move3':poisonjab,
			'move4':rocktomb
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


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
			'move3':psychic,
			'move4':gigaimpact
		}
		status = None
		Pokemon.__init__(self, name, moredmg, lessdmg, nodmg, hp, speed, moves, status)
	


poke_list = ['Aerodactyl','Alakazam','Arbok','Charizard','Dewgong','Dragonair','Dragonite','Exeggutor','Gengar','Golbat','Gyarados','Hitmonchan','Lapras','Machamp','Mewtwo','Onyx','Rhydon','Slowbro']