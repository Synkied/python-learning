# coding: cp1252


# def afficher_flottant(nb):
# 	if type(nb) is not float:
# 		raise TypeError("Please input a float")

# 	nb = str(nb)
# 	ent, flottant = nb.split(".")
# 	return ",".join([ent, flottant[:3]])


# print(afficher_flottant(3.9999))



# def afficher(*parametres, sep=' ', fin='\n'):
#     """Fonction chargée de reproduire le comportement de print.
    
#     Elle doit finir par faire appel à print pour afficher le résultat.
#     Mais les paramètres devront déjà avoir été formatés. 
#     On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

#     print(chaine, end='')"""
    
#     # Les paramètres sont sous la forme d'un tuple
#     # Or on a besoin de les convertir
#     # Mais on ne peut pas modifier un tuple
#     # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
#     parametres = list(parametres)
#     # On va commencer par convertir toutes les valeurs en chaîne
#     # Sinon on va avoir quelques problèmes lors du join
#     for i, parametre in enumerate(parametres):
#         parametres[i] = str(parametre)
#     # La liste des paramètres ne contient plus que des chaînes de caractères
#     # À présent on va constituer la chaîne finale
#     chaine = sep.join(parametres)
#     # On ajoute le paramètre fin à la fin de la chaîne
#     chaine += fin
#     # On affiche l'ensemble
#     print(chaine, end='')


# inventaire = [
#     ("fraises", 76),
#     ("prunes", 51),
#     ("pommes", 22),
#     ("poires", 18),
#     ("melons", 4),
# ]

# inventaire_reverse = [(fruit, qtt) for qtt, fruit in inventaire]
# print(inventaire_reverse)

# print([(fruit, qtt) for qtt, fruit in sorted(inventaire_reverse)])
# 

# echiquier = {}
# echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
# echiquier['b', 1] = "cavalier blanc" # À droite de la tour
# echiquier['c', 1] = "fou blanc" # À droite du cavalier
# echiquier['d', 1] = "reine blanche" # À droite du fou
# # ... Première ligne des blancs
# echiquier['a', 2] = "pion blanc" # Devant la tour
# echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# # ... Seconde ligne des blancs
# print(echiquier)
# 
# fruits = {"pommes":21, "melons":3, "poires":31}
# for cle in fruits.keys():
#      print(cle)

# my_string="Hello world!"

# print(my_string.split())

# class TableauNoir:

# 	def __init__(self):

# 		self.surface = ''

# 	def write(self, msg):

# 		if self.surface != "":
# 			self.surface += '\n'
# 		self.surface += msg

# 	def read(self):
# 		print(self.surface)

# 	def delete(self, index):

# 		self.surface = self.surface.split('\n')
# 		del self.surface[index]

# 		self.surface = '\n'.join(self.surface)


# tab = TableauNoir()

# tab.write("Dude, this is awesome")
# tab.write("Yeah, I know right?")
# tab.write("Please delete my message above")

# tab.read()

# tab.delete(1)
# print('\n')

# TableauNoir.write(tab, "I did :)")
# TableauNoir.read(tab)



# class Compteur:

# 	objet_cree = 0
# 	def __init__(self):

# 		Compteur.objet_cree+=1


# 	@classmethod
# 	def combien(cls):
# 		print("{} objects created.".format(cls.objet_cree))


# a = Compteur()
# b = Compteur()


# Compteur.combien()



# t = 100
# num = [n for n in range(t) if n%3 == 0 or n%5 == 0]
# print(sum(num))
# 



# word = "ni"

# file = open('my_txt.txt')
# lines = ''.join([line for line in file if word in line if not line.endswith('.')])

# print(lines)

# from random import randrange

# class CoinToss:

# 	def toss_a_coin(self):

# 		randToss = randrange(2)
# 		if randToss == 0:
# 			return "Heads"
# 		else:
# 			return "Tails"


# toss = CoinToss()

# print(toss.toss_a_coin())

# from random import randrange


# class GuessTheNumber:

# 	def play(self):
# 		randNum = randrange(101)
		
# 		while True:
# 			playerInput = int(input())	
# 			if playerInput > randNum:
# 				print("Your number is too big")
# 			elif playerInput < randNum:
# 				print("Your number is too small")
# 			else:
# 				print("GG!")
# 				break

# guessing = GuessTheNumber()

# guessing.play()

# reversed range
# for x in range(10,0,-1):
# 	print("X =", x)

# for x in reversed(range(10)):
# 	print("X =", x)

# for x in range(10):
# 	for y in range(10):
# 		print(x,y)


# Creating a MadLib game, with unpacking examples.
class MadLib:


	def getDataFromUser(self):
		noun1, adjective1, adverb1 = input(), input(), input()
		return noun1, adjective1, adverb1

	def tellStory(self, noun1, adjective1, adverb1):
		story = "This is a funny story about ", noun1, " who wandered in ", adjective1,". He was a beautiful ", adverb1
		print("".join(story))

myStory = MadLib()

userData = myStory.getDataFromUser()
myStory.tellStory(*userData) # unpacking multiple values from getDataFromuser(), using the *args.