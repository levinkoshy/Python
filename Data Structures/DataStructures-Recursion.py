#Find the factorial of a number

def fact(n):
    
    #Base Case
    if n == 0:
        return 1

    else:
        return n * fact(n-1)
-----------------------------------------------------------------------------------------

# rec_sum(4) = 4+3+2+1
def rec_sum(n):
    
    #Base Case
    if n == 0:
        return 0
    #Recursion
    else:
        return n + sum(n-1)

------------------------------------------------------------------------------------------

#Sum of the numbers of an integer
def sum_func(n):
    
    #Base Case
    if len(str(n)) == 1:
        return n
    #Recursion
    else:
        return n%10 + sum_func(n//10)

# 4876%10 = 6
#4876//10 = 487

-------------------------------------------------------------------------------------------
def word_split(phrase,list_of_words,output=None):
    
    #Base Case
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            
            return word_split(phrase[len(word):],list_of_words,output)
        
    return output

word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']

word_split('themanran',['clown','ran','man'])
[]


--------------------------------------------------------------------------------------------

# Reverse a string using recursion
def reverse(s):
    
    #Base Case
    if len(s) <= 1:
        return s
    
    #Recursion
    return reverse(s[1:]) + s[0]

-----------------------------------------------------------------------------------------------

#String permutations

#itertools can be used for this

def permute(s):
    
    out =[]
    #Base Case
    if len(s)==1:
        return [s]
    
    else:
    #Recursion
        for i,let in enumerate(s):
            
            # For every pernutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                #print(let)
                #print(perm)
                out += [let+perm]
                #print(out)
            
    return out


