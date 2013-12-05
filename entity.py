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

		if damage > self.power * 1.25:
			status = "Critical hit! "
		elif damage < self.power * .25:
			status = "Glancing blow! "
		else:
			status = ""

		print "%s%s hit %s for %d damage." % (status, self.name, target.name, damage)

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

	def __init__(self, name, power, cost):
		self.name = name
		self.power = power
		self.cost = cost

	def cast(self, target):
		damage = self.power
		target.currHP = target.currHP - damage if target.currHP - damage >= 0 else 0

		print "%s was struck by %s for %d damage." % (target.name, self.name, damage)

	def toString(self):
		return "'%s': PWR - %d, COST - %d" % (self.name, self.power, self.cost)