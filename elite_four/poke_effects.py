import poke_dict

BRN = {
	'status':'BRN',
	'report':'%s is hurt by burn!',
	'effect_pwr': 25,
}

PSN = {
	'status':'PSN',
	'report':'%s is hurt by poison!',
	'effect_pwr': 25,
}

FS = {
	'status':'FS',
	'report':'%s is hurt in the Fire Spin!',
	'effect_pwr':30,
}

class Effect(object):
	def __init__(self, effect_dict):
		self.effect_dict = effect_dict
	

	
class Burn(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': BRN,
			'printed': '%s has been burned!'
		}
		Effect.__init__(self, effect_dict)
	

burn = Burn()
class FireSpinEffect(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': FS,
			'printed': '%s has been caught in Fire Spin!'
		}
		Effect.__init__(self, effect_dict)
	

fire_spin_effect = FireSpinEffect()
class Flinch(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'printed': '%s flinched!',
		}
		Effect.__init__(self, effect_dict)
	

flinch = Flinch()
class Freeze(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': 'FRZ',
			'printed': '%s has been frozen!',
		}
		Effect.__init__(self, effect_dict)
	

freeze = Freeze()
class Paralyze(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': 'PAR',
			'printed': '%s has been paralyzed! It may be unable to move!',
		}
		Effect.__init__(self, effect_dict)
	

paralyze = Paralyze()
class Poison(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': PSN,
			'printed': '%s has been poisoned!'
		}
		Effect.__init__(self, effect_dict)
	

poison = Poison()
class Recharge(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'status': 'RCH',
			'printed': '%s must recharge!',
		}
		Effect.__init__(self, effect_dict)
	

recharge = Recharge()
class Recoil(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'printed': '%s is hit with recoil!',
			'effect_pwr': -30
		}
		Effect.__init__(self, effect_dict)
	

recoil = Recoil()
class RecoverEffect(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'printed': '%s gains health with Recover!',
			'effect_pwr': 150
		}
		Effect.__init__(self, effect_dict)
	

recover_effect = RecoverEffect()
class SheerColdEffect(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': 'FNT',
			'printed': '%s was hit by Sheer Cold! It\'s a one-hit KO!',
		}
		Effect.__init__(self, effect_dict)
	

sheer_cold_effect = SheerColdEffect()
class UserHealHalf(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'printed': '%s restores some HP!',
			'effect_pwr': 50
		}
		Effect.__init__(self, effect_dict)
	

user_hp_50 = UserHealHalf()