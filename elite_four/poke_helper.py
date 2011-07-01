from poke_dict import *

space = '-'*18

def start(intro = True, picka = True, picke = True, ally = None, enemy = None):
	"""A simple boolean handler for initiating the PokeArena.
	
	Boolean keyword arguments will determine which elements
of the handler are used. Keyword arguments for ally and enemy
are provided so that their respective objects can be passed,
retaining all attribute modifications that may have occurred."""
	
	print space
	if intro:
		print """Hello, and welcome to the PokeArena.
Please pick an ally and an enemy."""
		print space
	if picka:
		ally = input("Enter a valid Pokemon to command: ")
		ally = ally()
		ally.initialize()
	if picke:	
		enemy = input("Enter a valid Pokemon to battle: ")
		enemy = enemy()
		enemy.initialize()
	print space
	print "Good luck!"
	print space
	print "You send out %s!" % ally.name
	print "Foe sends out %s!" % enemy.name
	battle(ally, enemy)


def battle(ally, enemy, retry = False):
	
	while ally.hp > 0 and enemy.hp > 0:
		print space
		print "%s %s" % (ally.name.ljust(15), display_hp(ally))
		print "%s %s" % (enemy.name.ljust(15), display_hp(enemy))
		print space
		if retry:
			print "%s doesn't know what to do!" % ally.name
		print "What will %s do?" % ally.name
		print ally.moves['move1'].name.ljust(20), ally.moves['move2'].name.ljust(20), "\n", ally.moves['move3'].name.ljust(20), ally.moves['move4'].name.ljust(20)
			
		move = raw_input(">>> ").lower()
		
		for i in range(1,5):
			if ally.moves['move%d' % i].name.lower().startswith(move):				
				print space
				move = 'move%d' % i
				break
		else:
			battle(ally, enemy, retry = True)
		
		if ally.speed > enemy.speed:
			ally_attack(ally, enemy, move)
			check_faint(ally, enemy)
			print space
			enemy_attack(ally, enemy)
			check_faint(ally, enemy)
		else:
			enemy_attack(ally, enemy)
			check_faint(ally, enemy)
			print space
			ally_attack(ally, enemy, move)
			check_faint(ally, enemy)


def ally_attack(ally, enemy, move):
	print "%s uses %s!" % (ally.name, ally.moves[move].name)
	ally.attack(enemy, move)
			
	if ally.moves[move].effect != None:
		ally.pass_effect(ally, enemy, move)	


def enemy_attack(ally, enemy):
	enemy_move = 'move%d' % randint(1, 4)
	print "%s uses %s!" % (enemy.name, enemy.moves[enemy_move].name)
	enemy.attack(ally, enemy_move)
	
	if enemy.moves[enemy_move].effect != None:
		enemy.pass_effect(enemy, ally, enemy_move)


def check_faint(ally, enemy):
	if ally.hp <= 0:
		print space
		print "%s fainted!" % ally.name
		print "Pick a new ally!"
		start(intro = False, picke = False, enemy = enemy)
	elif enemy.hp <= 0:
		print space
		print "%s fainted!" % enemy.name
		print "Pick a new enemy!"
		start(intro = False, picka = False, ally = ally)


def display_hp(obj):
	remaining = '='*int(obj.hp/obj.hpinc)
	missing = ''
	if obj.hp < obj.maxhp:
		missing = '-'+'-'*int((obj.maxhp-obj.hp)/obj.hpinc)
	bar_form = "[%s%s]" % (remaining, missing)
	
	return bar_form


def status_end(ally, enemy):
	if ally.status == 