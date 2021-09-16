from deleteNode import LinkedList, Node

llist = LinkedList()
firstNode = Node(10)
llist.head = firstNode
secondNode = Node(11)
thirdNode = Node(14)
fourthNode = Node(22)
fifthNode = Node(5)
firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = fifthNode

print(llist)