class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(15)

def Travesing(Node):
    traverse = head
    while traverse is not None:
        print(traverse.key,end = " ")
        traverse = traverse.next

Travesing(Node)