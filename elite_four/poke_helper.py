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
Please pick an ally and an enemy from
the following list:"""
		print space
	print_poke()
	print space
	if picka:
		ally_chosen = False
		while ally_chosen == False:
			ally = raw_input("Enter a valid Pokemon to command: ").lower().capitalize()
			if ally in poke_list:
				ally = eval(ally)
				ally = ally()
				ally.initialize()
				ally_chosen = True
			else:
				print "You can't choose that!"
				print space
	if picke:
		enemy_chosen = False
		while enemy_chosen == False:	
			enemy = raw_input("Enter a valid Pokemon to battle: ").lower().capitalize()
			if enemy in poke_list:
				enemy = eval(enemy)
				enemy = enemy()
				enemy.initialize()
				enemy_chosen = True
			else:
				print "You can't choose that!"
				print space
	print space
	print "Good luck!"
	print space
	print "You send out %s!" % ally.name
	print "Foe sends out %s!" % enemy.name
	battle(ally, enemy)


def print_poke():
	for i in range(0,3):
		print poke_list[i].ljust(12),
	print poke_list[3].ljust(12)
	for i in range(4,7):
		print poke_list[i].ljust(12),
	print poke_list[7].ljust(12)
	for i in range(8,11):
		print poke_list[i].ljust(12),
	print poke_list[11].ljust(12)
	for i in range(12,15):
		print poke_list[i].ljust(12),
	print poke_list[15].ljust(12)

def battle(ally, enemy, retry = False):
	ally.type = 'usr'
	enemy.type = 'ai'
	while ally.hp > 0 and enemy.hp > 0:
		print space
		print_hp(ally, enemy)
		print space
		if retry:
			print "%s doesn't know what to do!" % ally.name
		print "What will %s do?" % ally.name
		print ally.moves['move1'].name.ljust(20), ally.moves['move2'].name.ljust(20), "\n", ally.moves['move3'].name.ljust(20), ally.moves['move4'].name.ljust(20)
			
		move = raw_input(">>> ").lower()
		enemy_move = 'move%d' % randint(1, 4)
		
		for i in range(1,5):
			if ally.moves['move%d' % i].name.lower().startswith(move):				
				print space
				move = 'move%d' % i
				break
		else:
			battle(ally, enemy, retry = True)
		
		ally.hit = 0
		enemy.hit = 0
		
		if ally.speed > enemy.speed:
			status_beg_of(ally, enemy, move, enemy_move)
		else:
			status_beg_of(enemy, ally, enemy_move, move)
		
		ally.flinch = 0
		enemy.flinch = 0


def attack_target(attacker, target, move):
	if attacker.flinch == 0 and attacker.recharge != 1:
		print "%s uses %s!" % (attacker.name, attacker.moves[move].name)
		attacker.attack(target, move)
			
		if attacker.moves[move].effect != None:
			attacker.pass_effect(attacker, target, move)	
	elif attacker.recharge == 1:
		print "%s has to recharge!" % attacker.name
		attacker.recharge = 0


def check_faint(first, second):
	if first.type == 'usr':
		ally = first
		enemy = second
	else:
		ally = second
		enemy = first
	
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


def status_end_of(first, second):
	checklist = [first, second]
	for obj in checklist:
		if obj.status in end_of:
			end_status = random()
			if end_status < .25:
				print "%s faded from %s..." % (obj.status['status'], obj.name)
				obj.status = None
			else:
				obj.hp = obj.hp - obj.status['effect_pwr']
				print space
				print obj.status['report'] % obj.name


def status_beg_of(first, second, firstmove, secondmove):
	checklist = [first, second]
	for obj in checklist:
		if obj.status in beg_of:
			end_status = random()
			if end_status < .25:
				print "%s faded from %s..." % (obj.status['status'], obj.name)
				obj.status = None
				obj.move = 1
		if obj.status in beg_of:
			print "%s can't move!" % obj.name
			print space
			obj.move = 0
	if first.move == 1:
		attack_target(first, second, firstmove)
		check_faint(first, second)
		print space
	if second.move == 1:
		attack_target(second, first, secondmove)
		check_faint(first, second)
	status_end_of(first, second)


def display_hp(obj):
	remaining = '='*int(obj.hp/obj.hpinc)
	missing = ''
	if obj.hp < obj.maxhp:
		missing = '-'+'-'*int((obj.maxhp-obj.hp)/obj.hpinc)
	bar_form = "[%s%s]" % (remaining, missing)
	
	return bar_form


def print_hp(ally, enemy):
	if ally.status != None and enemy.status != None:
		print "Ally: %s %s %s" % (ally.name.ljust(14), display_hp(ally), ally.status['status'])
		print "%s %s %s" % (enemy.name.ljust(20), display_hp(enemy), enemy.status['status'])	
	elif ally.status != None and enemy.status == None:
		print "Ally: %s %s %s" % (ally.name.ljust(14), display_hp(ally), ally.status['status'])
		print "%s %s" % (enemy.name.ljust(20), display_hp(enemy))
	elif enemy.status != None and ally.status == None:
		print "Ally: %s %s" % (ally.name.ljust(14), display_hp(ally))
		print "%s %s %s" % (enemy.name.ljust(20), display_hp(enemy), enemy.status['status'])
	else:
		print "Ally: %s %s" % (ally.name.ljust(14), display_hp(ally))
		print "%s %s" % (enemy.name.ljust(20), display_hp(enemy))
