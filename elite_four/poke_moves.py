class PokeMoves(object):
	
	def __init__(self, name, abil_type, power, acc, effect, effect_chance, crit):
		self.name = name
		self.abil_type = abil_type
		self.power = power
		self.acc = acc
		self.effect = effect
		self.effect_chance = effect_chance
		self.crit = crit
	
	
	def pass_attack(self, name, abil_type, power, acc, effect, effect_chance, crit):
		
	
	


class AerialAce(PokeMoves):
	
	def __init__(self):
		name = "Aerial Ace"
		abil_type = 'flying'
		power = 65
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class AirCutter(PokeMoves):
	
	def __init__(self):
		name = "Air Cutter"
		abil_type = 'flying'
		power = 55
		acc = 95
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)


class Amnesia(PokeMoves):
	def __init__(self):
		name = "Amnesia"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['def_up_2']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class AncientPower(PokeMoves):
	def __init__(self):
		name = "Ancient Poer"
		abil_type = 'rock'
		power = 60
		acc = 100
		effect = ['atk_up_1','def_up_1']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class AquaTail(PokeMoves):
	def __init__(self):
		name = "Aqua Tail"
		abil_type = 'water'
		power = 90
		acc = 90
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class AuraSphere(PokeMoves):
	def __init__(self):
		name = "Aura Sphere"
		abil_type = 'fight'
		power = 90
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Bite(PokeMoves):
	def __init__(self):
		name = "Bite"
		abil_type = 'dark'
		power = 65
		acc = 100
		effect = ['flinch']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class BodySlam(PokeMoves):
	def __init__(self):
		name = "Body Slam"
		abil_type = 'normal'
		power = 85
		acc = 100
		effect = ['paralyze']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class BrickBreak(PokeMoves):
	def __init__(self):
		name = "Brick Break"
		abil_type = 'fight'
		power = 75
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class BulkUp(PokeMoves):
	def __init__(self):
		name = "Bulk Up"
		abil_type = 'fight'
		power = 0
		acc = 100
		effect = ['atk_up_1','def_up_1']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class ConfuseRay(PokeMoves):
	def __init__(self):
		name = "Confuse Ray"
		abil_type = 'ghost'
		power = 0
		acc = 100
		effect = ['confuse']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Counter(PokeMoves):
	def __init__(self):
		name = "Counter"
		abil_type = 'fight'
		power = 0
		acc = 100
		effect = ['counter']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class CrossChop(PokeMoves):
	def __init__(self):
		name = "Cross Chop"
		abil_type = 'fight'
		power = 100
		acc = 80
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class DarkPulse(PokeMoves):
	def __init__(self):
		name = "Dark Pulse"
		abil_type = 'dark'
		power = 80
		acc = 100
		effect = ['flinch']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class DragonRush(PokeMoves):
	def __init__(self):
		name = "Dragon Rush"
		abil_type = 'dragon'
		power = 100
		acc = 75
		effect = ['flinch']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class DreamEater(PokeMoves):
	def __init__(self):
		name = "Dream Eater"
		abil_type = 'psychic'
		power = 100
		acc = 100
		effect = ['user_hp_50','must_asleep']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Earthquake(PokeMoves):
	def __init__(self):
		name = "Earthquake"
		abil_type = 'ground'
		power = 100
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class EggBomb(PokeMoves):
	def __init__(self):
		name = "Egg Bomb"
		abil_type = 'normal'
		power = 100
		acc = 75
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class EnergyBall(PokeMoves):
	def __init__(self):
		name = "Energy Ball"
		abil_type = 'grass'
		power = 80
		acc = 100
		effect = ['def_down_1']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class FireSpin(PokeMoves):
	def __init__(self):
		name = "Fire Spin"
		abil_type = 'fire'
		power = 35
		acc = 85
		effect = ['fire_spin']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Flamethrower(PokeMoves):
	def __init__(self):
		name = "Flamethrower"
		abil_type = 'fire'
		power = 95
		acc = 100
		effect = ['burn']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class FlareBlitz(PokeMoves):
	def __init__(self):
		name = "FlareBlitz"
		abil_type = 'fire'
		power = 120
		acc = 100
		effect = ['user_recoil_33']
		effect_chance = 100
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Fly(PokeMoves):
	def __init__(self):
		name = "Fly"
		abil_type = 'flying'
		power = 0
		acc = 100
		effect = ['fly_user','fly_target']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class FutureSight(PokeMoves):
	def __init__(self):
		name = "Future Sight"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['future_sight']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class GigaDrain(PokeMoves):
	def __init__(self):
		name = "Giga Drain"
		abil_type = 'grass'
		power = 75
		acc = 100
		effect = ['user_hp_50']
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Hail(PokeMoves):
	def __init__(self):
		name = "Hail"
		abil_type = 'ice'
		power = 0
		acc = 100
		effect = ['hail']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class HyperBeam(PokeMoves):
	def __init__(self):
		name = "Hyper Beam"
		abil_type = 'normal'
		power = 150
		acc = 90
		effect = ['recharge']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Hypnosis(PokeMoves):
	def __init__(self):
		name = "Hypnosis"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['sleep']
		effect_chance = 70
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class IceBeam(PokeMoves):
	def __init__(self):
		name = "Ice Beam"
		abil_type = 'ice'
		power = 95
		acc = 100
		effect = ['frozen']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class IronTail(PokeMoves):
	def __init__(self):
		name = "Iron Tail"
		abil_type = 'steel'
		power = 100
		acc = 75
		effect = ['def_down_1']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class LightScreen(PokeMoves):
	def __init__(self):
		name = "Light Screen"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['dmg_down_30']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class MachPunch(PokeMoves):
	def __init__(self):
		name = "Mach Punch"
		abil_type = 'fight'
		power = 50
		acc = 100
		effect = ['hit_first']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Outrage(PokeMoves):
	def __init__(self):
		name = "Outrage"
		abil_type = 'dragon'
		power = 120
		acc = 100
		effect = ['outrage']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class PoisonFang(PokeMoves):
	def __init__(self):
		name = "Poison Fang"
		abil_type = 'poison'
		power = 50
		acc = 100
		effect = ['poison']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Psychic(PokeMoves):
	def __init__(self):
		name = "Psychic"
		abil_type = 'psychic'
		power = 90
		acc = 100
		effect = ['def_down_1']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Recover(PokeMoves):
	def __init__(self):
		name = "Recover"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['recover']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Reflect(PokeMoves):
	def __init__(self):
		name = "Reflect"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['reflect']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Roar(PokeMoves):
	def __init__(self):
		name = "Roar"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['roar']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class RockTomb(PokeMoves):
	def __init__(self):
		name = "Rock Tomb"
		abil_type = 'rock'
		power = 50
		acc = 80
		effect = ['speed_down_1']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Safeguard(PokeMoves):
	def __init__(self):
		name = "Safeguard"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['safeguard']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class ScaryFace(PokeMoves):
	def __init__(self):
		name = "Scary Face"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['speed_down_2']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Screech(PokeMoves):
	def __init__(self):
		name = "Screech"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['def_down_2']
		effect_chance = 85
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class ShadowBall(PokeMoves):
	def __init__(self):
		name = "Shadow Ball"
		abil_type = 'ghost'
		power = 80
		acc = 100
		effect = ['def_down_1']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class SkyUppercut(PokeMoves):
	def __init__(self):
		name = "Sky Uppercut"
		abil_type = 'fight'
		power = 85
		acc = 90
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Slash(PokeMoves):
	def __init__(self):
		name = "Slash"
		abil_type = 'normal'
		power = 70
		acc = 100
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class SleepPowder(PokeMoves):
	def __init__(self):
		name = "Sleep Powder"
		abil_type = 'grass'
		power = 0
		acc = 75
		effect = ['sleep']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class SludgeBomb(PokeMoves):
	def __init__(self):
		name = "Sludge Bomb"
		abil_type = 'poison'
		power = 90
		acc = 100
		effect = ['poison']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Surf(PokeMoves):
	def __init__(self):
		name = "Surf"
		abil_type = 'water'
		power = 95
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class TakeDown(PokeMoves):
	def __init__(self):
		name = "Take Down"
		abil_type = 'normal'
		power = 90
		acc = 85
		effect = ['recoil_25']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Thunder(PokeMoves):
	def __init__(self):
		name = "Thunder"
		abil_type = 'electric'
		power = 120
		acc = 70
		effect = ['paralyze']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class WingAttack(PokeMoves):
	def __init__(self):
		name = "Wing Attack"
		abil_type = 'flying'
		power = 60
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	


class Yawn(PokeMoves):
	def __init__(self):
		name = "Yawn"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['yawn']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	
