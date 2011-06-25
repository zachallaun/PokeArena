class Effect(object):
	def __init__(self, effect_dict):
		self.effect_dict = effect_dict
	

	
class Burn(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 'perm',
			'status': 'BRN',
			'printed': '%s has been burned!',
			'effect_dmg': 25
		}
		Effect.__init__(self, effect_dict)
	

burn = Burn()
class FireSpinEffect(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': '4',
			'status': 'FRS',
			'printed': '%s has been caught in Fire Spin!',
			'effect_dmg': 30
		}
		Effect.__init__(self, effect_dict)
	

fire_spin_effect = FireSpinEffect()
class Flinch(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 0,
			'printed': '%s flinched!',
		}
		Effect.__init__(self, effect_dict)
	

flinch = Flinch()
class Freeze(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'enemy',
			'duration': 5,
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
			'status': 'PSN',
			'printed': '%s has been poisoned!',
			'effect_dmg': 25
		}
		Effect.__init__(self, effect_dict)
	

poison = Poison()
class Recharge(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'duration': 1,
			'status': 'RCH',
			'printed': '%s must recharge!',
		}
		Effect.__init__(self, effect_dict)
	

recharge = Recharge()
class Recoil(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'duration': 0,
			'printed': '%s is hit with recoil!',
			'effect_dmg': 30
		}
		Effect.__init__(self, effect_dict)
	

recoil = Recoil()
class RecoverEffect(Effect):
	def __init__(self):
		effect_dict = {
			'target': 'self',
			'duration': 0,
			'printed': '%s gains health with Recover!',
			'effect_heal': 150
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
			'duration': 0,
			'printed': '%s is healed by %s!',
			'effect_heal': 50
		}
		Effect.__init__(self, effect_dict)
	

user_hp_50 = UserHealHalf()