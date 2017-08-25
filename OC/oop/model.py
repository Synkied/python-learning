import json
import math

class Agent:

	def __init__(self, position, **agent_attributes): # initialize the Agent class with **kwargs (a dictionary with unknown number of pairs)
		self.position = position
		for attr_name, attr_value in agent_attributes.items(): # (items() returns a list of tuple pairs, on which it's possible to iterate)
			setattr(self, attr_name, attr_value) # sets all the key:value pairs to instances of the class Agent

	# def say_hello(self, first_name):
	# 	self.first_name = first_name
	# 	return("Bien le bonjour {} !".format(first_name))

class Position:
	def __init__(self, longitude_degrees, latitude_degrees):
		self.latitude_degrees = latitude_degrees
		self.longitude_degrees = longitude_degrees

	@property
	def longitude(self):
		# Longitude in radians
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		# Latitude in radians
		return self.latitude_degrees * math.pi / 180

class Zone:

	ZONES = []
	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	WIDTH_DEGREES = 1 # degrees of longitude
	HEIGHT_DEGREES = 1 # degrees of latitude

	def __init__(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		self.inhabitants = []

	@property
	def population(self):
		return len(self.inhabitants)

	def add_inhabitant(self, inhabitant):
		self.inhabitants.append(inhabitant)

	def contains(self, position):
		return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
			position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
			position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
			position.latitude < max(self.corner1.latitude, self.corner2.latitude)

	@classmethod
	def find_zone_that_contains(cls, position):
		# Compute the index in the ZONES array that contains the given position
		longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
		latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
		longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
		zone_index = latitude_index * longitude_bins + longitude_index

		# Just checking that the index is correct
		zone = cls.ZONES[zone_index]
		assert zone.contains(position)

		return zone

	@classmethod
	def initialize_zones(cls):
		# Note that this method is "private": we prefix the method name with "_".
		cls.ZONES = []
		for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
			for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
				bottom_left_corner = Position(longitude, latitude)
				top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
				zone = Zone(bottom_left_corner, top_right_corner)
				cls.ZONES.append(zone)


def main():
	Zone.initialize_zones()
	for agent_attributes in json.load(open("agents-100k.json")): # loads the agents in the json file into a python dictionary
		latitude = agent_attributes.pop("latitude") # returns the value of the latitudes keys in the agent_attributes dictionary
		longitude = agent_attributes.pop("longitude")

		position = Position(longitude, latitude) # instatiate an object "position" with latitude and longitude as attributes

		agent = Agent(position, **agent_attributes) # instantiate an object "agent" with **kwargs attributes (named attributes, dictionary)
		agent = Agent(position, **agent_attributes)
		zone = Zone.find_zone_that_contains(position)
		zone.add_inhabitant(agent)
		print(zone.population)

main()
if __name__ == main(): # if the python script is executed from this file...
	main() # execute the "main" function