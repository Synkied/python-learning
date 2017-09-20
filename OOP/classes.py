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