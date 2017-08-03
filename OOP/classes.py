class Fighter():

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attacks(self, other_fighter):
		other_fighter.health -= self.damage
		print(("{} attacks {} and deals {} damage").format(self.name, other_fighter.name, self.damage))
		print(("{} has {} health points left").format(other_fighter.name, other_fighter.health))

	def __str__(self):
		return "{}: {}".format(self.name, self.health)


ken = Fighter("Ken")
ryu = Fighter("Ryu")
print(ken)
print(ryu)

ryu.attacks(ken)