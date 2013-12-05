import entity
import random

goblin = entity.Creature("Goblin", 30, 5)
guard = entity.Creature("Guard", 40, 6)

beam = entity.Spell("Beam of Light", 15, 0)

def battle(a, b):
	if random.randrange(0, 2):
		order = [a, b]
	else:
		order = [b, a]

	print a.toString() + "\t" + b.toString()
	print order[0].name + " attacks first!"

	turn = 0
	while a.currHP > 0 and b.currHP > 0:
		turn += 1
		print "[Turn %d]-----------------------" % (turn)

		if order[0].type == "Creature":
			order[0].attack(order[1])

		print a.toString() + "\t" + b.toString()

		if order[1].currHP > 0:
			order.reverse()
		else:
			print order[1].name + " is dead!"

# battle(goblin, guard)
beam.cast(guard)
print beam.toString()
goblin.attack(guard)
print guard.toString()