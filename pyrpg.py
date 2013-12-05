import random

class Entity:
	def __init__(self, type):
		self.type = type

class Creature(Entity):
	type = "Creature"

	def __init__(self, name, hitpoints, power):
		self.name = name
		self.maxHP = hitpoints
		self.currHP = hitpoints
		self.power = power

	def attack(self, target):
		damage = self.power * random.randrange(0, 21) / 10.0
		target.currHP = target.currHP - damage if target.currHP - damage >= 0 else 0
		print "%s hit %s for %d damage." % (self.name, target.name, damage)

	def toString(self):
		return "%s: %d/%d" % (self.name, self.currHP, self.maxHP)

class Structure(Entity):
	type = "Structure"

	def __init__(self, name, hitpoints):
		self.name = name
		self.maxHP = hitpoints
		self.currHP = hitpoints

	def toString(self):
		return "%s: %d/%d" % (self.name, self.currHP, self.maxHP)

class Spell(Entity):
	type = "Spell"

	def __init__(self, name):
		self.name = name

def battle(a, b):
	if random.randrange(0, 2):
		order = [a, b]
	else:
		order = [b, a]

	while a.currHP > 0 and b.currHP > 0:
		if order[0].type != "Structure":
			order[0].attack(order[1])

		print a.toString() + "\t" + b.toString()

		if order[1].currHP > 0:
			order = order[::-1]
		else:
			print order[1].name + " is dead!"

guard = Creature("Guard", 200, 20)
orc = Creature("Orc", 200, 20)
wall = Structure("Wall", 2000)

battle(guard, orc)