#Singly Linked Lists implementation

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.NextNode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.NextNode = b
b.NextNode = c

a.NextNode.value



class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        
        self.value = value
        self.next_node = None
        self.prev_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# Setting b after a
b.prev_node = a
a.next_node = b

# Setting c after a
b.next_node = c
c.prev_node = b


-----------------------------------------------------------

# To check if the linked list is cyclic
def cycle_check(node):
    
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.nextnode != None:
        
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        
        if marker2 == marker1:
            return True
    
    return False


-----------------------------------------------------------
#Reverse a Linked List in place

# This can be acheived by changing the next pointer of each node to point to the previous node

#Iterate trough the linked list. In loop, change next to prev, prev to current and current to next.

def reverse(head):
    current = head
    nextnode = None
    previous = None
    
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        
        previous = current
        current = nextnode
        
    return previous

------------------------------------------------------------------------
#Finding the nth node from last
#Moving a block of n element from the head to tail; 
#When the right_pointer reaches the taile (nextnode = None), the left_pointer will be the nth node from the last node
def nth_to_last_node(n,head):
    
    left_pointer = head
    right_pointer = head
    
    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError('Error:n is larger than the length of linked list')
        
        right_pointer = right_pointer.nextnode
        
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
        
    return left_pointer