# """
# Creating a linked list
# """

# class Node:

# 	def __init__(self, data = None):
# 		self.data = data
# 		self.next = None


# class LinkedList:
# 	def __init__(self):
# 		self.head = Node()

# 	def append(self, data):
# 		new_node = Node(data)
# 		cur = self.head
# 		while cur.next != None:
# 			cur = cur.next
# 		cur.next = new_node

# 	def length(self):
# 		cur = self.head
# 		total = 0
# 		while cur.next != None:
# 			total+=1
# 			cur = cur.next
# 		return total

# 	def display(self):
# 		elems = []
# 		cur = self.head
# 		while cur.next != None:
# 			cur = cur.next
# 			elems.append(cur.data)

# 		print(elems)

# 	def get(self, index):
# 		if index >= self.length():
# 			print("ERROR: 'Get' index out of range.")
# 			return None

# 		cur_index = 0
# 		cur_node = self.head
# 		while cur_node:
# 			cur_node = cur_node.next
# 			if cur_index == index:
# 				return cur_node.data
# 			cur_index+=1


# 	def remove(self, index):
# 		if index >= self.length():
# 			print("ERROR: 'Remove' index out of range.")
# 			return

# 		cur_index = 0
# 		cur_node = self.head
# 		while cur_node:
# 			last_node = cur_node
# 			cur_node = cur_node.next

# 			if cur_index == index:
# 				last_node.next = cur_node.next
# 				return
# 			cur_index += 1






# my_list = LinkedList()

# my_list.append(1)
# my_list.append(3)
# my_list.append(8)
# my_list.append(0)
# my_list.display()
# print(my_list.get(1))
# print(my_list.remove(1))
# my_list.display()


class Node:
	def __init__(self,data):
		self.next = None
		self.data = data


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def add(self,data):
		new_node = Node(data)
		if self.tail:
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node

		self.size += 1

	def display(self):
		display_list = []
		cur = self.head
		while cur:
			display_list.append(cur.data)
			cur = cur.next
		print(display_list)

l = LinkedList()

l.add(4)

l.display()


