class PokeMoves(object):
	
	def __init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit):
		self.move_name = move_name
		self.abil_type = abil_type
		self.power = power
		self.acc = acc
		self.effect = effect
		self.effect_chance = effect_chance
		self.crit = crit
	
	


class AerialAce(PokeMoves):
	
	def __init__(self):
		move_name = "Aerial Ace"
		abil_type = 'flying'
		power = 65
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

aerialace = AerialAce()
class AirCutter(PokeMoves):
	
	def __init__(self):
		move_name = "Air Cutter"
		abil_type = 'flying'
		power = 55
		acc = 95
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)

aircutter = AirCutter()
class Amnesia(PokeMoves):
	def __init__(self):
		move_name = "Amnesia"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['def_up_2']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

amnesia = Amnesia()
class AncientPower(PokeMoves):
	def __init__(self):
		move_name = "Ancient Poer"
		abil_type = 'rock'
		power = 60
		acc = 100
		effect = ['atk_up_1','def_up_1']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

ancientpower = AncientPower()
class AquaTail(PokeMoves):
	def __init__(self):
		move_name = "Aqua Tail"
		abil_type = 'water'
		power = 90
		acc = 90
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

aquatail = AquaTail()
class AuraSphere(PokeMoves):
	def __init__(self):
		move_name = "Aura Sphere"
		abil_type = 'fight'
		power = 90
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

aurasphere = AuraSphere()
class Bite(PokeMoves):
	def __init__(self):
		move_name = "Bite"
		abil_type = 'dark'
		power = 65
		acc = 100
		effect = ['flinch']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

bite = Bite()
class BodySlam(PokeMoves):
	def __init__(self):
		move_name = "Body Slam"
		abil_type = 'normal'
		power = 85
		acc = 100
		effect = ['paralyze']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

bodyslam = BodySlam()
class BrickBreak(PokeMoves):
	def __init__(self):
		move_name = "Brick Break"
		abil_type = 'fight'
		power = 75
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

brickbreak = BrickBreak()
class BulkUp(PokeMoves):
	def __init__(self):
		move_name = "Bulk Up"
		abil_type = 'fight'
		power = 0
		acc = 100
		effect = ['atk_up_1','def_up_1']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

bulkup = BulkUp()
class ConfuseRay(PokeMoves):
	def __init__(self):
		move_name = "Confuse Ray"
		abil_type = 'ghost'
		power = 0
		acc = 100
		effect = ['confuse']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

confuseray = ConfuseRay()
class Counter(PokeMoves):
	def __init__(self):
		move_name = "Counter"
		abil_type = 'fight'
		power = 0
		acc = 100
		effect = ['counter']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

counter = Counter()
class CrossChop(PokeMoves):
	def __init__(self):
		move_name = "Cross Chop"
		abil_type = 'fight'
		power = 100
		acc = 80
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

crosschop = CrossChop()
class DarkPulse(PokeMoves):
	def __init__(self):
		move_name = "Dark Pulse"
		abil_type = 'dark'
		power = 80
		acc = 100
		effect = ['flinch']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

darkpulse = DarkPulse()
class DragonRush(PokeMoves):
	def __init__(self):
		move_name = "Dragon Rush"
		abil_type = 'dragon'
		power = 100
		acc = 75
		effect = ['flinch']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

dragonrush = DragonRush()
class DreamEater(PokeMoves):
	def __init__(self):
		move_name = "Dream Eater"
		abil_type = 'psychic'
		power = 100
		acc = 100
		effect = ['user_hp_50','must_asleep']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

dreameater = DreamEater()
class Earthquake(PokeMoves):
	def __init__(self):
		move_name = "Earthquake"
		abil_type = 'ground'
		power = 100
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

earthquake = Earthquake()
class EggBomb(PokeMoves):
	def __init__(self):
		move_name = "Egg Bomb"
		abil_type = 'normal'
		power = 100
		acc = 75
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

eggbomb = EggBomb()
class EnergyBall(PokeMoves):
	def __init__(self):
		move_name = "Energy Ball"
		abil_type = 'grass'
		power = 80
		acc = 100
		effect = ['def_down_1']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

energyball = EnergyBall()
class FireSpin(PokeMoves):
	def __init__(self):
		move_name = "Fire Spin"
		abil_type = 'fire'
		power = 35
		acc = 85
		effect = ['fire_spin']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

firespin = FireSpin()
class Flamethrower(PokeMoves):
	def __init__(self):
		move_name = "Flamethrower"
		abil_type = 'fire'
		power = 95
		acc = 100
		effect = ['burn']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

flamethrower = Flamethrower()
class FlareBlitz(PokeMoves):
	def __init__(self):
		move_name = "FlareBlitz"
		abil_type = 'fire'
		power = 120
		acc = 100
		effect = ['user_recoil_33']
		effect_chance = 100
		crit = 'yes'
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

flareblitz = FlareBlitz()
class Fly(PokeMoves):
	def __init__(self):
		move_name = "Fly"
		abil_type = 'flying'
		power = 0
		acc = 100
		effect = ['fly_user','fly_target']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

fly = Fly()
class FutureSight(PokeMoves):
	def __init__(self):
		move_name = "Future Sight"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['future_sight']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

futuresight = FutureSight()
class GigaDrain(PokeMoves):
	def __init__(self):
		move_name = "Giga Drain"
		abil_type = 'grass'
		power = 75
		acc = 100
		effect = ['user_hp_50']
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

gigadrain = GigaDrain()
class Hail(PokeMoves):
	def __init__(self):
		move_name = "Hail"
		abil_type = 'ice'
		power = 0
		acc = 100
		effect = ['hail']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

hail = Hail()
class HyperBeam(PokeMoves):
	def __init__(self):
		move_name = "Hyper Beam"
		abil_type = 'normal'
		power = 150
		acc = 90
		effect = ['recharge']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

hyperbeam = HyperBeam()
class Hypnosis(PokeMoves):
	def __init__(self):
		move_name = "Hypnosis"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['sleep']
		effect_chance = 70
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

hypnosis = Hypnosis()
class IceBeam(PokeMoves):
	def __init__(self):
		move_name = "Ice Beam"
		abil_type = 'ice'
		power = 95
		acc = 100
		effect = ['frozen']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

icebeam = IceBeam()
class IronTail(PokeMoves):
	def __init__(self):
		move_name = "Iron Tail"
		abil_type = 'steel'
		power = 100
		acc = 75
		effect = ['def_down_1']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

irontail = IronTail()
class LightScreen(PokeMoves):
	def __init__(self):
		move_name = "Light Screen"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['dmg_down_30']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

lightscreen = LightScreen()
class MachPunch(PokeMoves):
	def __init__(self):
		move_name = "Mach Punch"
		abil_type = 'fight'
		power = 50
		acc = 100
		effect = ['hit_first']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

machpunch = MachPunch()
class Outrage(PokeMoves):
	def __init__(self):
		move_name = "Outrage"
		abil_type = 'dragon'
		power = 120
		acc = 100
		effect = ['outrage']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

outrage = Outrage()
class PoisonFang(PokeMoves):
	def __init__(self):
		move_name = "Poison Fang"
		abil_type = 'poison'
		power = 50
		acc = 100
		effect = ['poison']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

poisonfang = PoisonFang()
class Psychic(PokeMoves):
	def __init__(self):
		move_name = "Psychic"
		abil_type = 'psychic'
		power = 90
		acc = 100
		effect = ['def_down_1']
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

psychic = Psychic()
class Recover(PokeMoves):
	def __init__(self):
		move_name = "Recover"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['recover']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

recover = Recover()
class Reflect(PokeMoves):
	def __init__(self):
		move_name = "Reflect"
		abil_type = 'psychic'
		power = 0
		acc = 100
		effect = ['reflect']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

reflect = Reflect()
class Roar(PokeMoves):
	def __init__(self):
		move_name = "Roar"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['roar']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

roar = Roar()
class RockTomb(PokeMoves):
	def __init__(self):
		move_name = "Rock Tomb"
		abil_type = 'rock'
		power = 50
		acc = 80
		effect = ['speed_down_1']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

rocktomb = RockTomb()
class Safeguard(PokeMoves):
	def __init__(self):
		move_name = "Safeguard"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['safeguard']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

safeguard = Safeguard()
class ScaryFace(PokeMoves):
	def __init__(self):
		move_name = "Scary Face"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['speed_down_2']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

scaryface = ScaryFace()
class Screech(PokeMoves):
	def __init__(self):
		move_name = "Screech"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['def_down_2']
		effect_chance = 85
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

screech = Screech()
class ShadowBall(PokeMoves):
	def __init__(self):
		move_name = "Shadow Ball"
		abil_type = 'ghost'
		power = 80
		acc = 100
		effect = ['def_down_1']
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

shadowball = ShadowBall()
class SkyUppercut(PokeMoves):
	def __init__(self):
		move_name = "Sky Uppercut"
		abil_type = 'fight'
		power = 85
		acc = 90
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

skyuppercut = SkyUppercut()
class Slash(PokeMoves):
	def __init__(self):
		move_name = "Slash"
		abil_type = 'normal'
		power = 70
		acc = 100
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

slash = Slash()
class SleepPowder(PokeMoves):
	def __init__(self):
		move_name = "Sleep Powder"
		abil_type = 'grass'
		power = 0
		acc = 75
		effect = ['sleep']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

sleeppowder = SleepPowder()
class SludgeBomb(PokeMoves):
	def __init__(self):
		move_name = "Sludge Bomb"
		abil_type = 'poison'
		power = 90
		acc = 100
		effect = ['poison']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

sludgebomb = SludgeBomb()
class Surf(PokeMoves):
	def __init__(self):
		move_name = "Surf"
		abil_type = 'water'
		power = 95
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

surf = Surf()
class TakeDown(PokeMoves):
	def __init__(self):
		move_name = "Take Down"
		abil_type = 'normal'
		power = 90
		acc = 85
		effect = ['recoil_25']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

takedown = TakeDown()
class Thunder(PokeMoves):
	def __init__(self):
		move_name = "Thunder"
		abil_type = 'electric'
		power = 120
		acc = 70
		effect = ['paralyze']
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

thunder = Thunder()
class WingAttack(PokeMoves):
	def __init__(self):
		move_name = "Wing Attack"
		abil_type = 'flying'
		power = 60
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

wingattack = WingAttack()
class Yawn(PokeMoves):
	def __init__(self):
		move_name = "Yawn"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = ['yawn']
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, move_name, abil_type, power, acc, effect, effect_chance, crit)
	

yawn = Yawn()