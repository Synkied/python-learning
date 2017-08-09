import json

class Agent:

	def __init__(self, **agent_attributes):
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)


	# def say_hello(self, first_name):
	# 	self.first_name = first_name
	# 	return("Bien le bonjour {} !".format(first_name))

def main():

	
	for agent_attributes in json.load(open("agents-100k.json")):
		agent = Agent(**agent_attributes)
		print(agent.agreeableness)

if __name__ == main():
	main()