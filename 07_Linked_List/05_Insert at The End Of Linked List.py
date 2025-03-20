class Linked_List:
    def __init__(self,k):
        self.Key = k
        self.next = None


temp1 = Linked_List(10)
temp2 = Linked_List(20)
temp3 = Linked_List(30)
head = temp1

temp1.next = temp2
temp2.next = temp3

def Insert_At_End(head,key):
        if head == None:
            return Linked_List(key)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Linked_List(key)
        return head
head = Insert_At_End(head,40)
head = Insert_At_End(head,50)

def PrintList(head):
    Current = head
    while Current != None:
          print(Current.Key,end="->")
          Current = Current.next
    print("None")  


# head = Insert_At_End(head,40)
# head = Insert_At_End(head,50)
PrintList(head)