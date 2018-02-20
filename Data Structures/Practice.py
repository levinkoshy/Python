##Linked_list cycle check

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None


def cycle_check(node):

	marker1 = node
	marker2 = node

	while marker2 != None and marker2.nextnode != None:

		marker1 = marker1.nextnode
		marker2 = marker2.nextnode.nextnode

	    if marker1 == marker2:
	    	return True
	return False


##Linked List Reversal

#In one pass from head to tail of our input list, we will point each node's next pointer to the previous element.
class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None


def reverse(head):

	current = head
	previous = None
	nextnode = None

	while current:

		nextnode = current.nextnode
        current.nextnode = previous
    
    #To move forward in the list
    previous = current
    current = nextnode

---------------------------------------------------------------------------

def nth_to_lastnode(n,head):

    leftpointer = head
    rightpointer = head

    for i in range(n-1):

    	if not rightpointer.nextnode:
    		raise LookupError ('Error: n is larger than the linked list')

    	rightpointer = rightpointer.nextnode

    while rightpointer.nextnode != None:

    	leftpointer = leftpointer.nextnode
    	rightpointer = rightpointer.nextnode

    return leftpointer


----------------------------------------------------------------------------

# Word reversal

def rev_word(s):

	words = []
	spaces = [' ']
	length = len(s)

	i = 0

	while i < length:

		if s[i] not in spaces:
			
			word_start = i
        
        while i < length and s[i] not in spaces:

        	i += 1

        words.append(s[word_start:i])


        i += 1

    return " ".join(reversed(words))         

----------------------------------------------------------

# To find if a string has only 


def unique_char(s):
    
    char = set()

	for let in s:
	    if let in char:
	        return False

	    else char.add(let)

	return True 

    
