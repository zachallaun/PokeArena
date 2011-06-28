from poke_dict import *
from sys import exit

space = "\t--------------------"
next = "\tPress <Enter> to continue."

def start():
	print """\tHello. Welcome to the PokeArena.
\tSoon, you will pick a Pokemon to command, and
\tan enemy to fight."""
	print space
	ally = input("\tEnter a valid Pokemon to command: ")
	enemy = input("\tEnter a valid Pokemon to battle: ")
	ally = ally()
	enemy = enemy()
	print space
	print "\tYou have chosen %s to fight %s." % (ally.name, enemy.name)
	print "\tGood luck!"
	print space
	raw_input(next)
	battle(ally, enemy)


def battle(ally, enemy):
	print space
	print "\tYou send out %s!" % ally.name
	print "\tFoe sends out %s!" % enemy.name
	
	while ally.hp > 0 and enemy.hp > 0:
		print space
		print "\t%s HP: %d" % (ally.name, ally.hp)
		print "\t%s HP: %d" % (enemy.name, enemy.hp)
		print space
		print "\tWhat will %s do?" % ally.name
		print "\t\t", ally.moves['move1'].name
		print "\t\t", ally.moves['move2'].name
		print "\t\t", ally.moves['move3'].name
		print "\t\t", ally.moves['move4'].name
		move = raw_input("\t>>> ")
		print space
		
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
	print "\t%s uses %s!" % (ally.name, move)
	if move == ally.moves['move1'].name:
		ally.attack(enemy, 'move1')
		
		if ally.moves['move1'].effect != None and ally.moves['move1'].effect.effect_dict['target'] == 'self':
			ally.pass_effect(
				ally, 
				ally.moves['move1'].effect,
				ally.moves['move1'].effect_chance
			)
			
	elif move == ally.moves['move2'].name:
		ally.attack(enemy, 'move2')
		
		if ally.moves['move2'].effect != None and ally.moves['move1'].effect.effect_dict['target'] == 'self':
			ally.pass_effect(
				ally, 
				ally.moves['move2'].effect,
				ally.moves['move2'].effect_chance
			)
		
	elif move == ally.moves['move3'].name:
		ally.attack(enemy, 'move3')
		
		if ally.moves['move3'].effect != None and ally.moves['move1'].effect.effect_dict['target'] == 'self':
			ally.pass_effect(
				ally, 
				ally.moves['move3'].effect,
				ally.moves['move3'].effect_chance
			)
		
	elif move == ally.moves['move4'].name:
		ally.attack(enemy, 'move4')
		
		if ally.moves['move4'].effect != None and ally.moves['move1'].effect.effect_dict['target'] == 'self':
			ally.pass_effect(
				ally, 
				ally.moves['move4'].effect,
				ally.moves['move4'].effect_chance
			)
		
	else:
		print "\tNot sure what you mean. Be more careful typing."


def enemy_attack(ally, enemy):
	enemy_move = 'move%d' % randint(1, 4)
	print "\t%s uses %s!" % (enemy.name, enemy.moves[enemy_move].name)
	enemy.attack(ally, enemy_move)


def check_faint(ally, enemy):
	if ally.hp <= 0:
		print space
		print "\t%s fainted!" % ally.name
		exit(1)
	elif enemy.hp <= 0:
		print space
		print "\t%s fainted!" % enemy.name
		exit(1)


start()