# coding: cp1252

from random import randint

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

            
# print(almostIncreasingSequence([1,2,3,1])


# matrix = [[0, 1, 1, 2], 
#           [0, 5, 0, 0], 
#           [2, 0, 3, 3]]


# for lists in matrix:
# 	for j in range(len(lists)):
# 		if lists[j] == 0:
# 			matrix[lists[j]] =0
# print(matrix)


# """Understanding list copy"""
# m = [[1,2,3],[3,2,1]]

# p = m[0][:]

# print(p)


# """
# After they became famous, the CodeBots all decided to move to a new building and live together. 
# The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. 
# Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. 
# That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

# Help the bots calculate the total price of all the rooms that are suitable for them.
# """

# def matrixElementsSum(matrix):
# 	for seq in range(len(matrix)-1):
# 		for elm in range(len(matrix[seq])):
# 			if matrix[seq][elm] == 0:
# 				matrix[seq+1][elm] = 0
	
# 	return sum([sum(row) for row in matrix])


# # alternative
# 	# t = 0
# 	# for c in zip(*matrix):
# 	# 	for r in c:
# 	# 		if r == 0:
# 	# 			break
# 	# 		t += r
# 	# return t

    

# matrix = [[0, 1, 1, 2], 
# 		[0, 5, 0, 0], 
# 		[2, 0, 3, 3]]

# print(matrixElementsSum(matrix))

# def allLongestStrings(inputArray):
# 	arr = []
# 	for i in (inputArray):
# 		if len(i) == len(max(inputArray)):
# 			arr.append(i)
# 	return arr			

# def allLongestStrings(inputArray):
# 	return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]	
    

# print(allLongestStrings(["aa","bb","aaaa","cc","bbbb"]))

# def commonCharacterCount(s1, s2):
# 	a = []
# 	b = []
# 	count = 0

# 	for char1 in s1:
# 		a.append(char1)
# 	for char2 in s2:
# 		b.append(char2)

# 	for i in range(len(a)):
# 		for j in range(len(b)):
# 			if a[i] == b[j]:
# 				b.pop(j)
# 				count+=1
# 				break
                
# 	return count

"""alternative"""

# def commonCharacterCount(s1, s2):
    
# 	com = [min(s1.count(i),s2.count(i)) for i in set(s1)]

# 	return sum(com)


# s1= "aabcc"
# s2= "adcaa"

# print(commonCharacterCount(s1,s2))

# def isLucky(n):

# 	t = [int(i) for i in str(n)]
# 	s = len(t)//2

# 	if sum(t[:s]) == sum(t[s:]):
# 		return True
# 	else:
# 		return False


# isLucky(1544)


# for i in range(3):
# 	for j in range(10):
# 		print(i)
# 		break

# x = 5
# n = 5

# a = 0
# for i in range(x):
#     a += n**i
    
# print(a)


# """
# Lychrel number
# """
# n="10154"
# d=[n]
# while n != n[::-1]:
# 	n=str(int(n)+int(n[::-1]))
# 	d.append(n)
# print(*d)

# def multipli(x):

# 	for i in range(1,10):
# 		print(i, end=": ") 

# 		for j in range(x):
# 			num = str(j*i)
# 			print(" " * (2-len(num)) + num, end=" ") # prints the number of space required before num. 2-len(num) : 0 if len(num) = 2 or 1 if len(num) = 1
# 		print() # prints a newline \n

# multipli(10)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9],]


# for seq in range(len(matrix)):
# 	for elm in range(len(matrix[seq])):
# 		print(matrix[seq][elm], end=" ")
# 	print()

# print()



# t = ["ab", "cd", "ef",]

# for i in range(len(t)):
# 	for j in range(len(t[i])):
# 		print(t[i][j], end=" ")
# 	print()


# print()

# for i in range(3):
# 	for j in range(2):
# 		print("i:",i,"j:",j)


"""
Guess the number game
"""
# import pickle
# import os

# def get_score():
# 	if os.path.exists("data_file"):
# 		with open("data_file" ,"rb") as data_file:
# 			save_scores = pickle.Unpickler(data_file)
# 			scores = save_scores.load()
# 	else:
# 		scores = {}

# 	return scores


# def save_score(scores):

# 	with open("data_file", 'wb') as data_file:
# 		saved_scores = pickle.Pickler(data_file)
# 		saved_scores.dump(scores)

# def get_name():
# 	try:
# 		print("Pls enter your name")
# 		name = input()
# 	except ValueError:
# 		print("This is not a valid name")
# 	return name

# def guess(name):
	
# 	rand_num = randint(0,21)
	
# 	guess = 6

# 	score = get_score()

# 	if name in score.keys():
# 		print("Hello", name)
# 	elif name not in score.keys():
# 		score[name] = 0

# 	while guess > 0:
# 		print("You have", guess, "guesses")
# 		print("DEBUG:",rand_num)

# 		try:
# 			print("pls chose a number")
# 			i = int(input())
# 			if i > rand_num:
# 				print("Lower")
# 				guess-=1
# 			elif i < rand_num:
# 				print("Higher")
# 				guess-=1
# 			else:
# 				print("GG", name)
# 				break
# 		except ValueError:
# 			print("This is not a number")

# 	score[name] += guess

# 	save_score(score)


# guess(get_name())


# a= [-1, 150, 190, 170, -1, -1, 160, 180]

# def sortByHeight(a):
    
#     b = sorted([i for i in a if i!=-1])
    
#     indexVal = 0
#     for i in range(len(a)):
#         if a[i] != -1:
#             a[i] = b[indexVal]
#             indexVal+=1
    
#     return a


# def reverseParentheses(s):
# 	for i in range(len(s)):
# 		if s[i] == "(":
# 			start = i
# 			print(i)
# 			print(s[:start])
# 		if s[i] == ")":
# 			end = i



# 			return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])

# 	return s

# s = "The ((quick (brown) (fox) jumps over the lazy) dog)"

# print(reverseParentheses(s))

"""
alternative
"""
# def reverseParentheses(s):
#     while ')' in s:
#         j = s.index(')')
#         i = s.rfind('(',0,j)
#         s = s[:i]+s[j-1:i:-1]+s[j+1:]
#     return s


# from operator import attrgetter, itemgetter

# my_name = "je suis Quentin Lathière"

# print(sorted(my_name.split(), key=str.lower))

# students = [("Quentin",5, 15), ("Nicolas", 15, 16), ("Cacahuete",12, 12)]

# print(sorted(students, key=lambda col: col[2]))

# print(sorted(students,key=itemgetter(2)))


# class Student:

# 	def __init__(self, name, age, grade):
# 		self.name = name
# 		self.age = age
# 		self.grade = grade

# 	def __repr__(self):
# 		return repr((self.name, self.age, self.grade))


# students_2 = [Student("Quentin", 18, 12), Student("Nico", 18, 18), Student("Jo", 5, 16)]

# print(sorted(students_2, key=lambda student: student.age))

# print(sorted(students_2, key=attrgetter("age","grade")))



# """
# stability
# """

# class Inventaire:

# 	def __init__(self, product, price, qtty):
# 		self.product = product
# 		self.price = price
# 		self.qtty = qtty


# 	def __repr__(self):

# 		return repr((self.product, self.price, self.qtty))


# inv = [Inventaire("Apple", 1, 15), Inventaire("Banana", 1.5, 20), Inventaire("Pear",1.6, 10), Inventaire("Apricot", 1.5, 24)]

# inv.sort(key=attrgetter("qtty"), reverse=True)

# print(sorted(inv, key=attrgetter("price")))




# t = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]


# for i in range(4):

# 	for j in range(4):
# 		print(t[i][j:j+3])
		
# 		s = sum(t[i][j:j+3]) + t[i+1][j+1] + sum(t[i+2][j:j+3])



# def fibo_recur(n):
# 	if n <= 2:
# 		return 1

# 	else:
# 		return fibo_recur(n-1)+fibo_recur(n-2)


# print(fibo_recur(6))


# def fibo_iter(n):
# 	a,b = 1

# 	for _ in range(2,n+1):
# 		a,b = a, a+b

# 	return b

# print(fibo_iter)



# l = []

# nom = input()
# prenom = input()


# n1,n2,n3 = [int(x) for x in input().split()]

# moy = (n1+n2+n3)//3

# print("Bonjour {} {}, la moyenne de vos 3 notes est: {}".format(prenom, nom, moy))




"""
Several people are standing in a row and need to be divided into two teams. 
The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, 
the fourth into team 2, and so on.
"""

# a = [50, 60, 60, 45, 70]

# def alternatingSums(a):
# 	t = []
# 	b = 0
# 	c = 0
# 	for i in range(len(a)):
# 		if i%2==0:
# 			b += a[i]
# 		else:
# 			c += a[i]
			
# 	t.append(b)
# 	t.append(c)

# 	return t

# print(alternatingSums(a))

# """
# alternative (beautiful)
# """
# return [sum(a[::2]),sum(a[1::2])]


# picture = ["abc", 
#  "ded"]

# def addBorder(picture):

# 	star_row = "*"*(len(picture[0])+2)

# 	return [star_row, (*["*"+row+"*" for row in picture]), star_row]


# print(addBorder(picture))


# a = [1, 1, 4]
# b = [1, 2, 3]

# def areSimilar(a, b):

# 	mismatches = []

# 	for i in range(len(a)):
# 		if a[i] != b[i]:
# 			if len(mismatches) > 1:
# 				return False
# 			if len(mismatches) == 0:
# 				mismatches.append(i)
# 			else:
# 				j = mismatches[0]
# 				if a[i] != b[j] or a[j] != b[i]:
# 					return False
# 				mismatches.append(i)

# 	return True


# print(areSimilar(a,b))


# """alternative"""
# from collections import Counter as C

# def areSimilar(A, B):
#     return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3

# inputArray = [-1000, 0, -2, 0]

# def arrayChange(inputArray):
# 	c = 0
# 	for i in range(len(inputArray)-1):
# 		if inputArray[i+1] <= inputArray[i]:
# 			inputArray[i+1]+=inputArray[i]
# 			c += 1
# 	print(inputArray)
# 	print(c)

# arrayChange(inputArray)
    






# def bubble_sort(a_list):

# 	for _ in range(len(a_list) - 1):   

# 		for j in range(len(a_list) - 1):

# 			print(j," ",end="")

# 			if a_list[j + 1] < a_list[j]:

# 				a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
# 		print()

# 	return a_list


# l = [5,2,9,7,8,0,1,6,4,3]

# print(bubble_sort(l))



# for i in range(2):
# 	print("row",i)
# 	for j in ["A","B","C"]:
# 		print(i, end="")
# 		print(j, end=" ")
# 	print()



# for i in range(5):
# 	for j in range(i+1):
# 		print("*", end="")
# 	print()


# m = [[1,2,3,4,5,6,7,8,9], ["A","B","C","D","E","F","G","H","I"]]


# for row in range(len(m)):
# 	for col in m[row]:
# 		print(col, end="")
# 	print()
# 	print(row, m[row][0])
# 	


# matrix = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]

# for row in range(len(matrix)): # each list in matrix is a row
# 	for col in matrix[row]: # each item in row is a column
# 		matrix[row][col] = row * col # for each column in each row, we compute row * col, so it goes like row0: 0*0 0*1 0*2 0*3; row1: 1*0 1*1 1*2 1*3

# 		print(matrix[row][col], " ", end="") # print each rows and cols with a space separating each item and with no newline at the end
# 	print("row",row, end="")
# 	print() # print a newline between each rows


# s = ["Je suis une phrase", "Hey ho"]

# for row in range(len(s)):
# 	for col in s[row]:
# 		print(col,end="")
# 	print()


"""
Comprehension dictionary
"""

# CANDIDATES = {
#     "hermione": "Hermione Granger",
#     "balou": "Balou",
#     "chuck-norris": "Chuck Norris",
#     "elsa": "Elsa",
#     "gandalf": "Gandalf",
#     "beyonce": "Beyoncé"
# }

# MENTIONS = [
#     "Excellent",
#     "Très bien",
#     "Bien",
#     "Assez Bien",
#     "Passable",
#     "Insuffisant",
#     "A rejeter"
# ]

# t = {candidate:[0]*len(MENTIONS) for candidate in CANDIDATES.keys()}

# print(t)




# def ask(a_list):

# 	while True:
# 		item = input("Please enter a word to search for: ").capitalize()
# 		linear_search(item, a_list)

		
# def linear_search(item, a_list):

# 	"""
# 	Linear search in a list
# 	"""
# 	found = False

# 	for i in range(len(a_list)):
# 		if a_list[i] == item:
# 			found = True

# 	if found == True:
# 		print("Found")
# 		print("Number of searches:", i+1)	
# 	else:
# 		while True:
# 			answer = input("Item not found. Do you want to add this item to the list ? (Y or N)")
# 			answer = answer.lower()

# 			if answer == "y":
# 				a_list.append(item)
# 				print("The list is now:", a_list)
# 				return False
# 			elif answer == "n":
# 				return False
# 			else:
# 				print("This is not a valid answer")


# my_list = ["Banana","Apple","Peach","Pear","Damn","Hi"]


# if __name__ == "__main__":
#     ask(my_list)


"""
Training with lists and dictionary in classes
"""

# class Products:

# 	def __init__(self, name, price, quantity):
# 		self.name = name
# 		self.price = price
# 		self.quantity = quantity

# 	def dic_conversion(self):
# 		return {self.name:{"price": self.price, "quantity": self.quantity}}

# 	def list_tuple_conversion(self):
# 		return [(self.name, (self.price, self.quantity))]


# apple = Products("Apple", 1.5, 3)

# orange = Products("Orange", 1.2, 10)

# print(apple.dic_conversion())
# print(apple.list_tuple_conversion())
# print()
# print(orange.dic_conversion())
# print(orange.list_tuple_conversion())


# PRODUCTS = ["Pear","Apple","Orange","Peach"]

# PRICE = ["1.5","1.2","1.4","1.3"]

# QUANTITY = ["3","5","6","2"]

# t = {product:{"price":price,"quantity":quantity} for product in PRODUCTS for price in PRICE for quantity in QUANTITY}

# u = [(product, (priceqtt["price"], priceqtt["quantity"])) for product, priceqtt in t.items()]

# print(u)



# string = "banana"
# s = []
# t=[]

# for i in range(len(string)):
# 	if string[i] == "a":
# 		s.append(i)

# print(s)
# print(len(s))


# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# atpos = data.find("@")
# sppos = data.find(" ", atpos)

# host = data[atpos+1:sppos]

# print(host)


# """
# array differences
# """

# inputArray = [-1000, 0, -2, 0]


# def arrayChange(inputArray):
# 	c = 0
# 	for i in range(len(inputArray)-1):
# 		if inputArray[i] >= inputArray[i+1]:
# 			diff = inputArray[i] - inputArray[i+1] + 1
# 			inputArray[i+1] = inputArray[i] + 1
# 			c+=diff
# 	return c

# print(arrayChange(inputArray))


inputString = "aaabbcceee"

# def palindromeRearranging(inputString):

# 	"""
# 	Finds if a string can be a palyndrome
# 	"""
# 	s = set()
# 	for c in inputString:
# 		if inputString.count(c) % 2 > 0:
# 			s.add(c)
# 	if len(s) > 1:
# 		return False
# 	else:
# 		return True

"""alternative one line"""

# def palindromeRearranging(inputString):

# 	return len(set(c for c in inputString if inputString.count(c) % 2 > 0)) <= 1


"""alternative one line 2"""			

# return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

# print(palindromeRearranging(inputString))

import time

from random import random

from math import ceil

lst = [3,7,1,2,3]

my_list = [7,2,3,10,3,30]
my_list2 = [0,8,9]

# def average(lst):
# 	return (sum(lst)/len(lst))

# def average(lst):
# 	j = 0
# 	nb = 0
# 	begin = time.time()
# 	for i in lst:
# 		j += i
# 		nb += 1
# 	j /= nb
# 	end = time.time() - begin
# 	print(end)
# 	return j

# print(average(lst))



# def median(lst):
# 	l = sorted(lst)
# 	if len(lst)%2==0:
# 		index = len(lst)//2
# 		return (l[index] + l[index-1])//2
# 	else:
# 		index = (len(lst)-1)//2
# 		return l[index]


# print(median(my_list))

# print(median(my_list2))



# def occurences(lst):
# 	dic = {}
# 	for c in lst:
# 		if c in dic:
# 			dic[c]+=1
# 		else:
# 			dic[c]=1

# 	return dic


# occurences(lst)

unique_lst = [2,3,1,1,3,1,4,1,3]

# def unique(lst):
# 	l = []
# 	for n in lst:
# 		if n not in l:
# 			l.append(n)

# 	return(l)


# print(unique(unique_lst))



def squares(lst):
	return [s**2 for s in lst]

print(squares(lst))


def stddev(lst):
	average = sum(lst)/len(lst)
	var = sum([(e - average)**2 for e in lst]) / (len(lst))
	ecart = var**(1/2)
	return ecart

print("Stddev : ")
print(stddev([5,4,7,4,4,2,5,9]))
print(stddev([20,20,20]))


def uniform():
	nb_0 = 0
	nb_1 = 0

	for e in range(10**6):
		n = random.randint(0,1)
		if n == 0: nb_0 += 1
		else: nb_1 += 1

	total = nb_0 + nb_1
	return "0: {}% | 1: {}%".format((nb_0*100/total), (nb_1*100/total))

print("Uniform 1 : ")
print(uniform())





