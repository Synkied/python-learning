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
# class MadLib:


# 	def getDataFromUser(self):
# 		noun1, adjective1, adverb1 = input(), input(), input()
# 		return noun1, adjective1, adverb1

# 	def tellStory(self, noun1, adjective1, adverb1):
# 		story = "This is a funny story about ", noun1, " who wandered in ", adjective1,". He was a beautiful ", adverb1
# 		print("".join(story))

# myStory = MadLib()

# userData = myStory.getDataFromUser()
# myStory.tellStory(*userData) # unpacking multiple values from getDataFromuser(), using the *args.
# 
# 


# l = input()
# s2 = l[-1] + l[:-1]
# print(l)
# while s2 != l:
#     print(s2)
#     s2 = s2[-1] + s2[:-1]
# print(s2)


# i=0
# p=""
# while True:
#     if p!=source:
#         print(source)
#     p=source
#     source=target[:i]+source[i:]
#     i+=1
#     if source==target:
#         break
# print(target)


# n = int(input())
# ok=[]
# for i in range(n):
#     a, b = [int(j) for j in input().split()]
#     i=1
#     while (b*i)%a!=1 and i<2761300 :
#         i+=1
#     if i==2761300:
#         ok.append( 'NaN')
#     else:
#         ok.append(str(i))
# print (" ".join(ok))


# n=int(input())
# p=int(input())
# a=0
# while n>1:a+=n//p;n=n//p
# print(a)

# """
# Write the shortest function to convert an IP address into it's integer representation and output it as an integer.

# To change an IPv4 address to it's integer representation, the following calculation is required:

#     Break the IP address into it's four octets.
#     (Octet1 * 16777216) + (Octet2 * 65536) + (Octet3 * 256) + (Octet4)
# """
# ipv_4 = input()

# print(sum((int(j)*4**(4*i)) for i,j in enumerate(ipv_4.split('.')[::-1])))


# """
# Printing shadocks numbers
# """

# n=int(input())
# numShadocks={0:"GA",1:"BU",2:"ZO",3:"MEU"}
# x=""
# while n>3:
#  x=numShadocks[n%4]+x;n//=4
# print(numShadocks[n]+x)

"""
output a category from an input : intervalx, intervaly, category
"""

# i=input
# x=int(i())
# i()
# while 1:
#  f,t,c=i().split()
#  if int(f)<=x<=int(t):print(c)


"""
Print a hollow square of n length
"""

# def printStars(n):
# 	if n > 1:
# 		l = ['*'*n] # top of the square
# 		l+= ['*' + ' '*(n-2) + '*'] * (n-2) # adds n-2 items to the l list, with n-2 spaces in them 
# 		l+= ['*'*n] # base of the square
# 		return l
# 	else:
# 		return "*"

# print('\n'.join(printStars(5)))  # joins the final list, with newlines, to get a square. Brillant.


# k = {1:2,3:4}

# for p,d in k.items():
# 	print(p)

# bash code
# 
# tr OLZEASGTBQolzeasgtbq 01234567890123456789


# import sys
# import math

# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.

# w, h = [int(i) for i in input().split()]
# x_1, y_1 = [int(i) for i in input().split()]
# x_2, y_2 = [int(i) for i in input().split()]
# tab=[]
# if y_1<0:
#     y_1=0
# if x_1<0:
#     x_1=0
# if x_1>x_2:
#     x_1,x_2=x_2,x_1
# if y_1>y_2:
#     y_1,y_2=y_2,y_1
# for i in range(h):
#     top=[]
#     for j in range(w):
#         if i in range(y_1,y_2+1) and j in range(x_1,x_2+1):
#             top.append('+')
#         else:
#             top.append('.')
#     tab.append(''.join(top))
# for i in tab:
#     print i


# l = int(input())
# m = int(input())
# n = int(input())

# # Write an action using print
# # To debug: print >> sys.stderr, "Debug messages..."
# for i in range(n):
#     print (l + (m*i))
# print
# for i in range(n):
#     print (l/(m**i))
# print
# 
# 
# 

# input_count = int(input())
# for i in range(input_count):
#     a,b = input().split('/')
#     b = int(b)
#     print(2**(32-b)-2)


# def factorial(n):

# 	if n <= 1:
# 		return 1
# 	else:
# 		return n*factorial(n-1)

# print(factorial(10))


# def exponentiation(n,p):
# 	if p <=0: 
# 		return 1
# 	else:
# 		return n * exponentiation(n,p-1)

# print(exponentiation(5,4))


"""
Creating a linked list
"""

class Node(object):

	def __init__(self, data, n = None):
		self.data = data
		self.next_node = n

class LinkedList(object):
	
	def __init__(self, head = None):
		self.head = head
		self.size = 0

	def add(self, data):
		new_node = Node(data, self.head)
		
		

# def checkPalindrome(inputString):
#     inputSRev = "".join([i for i in inputString][::-1])

#     print(inputSRev)
#     if inputString == inputSRev:
#         return True
#     else:
#         return False


# print(checkPalindrome("aabaa"))

# def almostIncreasingSequence(sequence):
#     dropped = False
#     last = prev = min(sequence) - 1
#     for elm in sequence:
#         if elm <= last:
#             if dropped:
#                 return False
#             else:
#                 dropped = True
#             if elm <= prev:
#                 prev = last
#             elif elm >= prev:
#                 prev = last = elm
#         else:
#             prev, last = last, elm
#     return last

            
# print(almostIncreasingSequence([1,2,3,1


# matrix = [[0, 1, 1, 2], 
#           [0, 5, 0, 0], 
#           [2, 0, 3, 3]]


# for lists in matrix:
# 	for j in range(len(lists)):
# 		if lists[j] == 0:
# 			matrix[lists[j]] =0
# print(matrix)


l = [1,2,2,3]

def factorial(n):
	"""Calculates the number of permutations of n items (n: integer >= 0)"""
	y = 1 # if x < 2, return 1
	for i in range(2,n+1): # if x >= 2...
		y*=i # calculate factorial of x. eg (x = 3 -> i in range(2,4) -> y = 1*2 -> y = 2. y = 2*3 -> y = 6. factorial of 3 is 6.)
	return y

# print(factorial(0))

def count_repetitions(a_list):
	repeted = []
	uniq = []
	for item in a_list:
		if item not in uniq: # if item is not in the uniq list, then we count the number of times it is in the origin list a_list. This assures we don't count n times the item is present //
		# eg. [1,1,1] would return 3 3 3 if we didn't count only items appended to uniq
			uniq.append(item) # append the item to the uniq list
			counting = a_list.count(item) # and count the number of times the item is present in the origin list l
			if counting > 1: # if item is repeted more than once
				repeted.append(counting) # append counting to the repeted list, to get the number of times each item is repeted
	return repeted


def permutation(x,y):
	if type(y) == list: # y can be a list of number of times of repeted items.
	# if y is such a list, we can determine how many unique permutations there are, ignoring y repeted nums
	# the calculation goes : factorial(x)//fact(y[0])*fact(y[1])....*fact(y[n]))

		m = factorial(x)
		for j in y:
			n = 1
			for i in range(2,j+1):
				m//=n*i #  (eg. factorial(8)//(factorial(2)*factorial(3)) = 3360)
		return m

	if x == 1:
		return 1
	else:
		z = factorial(x)//factorial(x-y)
		return z

def combination(x,y):
	if x == 1:
		return 1
	else:
		z = factorial(x)//(factorial(x-y)*factorial(y))
		return z


def permutlist(seq, er=False):
	"""
	Returns lists of permutations in seq
	if er = True, eliminates repeted elements
	"""
	p = [seq] # p = matrix of seq
	n = len(seq)

	for k in range(0,n-1):
		for i in range(0,len(p)):
			z = p[i][:] # p[i][:] is equivalent to list(p[i]). Creates a copy of p[i] in z
			for c in range(0,n-k-1):
				z.append(z.pop(k))

				if er==False or z not in p:
					p.append(z[:]) # copies the z list inside p, to get all permutations (with repeted elements in seq)
	print("Number of permutations:",len(p))
	return sorted(p)

# print(permutation(3,3))
print(permutation(len(l),count_repetitions(l))) # permutations of UNIQUE items in a list, via count_repetitions
# print(combination(n,k))

# print(permutlist(l))



"""Understanding list copy"""
m = [[1,2,3],[3,2,1]]

p = m[0][:]

print(p)