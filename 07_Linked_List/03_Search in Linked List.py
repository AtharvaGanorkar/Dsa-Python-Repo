class Node:
    def __init__(self,k):
        self.key = k
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(15)

def Search(head,X):
    n = 0
    current = head
    while current is not None:
        if X == current.key :
            return n
        n +=1
        current = current.next
    return -1
        

print(Search(head,20))