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
	

