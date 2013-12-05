class Item:
	pass

class Weapon(Item):
	def __init__(self, name, w_type, rarity, power):
		self.name = name
		self.w_type = w_type
		self.rarity = rarity
		self.power = power

	def toString(self):
		return "'%s': (%s %s) PWR +%d" % (self.name, self.rarity, self.w_type, self.power)

class Armor(Item):
	def __init__(self, name, a_type, rarity, defense):
		self.name = name
		self.a_type = a_type
		self.rarity = rarity
		self.defense = defense

	def toString(self):
		return "'%s': (%s %s) DEF +%d" % (self.name, self.rarity, self.a_type, self.defense)