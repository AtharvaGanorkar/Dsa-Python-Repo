class node:
    def __init__(self,k):
        self.key = k
        self.next = None

temp1 = node(10)
temp2 = node(20)
temp3 = node(30)
temp4 = node(40)

temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
head = temp1

print()

def Print_Linked_List(head):
    current = head
    while current is not None:
        print(current.key,end="->")
        current= current.next
    print("None")

Print_Linked_List(head)