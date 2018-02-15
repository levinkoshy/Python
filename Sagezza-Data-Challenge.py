#scala
object Solution {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        var s = new Array[Int](n);
        for(s_i <- 0 to n-1) {
           s(s_i) = sc.nextInt();
        }
        var d = sc.nextInt();
        var m = sc.nextInt();
        var i = 0;
        var counter =0;
        var x=0;
        while (i<n-m+1){
           var total=0;
           for(x <- i to i+m-1){
                 total += s(x);
           }
           if (total==d) counter += 1;
             i += 1;
        }
        println(counter);
    }
}

--------------------------------------------------------------------------------
#3
#!/bin/python

import sys

def twoCharaters(s):
    l= list(s)
    li =[]
    dic={}
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            li = [x for x in l if x!=l[i]]
    if len(li)==0:
        return 0
    elif len(set(li)) >2:
        d = {x:li.count(x) for x in li}
        dic.update(dict(sorted(d.items(), key=lambda x:x[1], reverse=True)[:2]))
        lis = [x for x in dic.keys()]
        list1 = [x for x in li if x in lis]
        return len(list1)
    else:
        return len(li)
                        
            
    # Complete this function

if __name__ == "__main__":
    l = int(raw_input().strip())
    s = raw_input().strip()
    result = twoCharaters(s)
    print result

#----------------------------------------------------------------------------------
##
#Insertion sort
#!/bin/python

import sys

def insertionSort1(n, arr):
    # Complete this function
    position = len(arr)-1
    currentvalue = arr[position]
    while position>0 and arr[position-1]>currentvalue:
        arr[position]=arr[position-1]
        position = position-1
        print arr  
        
    arr[position]=currentvalue
    print arr


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    insertionSort1(n, arr)

#---------------------------------------------------------------------------------
#2 numbers
#!/bin/python3

import sys    
    
def missingNumbers(arr, brr):
    # Complete this function
    c = []
    b_dict = {}
    a = set(arr)
    b = set(brr)
    a_dict = {i:arr.count(i) for i in set(arr)}
    b_dict = {i:brr.count(i) for i in set(brr)}
    
    for b_key,b_freq in b_dict.items():
        if a_dict[b_key]:
            if a_dict[b_key] != b_freq:
                c.append(b_key)
        else:
            c.append(b_key)
    
    return c
        
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))
