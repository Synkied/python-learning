# Classes
print ("-"*8, "Classes", "-"*8)

class Dog:
	legs = 4
	def __init__(self, name, color):
	    self.name = name
	    self.color = color

	def bark(self):
		print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
print(fido.legs)

# Inheritance
print ("\n","-"*8, "Inheritance", "-"*8)

class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B):
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

# Use of super(). Function that refers to the parent class.
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2) # prints 2
    super().spam() # prints 1, the value printed by the function spam in the parent class "A".
            
print("\n")
B().spam()


# Magic methods/Dunders
print ("\n","-"*8, "Magic methods/Dunders", "-"*8)

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second # appends the x and y of "first" and x and y of "second". The "+" sign is interpreted as the method __add__ by Python.
print(result.x)
print(result.y)

print ("\n", "-"*8, "Understanding Dunders", "-"*8)
class Vector2D: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
	def __add__(self, other): 
		return Vector2D(self.x + other.x, self.y - other.y) #change +, -, * etc 
first = Vector2D(5, 7) 
second = Vector2D(3, 9) 

print("First X: ", first.x) 
print("First Y: ", first.y) 
print("---") 
print("Second X: ", second.x) 
print("Second Y: ", second.y) 
print("---result:") 
result = first + second 
print("First + second X: ", result.x) 
print("First + second Y: ", result.y)


print ("\n", "-"*8, "Weakly private method", "-"*8)
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

print ("\n", "-"*8, "Strongly private method", "-"*8)
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg) # returns error AttributeError: 'Spam' object has no attribute '__egg'

print ("\n", "-"*8, "Class method", "-"*8)
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod # used to define a method accessed by a class. (e.g.: Rectangle.new_square will work if new_square is a class method)
  def new_square(cls, side_length): # known as factory method
    return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

roh = Rectangle(7, 6)
print(roh.calculate_area())

# class Cup:
#     def __init__(self):
#         self.color = None
#         self.content = None

#     def fill(self, beverage):
#         self.content = beverage

#     def empty(self):
#         self.content = None

# redCup = Cup()
# redCup.color = "red"
# redCup.content = "tea"
# redCup.empty()
# redCup.fill("coffee")

print ("\n", "-"*8, "Static method", "-"*8)
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

  @property
  def pineapple_allowed(self):
    return False

  def add_topping(self, added_topping):
    return self.toppings.append(added_topping)

ingredients = ["cheese", "onions", "spam"]
ingredients_Pizza1 = ["cheese", "onions", "eggs", "French fries"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
  pizza1 = Pizza(ingredients_Pizza1) 

print(pizza1.toppings)

pizza1.add_topping("pineapple")
print(pizza1.toppings)

print(ingredients)


print ("\n", "-"*8, "Property", "-"*8)
class Person:
  def __init__(self, age):
    self.age = int(age)

  @property
  def isAdult(self):
    if self.age > 18:
      return True
    else:
      return False

Quentin = Person(23)
print (Quentin.age)

# Quentin.isAdult = False # AttributeError: can't set attribute, because @property makes isAdult read-only

print ("\n", "-"*8, "Setter", "-"*8)
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)