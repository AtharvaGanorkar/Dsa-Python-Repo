class Node:
    def __init__(self, k):
        self.Key = k
        self.next = None

# Creating the linked list
temp1 = Node(10)
temp2 = Node(10)
temp3 = Node(10)
temp4 = Node(10)
temp5 = Node(10)

head = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
temp4.next = temp5

def Insert(head, pos, Key):
    temp = Node(Key)

    # If inserting at the beginning
    if pos == 1:
        temp.next = head
        return temp # New head

    current = head
    count = 1

    # Traverse until the node before the desired position
    while current is not None and count < pos - 1:
        current = current.next
        count += 1

    # If position is greater than the length of the list
    if current is None:
        print("Position out of range")
        return head

    # Insert the new node
    temp.next = current.next
    current.next = temp

    return head  # Return the updated head

def PrintList(head):
    curr = head
    while curr is not None:
        print(curr.Key, end=" -> ")
        curr = curr.next
    print("None")

# Inserting at position 4
head = Insert(head, 4, 45)
PrintList(head)
