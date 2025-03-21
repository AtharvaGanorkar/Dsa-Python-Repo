class Linked_List:
    def __init__(self,k):
        self.key = k
        self.next = None

temp1 = Linked_List(10)
temp2 = Linked_List(20)
temp3 = Linked_List(30)
temp4 = Linked_List(40)

head =  temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4

def Del(head):
    if head == None:
        return None
    else:
        temp = head
        head = head.next
        temp.next = None
        del temp
        return head
    

head = Del(head)

def PrintList(head):
    curr = head
    while curr != None:
        print(curr.key,end="->")
        curr = curr.next
    print("None")

PrintList(head)

    


    