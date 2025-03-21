class Node:
    def __init__(self,k):
        self.key = k
        self.next = None



def Del_Last(head):
    if head == None:
        return None
    
    if head.next == None:
        return None
    
    temp = head
    
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head



def PrintList(head):
    curr = head
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

PrintList(head)

head = Del_Last(head)

PrintList(head)
            




