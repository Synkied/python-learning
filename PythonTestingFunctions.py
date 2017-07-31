# -*-coding:utf-8 -*-

# with open("test.txt", 'a+') as text_file:
# 	text_file.write('test ')
# 	content = text_file.read()
# 	print(content)

#### Jouer avec les dictionnaires
# my_dic = {1:4, 2:5}

# print(my_dic[1])
# print(my_dic[2])


# a = [1,2,3]
# b = a
# a.append(4)

# print(a)
# print(b)

# squares = {1: 1, 2: 4, 3: "error", 4: 16,} 
# squares[8] = 64 
# squares[16]=256 
# squares[17]=289 
# squares[24]=576 
# squares[32]=1024 
# squares[3] = 9 
# print(squares)

#### Jouer avec les fichiers
# def count_char(text, char):
#   count = 0
#   for c in text:
#     if c == char:
#       count += 1
#   return count

# filename = input("Enter a filename: ")
# with open(filename) as f:
#   text = f.read()

# # for char in "abcdefghijklmnopqrstuvwxyz":
# #   perc = 100 * count_char(text, char) / len(text)
# #   print("{0} - {1}%".format(char, round(perc, 2)))

# dic = {} 
# for c in "abcdefghijklmnopqrstuvwxyz": 
# 	dic[c] = 0 
	
# doc = text.lower() 
# for c in doc: 
# 	dic[c] += 1 

# 	perc = 100 * dic[c] / len(text) 
# 	print("{0} - {1}%".format(c, round(perc, 2)))

#### Jouer avec la fonction map
# def add_five(x):
#   return x + 5

# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)




#### Jouer avec les list comprehensions
print ("\n","-"*8, "List comprehensions", "-"*8)
# def assemble(words):
# 	for i in words:
# 		return ' '.join(words)
# words = 'The quick brown fox jumps over the lazy dog'.split()
# print (words)

# stuff =[[w.upper(), w.lower(), len(w), assemble(words)] for w in words]
# for i in stuff:
# 	print (i)

def mult(num):
	return num*4

nums = [1,2,3,4,5,6]

newList = [x for x in nums if x%2==0] #return a new list with even numbers
listBool = [x%2==0 for x in nums] #returns a new list with booleans for each numbers. True if even
lambdaMap = list(map(lambda x:x*4, nums)) #returns a new list with each item *4. Using lambda to map
lambdaFilter = list(filter(lambda x:x%2==0, nums)) #returns a new list with only even numbers. Using lambda to filter
listCompMap = [x*4 for x in nums] # maps items using list comprehensions
simpleMap = list(map(mult,nums)) # maps items using map

print(newList)
print(listBool)
print(lambdaMap)
print(lambdaFilter)
print(listCompMap)
print(simpleMap)

# Generators
print ("\n","-"*8, "Generators", "-"*8)

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print("Generators: ", list(numbers(11)))

# Decorators
print ("\n","-"*8, "Decorators", "-"*8)

def decor(func):
	def wrap():
		print("="*5)
		func()
		print("="*5)
	return wrap

def print_text():
	print("Hello World !")

decorated = decor(print_text)
decorated()

# Recursion
print ("\n","-"*8, "Recursion", "-"*8)

def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1) # for 5 : 5 * factorial(4) ; 4 * factorial(3) ; 3 * factorial(2) ; 2 * factorial(1) ; stops. 5*4*3*2*1 = 120
    
print(factorial(5))

# Sets
print ("\n","-"*8, "Sets", "-"*8)

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

# ------------
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

# Understanding magic classes
print ("\n","-"*8, "Understanding magic classes", "-"*8)

x = [1,2,3,4]

x[0]=2 # this is the same as...
print(x[0])

x.__setitem__(0,2) # ...this
print(x[0])
