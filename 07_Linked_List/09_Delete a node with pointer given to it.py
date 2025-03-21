class Node:
    def __init__(self, k):  # Fixed constructor name
        self.key = k
        self.next = None


def Del(pointer, head):
    if head is None:
        return None

    # If the head itself holds the key to be deleted
    if head.key == pointer:
        return head.next  # Move head to the next node

    curr = head
    while curr.next is not None:
        if curr.next.key == pointer:  # Find node before the one to delete
            curr.next = curr.next.next  # Skip over the node to be deleted
            return head  # Return updated head
        curr = curr.next

    return head  # Return head if the node was not found


def PrintList(head):
    curr = head
    while curr is not None:
        print(curr.key, end="->")
        curr = curr.next
    print("None")


# Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

PrintList(head)  # Output: 10->20->30->40->None

head = Del(20, head)  # Deleting node with value 20

PrintList(head)  # Expected Output: 10->30->40->None



# IF initial head is not known to us and only pointer is given then 

class Node:
    def __init__(self, k):
        self.Key = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.Key)
        curr = curr.next
    print()


    
def deleteNode(ptr):
    temp = ptr.next
    ptr.key= temp.Key
    ptr.next = temp.next
    
            
    
    
    
        

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
deleteNode(head)
printList(head)