class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)


def Sorted_Insert(head,x):
    temp = Node(x)

    if head == None:
        return temp

    elif head.key >= x:
        temp.next = head
        return temp
    
    # elif head.key <= x:
    #     temp = head
    #     while temp.next != None:
    #         temp = temp.next
    #     temp.next = Node(x)
    #     return head
    
    else:
        current = head
        while current.next != None and current.next.key < x:
                current = current.next
        temp.next = current.next
        current.next = temp
        return head

            
       

head = Sorted_Insert(head,35)

def PrintList(head):
    curr = head
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print("None")

PrintList(head)

