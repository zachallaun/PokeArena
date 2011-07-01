from poke_effects import *

class PokeMoves(object):
	
	def __init__(self, name, abil_type, power, acc, effect, effect_chance, crit):
		self.name = name
		self.abil_type = abil_type
		self.power = power
		self.acc = acc
		self.effect = effect
		self.effect_chance = effect_chance
		self.crit = crit
	
	


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
	

aerialace = AerialAce()
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

aircutter = AirCutter()
class AncientPower(PokeMoves):
	def __init__(self):
		name = "Ancient Power"
		abil_type = 'rock'
		power = 60
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

ancientpower = AncientPower()
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
	

aquatail = AquaTail()
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
	

aurasphere = AuraSphere()
class Bite(PokeMoves):
	def __init__(self):
		name = "Bite"
		abil_type = 'dark'
		power = 65
		acc = 100
		effect = flinch
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

bite = Bite()
class BodySlam(PokeMoves):
	def __init__(self):
		name = "Body Slam"
		abil_type = 'normal'
		power = 85
		acc = 100
		effect = paralyze
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

bodyslam = BodySlam()
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
	

brickbreak = BrickBreak()
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
	

crosschop = CrossChop()
class DarkPulse(PokeMoves):
	def __init__(self):
		name = "Dark Pulse"
		abil_type = 'dark'
		power = 80
		acc = 100
		effect = flinch
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

darkpulse = DarkPulse()
class DragonRush(PokeMoves):
	def __init__(self):
		name = "Dragon Rush"
		abil_type = 'dragon'
		power = 75
		acc = 100
		effect = flinch
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

dragonrush = DragonRush()
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
	

earthquake = Earthquake()
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
	

eggbomb = EggBomb()
class EnergyBall(PokeMoves):
	def __init__(self):
		name = "Energy Ball"
		abil_type = 'grass'
		power = 80
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

energyball = EnergyBall()
class FirePunch(PokeMoves):
	def __init__(self):
		name = "Fire Punch"
		abil_type = 'fire'
		power = 75
		acc = 100
		effect = burn
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

firepunch = FirePunch()
class FireSpin(PokeMoves):
	def __init__(self):
		name = "Fire Spin"
		abil_type = 'fire'
		power = 30
		acc = 100
		effect = fire_spin_effect
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

firespin = FireSpin()
class Flamethrower(PokeMoves):
	def __init__(self):
		name = "Flamethrower"
		abil_type = 'fire'
		power = 95
		acc = 100
		effect = burn
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

flamethrower = Flamethrower()
class FlareBlitz(PokeMoves):
	def __init__(self):
		name = "Flare Blitz"
		abil_type = 'fire'
		power = 120
		acc = 100
		effect = recoil
		effect_chance = 100
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

flareblitz = FlareBlitz()
class GigaDrain(PokeMoves):
	def __init__(self):
		name = "Giga Drain"
		abil_type = 'grass'
		power = 75
		acc = 100
		effect = user_hp_50
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

gigadrain = GigaDrain()
class GigaImpact(PokeMoves):
	def __init__(self):
		name = "Giga Impact"
		abil_type = 'normal'
		power = 150
		acc = 90
		effect = recharge
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

gigaimpact = GigaImpact()
class GunkShot(PokeMoves):
	def __init__(self):
		name = "Gunk Shot"
		abil_type = 'poison'
		power = 120
		acc = 70
		effect = poison
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

gunkshot = GunkShot()
class HyperBeam(PokeMoves):
	def __init__(self):
		name = "Hyper Beam"
		abil_type = 'normal'
		power = 150
		acc = 90
		effect = recharge
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

hyperbeam = HyperBeam()
class IceBeam(PokeMoves):
	def __init__(self):
		name = "Ice Beam"
		abil_type = 'ice'
		power = 95
		acc = 100
		effect = freeze
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

icebeam = IceBeam()
class IronTail(PokeMoves):
	def __init__(self):
		name = "Iron Tail"
		abil_type = 'steel'
		power = 100
		acc = 75
		effect = None
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

irontail = IronTail()
class LeafStorm(PokeMoves):
	def __init__(self):
		name = "Leaf Storm"
		abil_type = 'grass'
		power = 120
		acc = 90
		effect = recoil
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

leafstorm = LeafStorm()
class Lick(PokeMoves):
	def __init__(self):
		name = "Lick"
		abil_type = 'ghost'
		power = 50
		acc = 100
		effect = paralyze
		effect_chance = 50
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

lick = Lick()
class MachPunch(PokeMoves):
	def __init__(self):
		name = "Mach Punch"
		abil_type = 'fight'
		power = 80
		acc = 100
		effect = None
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

machpunch = MachPunch()
class PoisonFang(PokeMoves):
	def __init__(self):
		name = "Poison Fang"
		abil_type = 'poison'
		power = 50
		acc = 100
		effect = poison
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

poisonfang = PoisonFang()
class PoisonJab(PokeMoves):
	def __init__(self):
		name = "Poison Jab"
		abil_type = 'poison'
		power = 80
		acc = 100
		effect = poison
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

poisonjab = PoisonJab()
class Psychic(PokeMoves):
	def __init__(self):
		name = "Psychic"
		abil_type = 'psychic'
		power = 90
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

psychic = Psychic()
class Psyshock(PokeMoves):
	def __init__(self):
		name = "Psyshock"
		abil_type = 'psychic'
		power = 80
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

psyshock = Psyshock()
class Recover(PokeMoves):
	def __init__(self):
		name = "Recover"
		abil_type = 'normal'
		power = 0
		acc = 100
		effect = recover_effect
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

recover = Recover()
class RockTomb(PokeMoves):
	def __init__(self):
		name = "Rock Tomb"
		abil_type = 'rock'
		power = 80	
		acc = 95
		effect = None
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

rocktomb = RockTomb()
class ShadowBall(PokeMoves):
	def __init__(self):
		name = "Shadow Ball"
		abil_type = 'ghost'
		power = 80
		acc = 100
		effect = None
		effect_chance = 20
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

shadowball = ShadowBall()
class SheerCold(PokeMoves):
	def __init__(self):
		name = 'Sheer Cold'
		abil_type = 'ice'
		power = 0
		acc = 100
		effect = sheer_cold_effect
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

sheercold = SheerCold()
class SignalBeam(PokeMoves):
	def __init__(self):
		name = 'Signal Beam'
		abil_type = 'bug'
		power = 80
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

signalbeam = SignalBeam()
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
	

skyuppercut = SkyUppercut()
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
	

slash = Slash()
class SludgeBomb(PokeMoves):
	def __init__(self):
		name = "Sludge Bomb"
		abil_type = 'poison'
		power = 90
		acc = 100
		effect = poison
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

sludgebomb = SludgeBomb()
class StoneEdge(PokeMoves):
	def __init__(self):
		name = "Stone Edge"
		abil_type = 'rock'
		power = 100
		acc = 80
		effect = None
		effect_chance = 0
		crit = 'yes'
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

stoneedge = StoneEdge()
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
	

surf = Surf()
class TakeDown(PokeMoves):
	def __init__(self):
		name = "Take Down"
		abil_type = 'normal'
		power = 95
		acc = 90
		effect = recoil
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

takedown = TakeDown()
class Thunder(PokeMoves):
	def __init__(self):
		name = "Thunder"
		abil_type = 'electric'
		power = 120
		acc = 70
		effect = paralyze
		effect_chance = 30
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

thunder = Thunder()
class ThunderBolt(PokeMoves):
	def __init__(self):
		name = "Thunder Bolt"
		abil_type = 'electric'
		power = 95
		acc = 100
		effect = paralyze
		effect_chance = 10
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

thunderbolt = ThunderBolt()
class ThunderWave(PokeMoves):
	def __init__(self):
		name = "Thunder Wave"
		abil_type = 'electric'
		power = 0
		acc = 100
		effect = paralyze
		effect_chance = 100
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

thunderwave = ThunderWave()
class Toxic(PokeMoves):
	def __init__(self):
		name = "Toxic"
		abil_type = 'poison'
		power = 0
		acc = 100
		effect = poison
		effect_chance = 90
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

toxic = Toxic()
class WingAttack(PokeMoves):
	def __init__(self):
		name = "Wing Attack"
		abil_type = 'flying'
		power = 75
		acc = 100
		effect = None
		effect_chance = 0
		crit = None
		PokeMoves.__init__(self, name, abil_type, power, acc, effect, effect_chance, crit)
	

wingattack = WingAttack()