class Linked_list:
    def __init__(self,k):
        self.key = k
        self.next = None


def Insert_At_Begining(head,key):
    temp = Linked_list(key)
    temp.next = head
    return temp


# head = Insert_At_Begining(head,5)

def printList(head):
    curr = head
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print("None")

# printList(head)

temp1 = Linked_list(10)
temp2 = Linked_list(20)
temp3 = Linked_list(30)

temp1.next = temp2
temp2.next = temp3
head = temp1

# head = None

head = Insert_At_Begining(head,5)
head = Insert_At_Begining(head,0)
printList(head)

