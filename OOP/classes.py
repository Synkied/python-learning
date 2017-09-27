import pickle
# # """
# # Building a Fighter class to learn classes
# # """

# # class Fighter():

# # 	def __init__(self, name):
# # 		self.name = name
# # 		self.health = 100
# # 		self.damage = 10

# # 	def attacks(self, other_fighter):
# # 		other_fighter.health -= self.damage
# # 		print(("{} attacks {} and deals {} damage").format(self.name, other_fighter.name, self.damage))
# # 		print(("{} has {} health points left").format(other_fighter.name, other_fighter.health))

# # 	def __str__(self):
# # 		return "{}: {}".format(self.name, self.health)


# # ken = Fighter("Ken")
# # ryu = Fighter("Ryu")

# # print(ken)
# # print(ryu)

# # ryu.attacks(ken)


# """
# Builds a Library class with books to check out and return on certain days. Use of dictonaries and call of Book class in Library class
# """

# class Library:

# 	def __init__(self, bookCollection, currentDay = 0, lengthOfCheckoutPeriod = 7, fees = 1):
# 		self.bookCollection = bookCollection
# 		self.currentDay = currentDay
# 		self.lengthOfCheckoutPeriod = lengthOfCheckoutPeriod
# 		self.fees = fees


# 	def checkOutBook(self, bookName):
# 		book = bookCollection.get(bookName)
# 		if book.isCheckedOut:
# 			print("Sorry, {} already checked out. It should be back on day {}. Which is in {} days.".format(book.bookName, 
# 				book.dayOfCheckOut + self.lengthOfCheckoutPeriod, self.lengthOfCheckoutPeriod - self.currentDay))
# 		else:
# 			book.checkingOut(self.currentDay)
# 			print("You just checked out {} on day {}. It is due on day {}".format(bookName, self.currentDay, self.currentDay+self.lengthOfCheckoutPeriod))

# 	def returnBook(self, bookName):
# 		book = bookCollection.get(bookName)
# 		daysLate = self.currentDay - (book.dayOfCheckOut + self.lengthOfCheckoutPeriod)
# 		if daysLate > 0:
# 			print("You owe the library ${}, because your book is {} day(s) overdue.".format(daysLate*self.fees, daysLate))
# 		else:
# 			print("{} returned on day {}. Thank you.".format(book.bookName, self.currentDay))

# 		book.isCheckedOut = False


# 	def nextDay(self):
# 		self.currentDay+=1



# class Book:

# 	def __init__(self, bookName, ISBN, dayOfCheckOut = -1):
# 		self.bookName = bookName
# 		self.ISBN = ISBN
# 		self.isCheckedOut = False
# 		self.dayOfCheckOut = dayOfCheckOut

# 	def checkingOut(self, currentDayCheckOut):
# 		self.isCheckedOut = True
# 		self.dayCheckedOut(currentDayCheckOut)

# 	def dayCheckedOut(self, day):
# 		self.dayOfCheckOut = day




# harry = Book("Harry Potter", 999999)
# pouet = Book("Pouet", 999)

# bookCollection = {"Harry Potter": harry, "Pouet":pouet} 
# """ 
# the call to the instance harry and pouet, makes it so that we can call book.dayCheckedOut in Library class when we do "book = bookCollection.get(bookName)"
# because the dict.get() method gets the value for the provided key bookName. That value is the call to the instance created (here harry or pouet) so we can access every attribute of the instance.
# """ 

# lib = Library(bookCollection)

# lib.checkOutBook("Harry Potter")
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.nextDay()
# lib.checkOutBook("Pouet")
# lib.returnBook("Harry Potter")
# lib.checkOutBook("Harry Potter")
# lib.returnBook("Pouet")



# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author   
#     @abstractmethod
#     def display(): pass

# #Write MyBook class
# class MyBook(Book):
    
#     def __init__(self, title, author, price):
#         super(Book, self).__init__()
#         self.price = price
       
#     def display(self):
#         print("Title: {}".format(title))
#         print("Author: {}".format(author))
#         print("Price: {}".format(price))

# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# new_novel.display()


class ZDict():

	def __init__(self):

		self._dictionary = {}

	def __getitem__(self, index):

		if index in self._dictionary:
			return self._dictionary[index]
		else:
			return "INDEX ERROR: Index out of range"

	def __setitem__(self, index, value):
		self._dictionary[index] = value

	def __str__(self):
		return "{}".format(self._dictionary)

	def __contains__(self, obj):
		if obj in self._dictionary:
			return True
		else:
			False

	def __len__(self):
		return len(self._dictionary)


z = ZDict()
z[0] = 10
z[1] = 15
z[2] = 20
z[3] = 25

print(0 in z)

print(z)


class Duration:

	def __init__(self, mins = 0, sec = 0):
		self.mins = mins
		self.sec = sec

	def __str__(self):
		return "{0:02}:{1:02}".format(self.mins, self.sec)

	def __add__(self, obj_to_add):
		new_dur = Duration()

		new_dur.mins = self.mins
		new_dur.sec = self.sec

		new_dur.sec += obj_to_add

		if new_dur.sec >= 60:
			new_dur.mins += new_dur.sec // 60
			new_dur.sec %= 60
		return new_dur

	def __radd__(self, obj_to_add):
		return self + obj_to_add

	def __eq__(self, other_dur):

		return self.sec == other_dur.sec and self.mins == other_dur.mins

	def __gt__(self, other_dur):
		nb_sec1 = self.sec + self.mins * 60
		nb_sec2 = other_dur.sec + other_dur.mins * 60

		return nb_sec1 > nb_sec2


d = Duration(15,15)

print(d)
d += 80

print(d)


