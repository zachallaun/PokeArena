from poke_effects import *

class PokeMoves(object):
	
	def __init__(self, name, abil_type, power, acc, effect = None, effect_chance = 0, crit = None):
		self.name = name
		self.abil_type = abil_type
		self.power = power
		self.acc = acc
		self.effect = effect
		self.effect_chance = effect_chance
		self.crit = crit
	
	


class AerialAce(PokeMoves):
	
	def __init__(self):
		attrs = {
		'name': "Aerial Ace",
		'abil_type': 'flying',
		'power': 65,
		'acc': 100,
		}
		super(AerialAce, self).__init__(**attrs)
	

aerialace = AerialAce()
class AirCutter(PokeMoves):
	
	def __init__(self):
		attrs = {
		'name': "Air Cutter",
		'abil_type': 'flying',
		'power': 55,
		'acc': 95,
		'crit': 'yes'
		}
		super(AirCutter, self).__init__(**attrs)

aircutter = AirCutter()
class AncientPower(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Ancient Power",
		'abil_type': 'rock',
		'power': 60,
		'acc': 100,
		}
		super(AncientPower, self).__init__(**attrs)
	

ancientpower = AncientPower()
class AquaTail(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Aqua Tail",
		'abil_type': 'water',
		'power': 90,
		'acc': 90,
		}
		super(AquaTail, self).__init__(**attrs)
	

aquatail = AquaTail()
class AuraSphere(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Aura Sphere",
		'abil_type': 'fight',
		'power': 90,
		'acc': 100,
		}
		super(AuraSphere, self).__init__(**attrs)
	

aurasphere = AuraSphere()
class Bite(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Bite",
		'abil_type': 'dark',
		'power': 65,
		'acc': 100,
		'effect': flinch,
		'effect_chance': 30,
		}
		super(Bite, self).__init__(**attrs)
	

bite = Bite()
class BodySlam(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Body Slam",
		'abil_type': 'normal',
		'power': 85,
		'acc': 100,
		'effect': paralyze,
		'effect_chance': 30,
		}
		super(BodySlam, self).__init__(**attrs)
	

bodyslam = BodySlam()
class BrickBreak(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Brick Break",
		'abil_type': 'fight',
		'power': 75,
		'acc': 100,
		}
		super(BrickBreak, self).__init__(**attrs)
	

brickbreak = BrickBreak()
class CrossChop(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Cross Chop",
		'abil_type': 'fight',
		'power': 100,
		'acc': 80,
		'crit': 'yes'
		}
		super(CrossChop, self).__init__(**attrs)
	

crosschop = CrossChop()
class DarkPulse(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Dark Pulse",
		'abil_type': 'dark',
		'power': 80,
		'acc': 100,
		'effect': flinch,
		'effect_chance': 20
		}
		super(DarkPulse, self).__init__(**attrs)
	

darkpulse = DarkPulse()
class DragonRush(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Dragon Rush",
		'abil_type': 'dragon',
		'power': 75,
		'acc': 100,
		'effect': flinch,
		'effect_chance': 20
		}
		super(DragonRush, self).__init__(**attrs)
	

dragonrush = DragonRush()
class Earthquake(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Earthquake",
		'abil_type': 'ground',
		'power': 100,
		'acc': 100,
		}
		super(Earthquake, self).__init__(**attrs)
	

earthquake = Earthquake()
class EggBomb(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Egg Bomb",
		'abil_type': 'normal',
		'power': 100,
		'acc': 75,
		}
		super(EggBomb, self).__init__(**attrs)
	

eggbomb = EggBomb()
class EnergyBall(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Energy Ball",
		'abil_type': 'grass',
		'power': 80,
		'acc': 100,
		}
		super(EnergyBall, self).__init__(**attrs)
	

energyball = EnergyBall()
class FirePunch(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Fire Punch",
		'abil_type': 'fire',
		'power': 75,
		'acc': 100,
		'effect': burn,
		'effect_chance': 10,
		}
		super(FirePunch, self).__init__(**attrs)
	

firepunch = FirePunch()
class FireSpin(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Fire Spin",
		'abil_type': 'fire',
		'power': 30,
		'acc': 100,
		'effect': fire_spin_effect,
		'effect_chance': 100,
		}
		super(FireSpin, self).__init__(**attrs)
	

firespin = FireSpin()
class Flamethrower(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Flamethrower",
		'abil_type': 'fire',
		'power': 95,
		'acc': 100,
		'effect': burn,
		'effect_chance': 10,
		}
		super(Flamethrower, self).__init__(**attrs)
	

flamethrower = Flamethrower()
class FlareBlitz(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Flare Blitz",
		'abil_type': 'fire',
		'power': 120,
		'acc': 100,
		'effect': recoil,
		'effect_chance': 100,
		'crit': 'yes'
		}
		super(FlareBlitz, self).__init__(**attrs)
	

flareblitz = FlareBlitz()
class GigaDrain(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Giga Drain",
		'abil_type': 'grass',
		'power': 75,
		'acc': 100,
		'effect': user_hp_50,
		'effect_chance': 100,
		}
		super(GigaDrain, self).__init__(**attrs)
	

gigadrain = GigaDrain()
class GigaImpact(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Giga Impact",
		'abil_type': 'normal',
		'power': 150,
		'acc': 90,
		'effect': recharge,
		'effect_chance': 100,
		}
		super(GigaImpact, self).__init__(**attrs)
	

gigaimpact = GigaImpact()
class GunkShot(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Gunk Shot",
		'abil_type': 'poison',
		'power': 120,
		'acc': 70,
		'effect': poison,
		'effect_chance': 30,
		}
		super(GunkShot, self).__init__(**attrs)
	

gunkshot = GunkShot()
class HyperBeam(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Hyper Beam",
		'abil_type': 'normal',
		'power': 150,
		'acc': 90,
		'effect': recharge,
		'effect_chance': 100,
		}
		super(HyperBeam, self).__init__(**attrs)
	

hyperbeam = HyperBeam()
class IceBeam(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Ice Beam",
		'abil_type': 'ice',
		'power': 95,
		'acc': 100,
		'effect': freeze,
		'effect_chance': 10,
		}
		super(IceBeam, self).__init__(**attrs)
	

icebeam = IceBeam()
class IronTail(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Iron Tail",
		'abil_type': 'steel',
		'power': 100,
		'acc': 75,
		}
		super(IronTail, self).__init__(**attrs)
	

irontail = IronTail()
class LeafStorm(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Leaf Storm",
		'abil_type': 'grass',
		'power': 120,
		'acc': 90,
		'effect': recoil,
		'effect_chance': 100,
		}
		super(LeafStorm, self).__init__(**attrs)
	

leafstorm = LeafStorm()
class Lick(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Lick",
		'abil_type': 'ghost',
		'power': 50,
		'acc': 100,
		'effect': paralyze,
		'effect_chance': 50,
		}
		super(Lick, self).__init__(**attrs)
	

lick = Lick()
class MachPunch(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Mach Punch",
		'abil_type': 'fight',
		'power': 80,
		'acc': 100,
		}
		super(MachPunch, self).__init__(**attrs)
	

machpunch = MachPunch()
class PoisonFang(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Poison Fang",
		'abil_type': 'poison',
		'power': 50,
		'acc': 100,
		'effect': poison,
		'effect_chance': 30,
		}
		super(PoisonFang, self).__init__(**attrs)
	

poisonfang = PoisonFang()
class PoisonJab(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Poison Jab",
		'abil_type': 'poison',
		'power': 80,
		'acc': 100,
		'effect': poison,
		'effect_chance': 10,
		}
		super(PoisonJab, self).__init__(**attrs)
	

poisonjab = PoisonJab()
class Psychic(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Psychic",
		'abil_type': 'psychic',
		'power': 90,
		'acc': 100,
		}
		super(Psychic, self).__init__(**attrs)
	

psychic = Psychic()
class Psyshock(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Psyshock",
		'abil_type': 'psychic',
		'power': 80,
		'acc': 100,
		}
		super(Psyshock, self).__init__(**attrs)
	

psyshock = Psyshock()
class Recover(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Recover",
		'abil_type': 'normal',
		'power': 0,
		'acc': 100,
		'effect': recover_effect,
		'effect_chance': 100,
		}
		super(Recover, self).__init__(**attrs)
	

recover = Recover()
class RockTomb(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Rock Tomb",
		'abil_type': 'rock',
		'power': 80,
		'acc': 95,
		}
		super(RockTomb, self).__init__(**attrs)
	

rocktomb = RockTomb()
class ShadowBall(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Shadow Ball",
		'abil_type': 'ghost',
		'power': 80,
		'acc': 100,
		}
		super(ShadowBall, self).__init__(**attrs)
	

shadowball = ShadowBall()
class SheerCold(PokeMoves):
	def __init__(self):
		attrs = {
		'name': 'Sheer Cold',
		'abil_type': 'ice',
		'power': 0,
		'acc': 100,
		'effect': sheer_cold_effect,
		'effect_chance': 30,
		}
		super(SheerCold, self).__init__(**attrs)
	

sheercold = SheerCold()
class SignalBeam(PokeMoves):
	def __init__(self):
		attrs = {
		'name': 'Signal Beam',
		'abil_type': 'bug',
		'power': 80,
		'acc': 100,
		}
		super(SignalBeam, self).__init__(**attrs)
	

signalbeam = SignalBeam()
class SkyUppercut(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Sky Uppercut",
		'abil_type': 'fight',
		'power': 85,
		'acc': 90,
		}
		super(SkyUppercut, self).__init__(**attrs)
	

skyuppercut = SkyUppercut()
class Slash(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Slash",
		'abil_type': 'normal',
		'power': 70,
		'acc': 100,
		'crit': 'yes'
		}
		super(Slash, self).__init__(**attrs)
	

slash = Slash()
class SludgeBomb(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Sludge Bomb",
		'abil_type': 'poison',
		'power': 90,
		'acc': 100,
		'effect': poison,
		'effect_chance': 30,
		}
		super(SludgeBomb, self).__init__(**attrs)
	

sludgebomb = SludgeBomb()
class StoneEdge(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Stone Edge",
		'abil_type': 'rock',
		'power': 100,
		'acc': 80,
		'crit': 'yes'
		}
		super(StoneEdge, self).__init__(**attrs)
	

stoneedge = StoneEdge()
class Surf(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Surf",
		'abil_type': 'water',
		'power': 95,
		'acc': 100,
		}
		super(Surf, self).__init__(**attrs)
	

surf = Surf()
class TakeDown(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Take Down",
		'abil_type': 'normal',
		'power': 95,
		'acc': 90,
		'effect': recoil,
		'effect_chance': 100,
		}
		super(TakeDown, self).__init__(**attrs)
	

takedown = TakeDown()
class Thunder(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Thunder",
		'abil_type': 'electric',
		'power': 120,
		'acc': 70,
		'effect': paralyze,
		'effect_chance': 30,
		}
		super(Thunder, self).__init__(**attrs)
	

thunder = Thunder()
class ThunderBolt(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Thunder Bolt",
		'abil_type': 'electric',
		'power': 95,
		'acc': 100,
		'effect': paralyze,
		'effect_chance': 10,
		}
		super(ThunderBolt, self).__init__(**attrs)
	

thunderbolt = ThunderBolt()
class ThunderWave(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Thunder Wave",
		'abil_type': 'electric',
		'power': 0,
		'acc': 100,
		'effect': paralyze,
		'effect_chance': 100,
		}
		super(ThunderWave, self).__init__(**attrs)
	

thunderwave = ThunderWave()
class Toxic(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Toxic",
		'abil_type': 'poison',
		'power': 0,
		'acc': 100,
		'effect': poison,
		'effect_chance': 90,
		}
		super(Toxic, self).__init__(**attrs)
	

toxic = Toxic()
class WingAttack(PokeMoves):
	def __init__(self):
		attrs = {
		'name': "Wing Attack",
		'abil_type': 'flying',
		'power': 75,
		'acc': 100,
		}
		super(WingAttack, self).__init__(**attrs)
	

wingattack = WingAttack()