# replacing chars
# def disemvowel(string):
#     newString = ""
#     vowels = ["a","e","i","o","u","A","E","I","O","U"]
#     for i in string:
#         if i in vowels:
#             del(i)
#         else:
#             newString+=i
#     return newString


# print(disemvowel("This website is for losers LOL!"))

# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")

# print(disemvowel("This website is for losers LOL!"))

# replacing chars

# def song_decoder(song):
# 	dubstepSound = "WUB"

# 	if dubstepSound in song:
# 		oldSong = song.replace(dubstepSound, " ").lstrip(" ") # replaces all "WUB" by a whitespace. Strips whitespaces from the beginning and the end of the string
# 		return " ".join(oldSong.split()) # in short : this deletes double whitespaces
# 		"""
# 		This is equivalent to :
# 		newSong = oldSong.split() # this splits the string into list of strings (split() takes whitespace as default value)
# 		print(newSong)
# 		print (" ".join(newSong)) # joins the elements of the list newSong, using a single whitespace
# 		"""

# print (song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))

# cube building
# def find_nb(m):

#     volume = 0
#     n = 0
#     while volume < m: # while volume inferior to m
#     	print("n =",n)
#         volume += n ** 3 # volume = volume + n^3
#         print("volume =",volume)
#         if volume == m: # if volume equals to m, return n
#             return n
#         n += 1
#     return -1


# print(find_nb(100))


# def make_negative(number):
# 	if number > 0:
# 		number -= number*2
# 		return number
# 	elif number < 0:
# 		return number
# 	else:
# 		return 0

# print(make_negative(100))

# alternatives : 
# def make_negative(number):
#     return -abs(number)

# def make_negative( number ):
#     return -number if number>0 else number

"""
Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
"""
# from math import sqrt

# def is_square(n):
# 	if n < 0:
# 		return False
# 	else:
# 	    root = sqrt(n)
# 	    if int(root) ** 2 == n: 
# 	        return True
# 	    else:
# 	        return False

# alternatives
# from math import sqrt

# def is_square(n):
#     return n > 0 and sqrt(n).is_integer()

"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


"""
# def isValidWalk(walk):
#     d = {
#         's': [0, -1],
#         'n': [0, +1],
#         'w': [-1, 0],
#         'e': [+1, 0],
#     }
#     x, y = 0, 0
#     if len(walk) != 10:
#         return False
#     for w in walk:
#         x += d[w][0]
#         y += d[w][1]
# 	return x == 0 and y == 0

"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""

# def filter_list(l):
# 	newList = []
# 	for item in l:
# 		if type(item) != str: # check if item in list is not a string. if it is not, appends to newlist
# 			newList.append(item)
# 	return newList

# print (filter_list([1,2,'a','b']))

# alternatives
# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [i for i in l if not isinstance(i, str)]


# def gimme(input_array):
# 	sorted_array = sorted(input_array)
# 	middle = sorted_array[1]
# 	return input_array.index(middle)

# gimme([1,3,4])


# alternatives
# def gimme(inputArray):
#     # Implement this function
#     return inputArray.index(sorted(inputArray)[1])

# gimme([1,3,4])


"""
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets. 
"""
# def duplicate_count(text):
# 	count = 0
# 	new_text = set(text.lower()) # transforme the list to a set (list without duplicates)
# 	for item in new_text: # evaluates each item in the set
# 		if text.lower().count(item) > 1: # if item in the set is represented more than one time in the evaluated string...
# 			count+=1 # ...increment count
# 	return count

# print(duplicate_count('abcdeabB'))

# alternative
# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])


# def calculate_years(principal, interest, tax, desired):

# 	inter_sum = 0
# 	years = 0

# 	while (principal <= desired): # while principal does not equal or greater than desired
# 		if principal == desired: # if principal = desired, return 0 years
# 			return 0
# 		else:
# 			inter_sum = (principal*interest) - (principal*interest*tax) # (e.g. inter_sum = (1000*0.05)-(1000*0.05*0.18)), inter_sum = 50 - 9, inter_sum = 41
# 			principal+=inter_sum # increment principal income
# 			years+=1 # increment year until principal >= desired
# 	return years
	

# print((calculate_years(1000, 0.05, 0.18, 1100)))


# def tickets(people):
# 	cashier = {100:0, 50:0, 25:0}

# 	for i in people:
# 		if i == 25:
# 			cashier[25]+=1
# 		elif i == 50:
# 			cashier[50]+=1
# 			if cashier[25] == 0:
# 				return "NO"
# 			cashier[25]-=1
# 		else:
# 			cashier[100]+=1
# 			if cashier[50] >= 1 and cashier[25] >=1:
# 				cashier[50]-=1
# 				cashier[25]-=1
# 			elif cashier[25]>=3:
# 				cashier[25]-=3
# 			else:
# 				return "NO"
# 	return "YES"			

# print(tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]))


# alternatives
# def tickets(people):
#   till = {100.0:0, 50.0:0, 25.0:0}

#   for paid in people:
#     till[paid] += 1
#     change = paid-25.0
    
#     for bill in (50,25):
#       while (bill <= change and till[bill] > 0):
#         till[bill] -= 1
#         change -= bill

#     if change != 0:
#       return 'NO'
        
#   return 'YES'

# recursion with cache (limited recursion)
# cache = {}

# def f(n):
# 	if type(n) != int or int(n) < 1:
# 		raise TypeError("n must be a positive int")
# 	if n in cache:
# 		return cache[n]
# 		return None
# 	if n == 1 or n == 2:
# 		value = 1
# 	else:
# 		value = f(n-1) + f(n-2)

# 	cache[n] = value
# 	print(cache)
# 	print(cache[n])
# 	return value

# print(f(5))


# def f(n):
# 	if type(n) != int or n < 1:
# 		raise TypeError("n must be a positive int")
# 		return None

# 	for i in range(1,n):
# 		n+=i
# 	print(n)
# 	return n

# print(f(5))

# alternative
# def f(n):
#     return n * (n + 1) // 2 if (n > 0 and isinstance(n, int)) else None

# print(f(5))


# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.
# def sum_two_smallest_numbers(numbers):
#     	s = sorted(numbers)
#     	return s[0]+s[1]

# sum_two_smallest_numbers([19,5,42,2,77])

# alternative
# def sum_two_smallest_numbers(numbers):
    # return sum(sorted(numbers)[:2])



"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""
# import re
# def validate_pin(pin):


"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
"""
# def find_longest(arr):


# print(find_longest([8, 900, 500]))
# 
# 
# 

# fighters = [
# 	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
# 	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# opts = ["up","down","right","left"]

# MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

# def street_fighter_selection(fighters, initial_position, moves):
#     y, x = initial_position
#     hovered_fighters = []
#     for move in moves:
#         dy, dx = MOVES[move]
#         y += dy
#         if not 0 <= y < len(fighters):
#             y -= dy
#         x = (x + dx) % len(fighters[y])
#         hovered_fighters.append(fighters[y][x])
#     return hovered_fighters

# print(street_fighter_selection(fighters, (0,0), ["left"]*8))

# alternative
# 
#  def street_fighter_selection(fighters, initial_position, moves):
#     cur_pos = [initial_position[0], initial_position[1]]
#     selected_fighters = []

#     for move in moves:
#         if move == "up": 
#             cur_pos[0] = 0
#         elif move == "down": 
#             cur_pos[0] = 1
#         elif move == "right":
#             cur_pos[1] = (cur_pos[1] + 1) % 6
#         elif move == "left":
#             cur_pos[1] = (cur_pos[1] - 1) % 6
#         selected_fighters.append(fighters[cur_pos[0]][cur_pos[1]])

#     return selected_fighters
#     

"""
Unscramble the eggs.

The string given to your function has had an "egg" inserted directly after each consonant. You need to return the string before it became eggcoded.
"""
# import re
# def unscramble_eggs(word):
# 	matchObj = re.sub(r'(egg)*','', word) # sub replaces a string. The usage is : re.sub(pattern, replacing_string, original_string)
# 	return matchObj


"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
"""

# def getCount(inputStr):
# 	num_vowels = 0
# 	vowels = ["A","I","U","E","O"]

# 	for char in inputStr.upper():
# 		if char in vowels:
# 			num_vowels+=1
# 	return num_vowels

# print(getCount("abracadabra"))

# # alternative

# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")
#     

# def mean(lst):
# 	a = []
# 	chars = ""
# 	nums = []
# 	for item in lst:
# 		if item.isalpha(): # check if item is in the alphabet
# 			chars+=item
# 		elif item.isdigit(): # check if item is a digit
# 			item = int(item) # convert item to integer
# 			nums.append(item) # append all items to nums
# 			mean_cal = sum(nums)/len(nums) # get the sum of all items in nums and divide by the number of items in nums (calulating the mean)

# 	a.append(mean_cal) # append mean_cal to a
# 	a.append(chars) # append chars to a
# 	return a


# lst = ["u", "6", "d", "1", "i", "w", "6", "s", "t", "4", "a", "6", "g", "1", "2", "w", "8", "o", "2", "0"]
# print(mean(lst))


# #alternative
# def mean(lst):
#     return [sum(int(n) for n in lst if n.isdigit()) / 10.0, "".join(c for c in lst if c.isalpha())]


# def black_or_white_key(key_press_count):
#     return "black" if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11] else "white"


# w, b = "white", "black"
# keyboard = [w, b, w, w, b, w, b, w, w, b, w, b]

# def black_or_white_key(count):
#     return keyboard[(count - 1) % 88 % 12]
#     

# Count characters in your string

# def count(string):
# 	letters_count = {}
# 	for char in string:
# 		letters_count[char] = 0
# 	for char in string:
# 		if string.count(char) >= 1:
# 			letters_count[char] += 1
# 		else:
# 			letters_count = {}
	
# 	return letters_count

# print(count('abaaaa'))



# Regexp Basics - is it IPv4 address?


# def ipv4_address(address):
#     #your code heren