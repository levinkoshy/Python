#Python

and operator - 'and'

l=[]
print ','.join(l)

#gives the elements of the list separated by ','

#to find the factorial of a given number
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


n=int(raw_input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i


#io-34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t

import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)


-----------------------------------------------------------
input_str = raw_input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col



items = [x for x in input_str.split(",")]
itemsSorted = items.sort()
print ','.join(items)


s = "hello world and practice makes perfect and hello world again"
ls = [x for x in s.split(" ")]
print ','.join(sorted(set(list(ls))))


## convert binary to integer
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)


value=[]
for i in range(1000,3001):
    if i%2==0:
        value.append(str(i))

print ','.join(value)


s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]


ls = [int(x) for i in string.split]


##dictionary initialization
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():	
        print v


# slicing list
#5: after fifth index element to rest
#:5: Till 5th index element 
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print li[5:]
		
printList()
##tuple
def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print tuple(li)
		
printTuple()

##filtering a list
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print evenNumbers

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers


##even numbers between 1 and 21 (both included)
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print evenNumbers

#**********
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()


class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()

###
raise RuntimeError('something wrong')


import re
emailAddress = "lk@io.com"
pat2 = "(\w+)@(\w+).(com)"
r2 = re.match(pat2,emailAddress)
print r2.group(2)
#the patterns needed are enclosed in the bracket
#and divides into groups
#this is group 2



## re.findall returns the digits as a list
>>> s = "2 cats and 3 dogs"
>>> print re.findall("\d+",s)
['2', '3']


s = raw_input()
u = unicode( s ,"utf-8")
print u


##fibonacci series
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(raw_input())
print f(n)

n=int(raw_input())
values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)



#assert would give error if the condition fails
li = [2,4,6,8]
    for i in li:
        assert i%2==0

#if 35+3 is the input -- output will be 38
expression = raw_input()
print eval(expression)

#binary search
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)



import random
print random.random()*100-5

import random
print random.choice([i for i in range(11) if i%2==0])



#iterate a list by 2 elements
s=[1,2,3,4,5,6,7,8,8]
s = s[::2]
print s

>>1,3,5,7,8

## to iterate by 3 elements -- ::3 and so on
 s="H1e2l3l4o5w6o7r8l9d"
>>> s = s[::2]
>>> print s
Helloworld


#itterate list in the reverse order
[::-1]

##itertools.permutations()

import itertools
print list(itertools.permutations([1,2,3]))


###intersection of 2 sets
set1 &= set2


#removing an element from the list
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print li


##enumerate will get the index too
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print li


#3*5*8 3D Array filled with 0
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array

import random
print random.choice([i for i in range(201) if i%5==0 and i%7==0])



##generator -- yield -- not understood

def createGenerator():
    mylist = range(3)
    for i in mylist:
       yield i*i

mygenerator = createGenerator()
print(mygenerator)

for i in mygenerator:
    print(i)

#for loop on my generator can be used only once 

#range-- (1,21)-- 21 won't be included; it will be 1 to 21

# frequency of different words in a line
>>> freq={}
>>> line="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
>>> for word in line.split():
...     freq[word] = freq.get(word,0)+1
...
>>> words = freq.keys()
>>> words.sort()
>>> words
['2', '3.', '3?', 'New', 'Python', 'Read', 'and', 'between', 'choosing', 'or', 'to']
>>> words.sort(key=str.lower)
>>> words
['2', '3.', '3?', 'and', 'between', 'choosing', 'New', 'or', 'Python', 'Read', 'to']

##robot
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))

#to check if a password is valid
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)

"(D 300)(D 300)(W 200)(D 100)"