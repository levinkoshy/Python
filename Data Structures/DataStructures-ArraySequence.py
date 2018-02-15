# Anagram
#if the frequency of elements in 2 strings are equal, they will be anagrams

#if 2 strings are equal after sorting, then also they are anagrams of each other

def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    return sorted(s1)==sorted(s2)


anagram("god","dog")


def anagram2(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
    	    return False
 
    return True
------------------------------------------------------------------------
##Array Pair Sum
def pair_sum(arr,k):
    
    if len(arr) < 2:
        return
    #sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k-num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
            
    #return len(output)
    return output

---------------------------------------------------------------------------
##Find missing elements in the second array
#The second array is shuffled and some elements are removed

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    for num1,num2 in zip(arr1,arr2):
        if num1!=num2:
            return num1
    return arr1[-1]
#zip creates tuples of elements of both arrays based on their position


def finder2(arr1,arr2):
    
    d=collections.defaultdict(int)
    #default dict - If the key is not avaialable in the dictionary it will be added to the dict
    
    for num in arr2:
        d[num] +=1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1
------------------------------------------------------------------------------

##largest continuous Sum

#array in python is a list

def large_count_sum(arr):
    
    if len(arr)==0:
        return 0
    
    current_sum = max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        
        max_sum = max(current_sum,max_sum)
        
    return max_sum

------------------------------------------------------------------------------

#Reverse words in a string

def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']
    
    i=0
    
    while i < length:
        if s[i] not in spaces:
            word_start = i
            
            while i < length and s[i] not in spaces:
                i +=1 
        
            words.append(s[word_start:i])
        
        i += 1
    
    return " ".join(reversed(words))

-----------------------------------------------------------------------------------

#compressing
def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    return r

----------------------------------------------------------------------

# Strings with unique characters

#my solution
def unique(s):
    
    d = collections.defaultdict(int)
    
    for st in s:
        d[st] += 1
        
    for k in d:
        if d[k] != 1:
            return False
    return True


def unique2(s):
    if len(set(s))!=len(s):
        return False
    else:
        return True

def unique3(s):
    
    chars = set()
    for letter in s:
        if letter in st:
            return False
        else:
            chars.add(letter)
    return True
            