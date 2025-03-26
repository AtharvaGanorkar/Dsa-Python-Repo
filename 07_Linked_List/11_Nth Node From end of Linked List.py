class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def Print_List(head):
    curr = head  
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print("None")

Print_List(head)


def Nth_Node(head,n):

    len = 0
    curr = head
    while curr != None:
        len +=1
        curr =curr.next

    if len < n:
        return 
    
    
    curr = head
    for i in range(1,len-n+1 ):
        curr = curr.next
    print(curr.key)

Nth_Node(head,3)



    


class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def Print_List(head):
    curr = head  
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print("None")

Print_List(head)


def Nth_Node(head,n):
    if head == None:
        return
    
    
    first = head
    for i in range(n):
        if first == None:
            return
        first = first.next

    second = head
    while first != None:
        second = second.next
        first = first.next
    print(second.key)

Nth_Node(head,2)




    
