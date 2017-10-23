"""
Creating binary search trees
"""

class Node:

	def __init__(self, val):
		self.value = val
		self.left_child = None
		self.right_child = None


	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left_child:
				return self.left_child.insert(data)
			else:
				self.left_child = Node(data)
				return True
		else:
			if self.right_child:
				return self.right_child.insert(data)
			else:
				self.right_child = Node(data)
				return True 


	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.left_child:
				return self.left_child.find(data)
			else:
				return False
		else:
			if self.right_child:
				return self.right_child.find(data)
			else:
				return False

	def preorder(self):

		


		

class Tree:

	def __init__(self):
		self.root = None


	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True


	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def preorder(self):
		print("PreOrder")
		self.root.preorder()


	def postorder(self):
		print("PostOrder")
		self.root.postorder()

	def inorder(self):
		print("InOrder")
		self.root.inorder()