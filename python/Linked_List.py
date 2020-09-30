class Node:
	def __init__(self, val=None):
		self.dataval = val
		self.nextval = None

class LinkedList:
	def __init__(self):
		self.head = None

	def atStart(self, val=None):
		newNode = Node(val)
		newNode.nextval = self.head
		self.head = newNode

	def atEnd(self, val=None):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			return 
			
		ptr = self.head
		while ptr.nextval:
			ptr = ptr.nextval
		ptr.nextval = newNode

	def inBetween(self, middleNode, val):
		if middleNode is None:
			return 

		newNode = Node(val)
		newNode.nextval = middleNode.nextval
		middleNode.nextval = newNode


	def print(self):
		ptr = self.head
		while ptr is not None:
			print(ptr.dataval)
			ptr = ptr.nextval


LL = LinkedList()
LL.head = Node("Monday")
n1 = Node("Tuesday")
n2 = Node("Wednesday")

LL.head.nextval = n1
n1.nextval = n2
LL.atStart("Sunday")
LL.atEnd("Thursday")

LL.inBetween(n2.nextval, "Friday")
LL.atEnd("Saturday")

LL.print()