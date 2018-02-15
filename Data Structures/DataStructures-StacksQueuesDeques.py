#Stacks 

#Top & Base
#Top - Items are added to and removed from Top

#Last In First Out - LIFO

#popping out stacks can help in reversing the elements in a stack

#push
#pop
#peek
#isempty
#size


#Queue

#Addition of elements happen at one end - "Rear End" : Enqueue
#Removal of elements happen at the other end - "Front End" : Dequeue

#First In First Out - FIFO 

#enqueue
#dequeue
#isempty
#size

---------------------------------------------------------------------

#balance check
def balance_check(s):
    
    # Check is even number of brackets
    if len(s)%2 != 0:
        return False
    
    # Set of opening brackets
    opening = set('([{') 
    
    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    # Use a list as a "Stack"
    stack = []
    
    # Check every parenthesis in string
    for paren in s:
        
        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)
        
        else:
            
            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False
            
            # Check the last open parenthesis
            last_open = stack.pop()
            
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0


-------------------------------------------------------------------------------

#Implementing Queue using 2 stacks
class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        
        # Add an enqueue with the "IN" stack
        self.instack.append(element)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()  
