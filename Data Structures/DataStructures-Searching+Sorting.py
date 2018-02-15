#Binary Search

#array -not ordered

def seq_search(arr,ele):
    
    pos = 0
    found = False
    
    while pos < len(arr) and not found:
        
        if arr[pos] == ele:
            found = True
        else:
            pos +=1
            
    return found


#array ordered; We can stop searching when the element in the array is greater than the key
def ordered_seq_search(arr,ele):
    
    pos = 0
    found = False
    stopped = False
    
    while pos < len(arr) and not found and not stopped:
        
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos +=1
            
    return found


------------------------------------------------------------------------------------------
#Binary search, because we are splitting the array into 2 each time.

# will work only on a sorted array

def binary_search(arr,ele):
    
    first = 0
    last = len(arr)-1
    
    found = False
    
    while first <= last and not found:
        
        mid = (first+last)//2
        
        if arr[mid] == ele:
            found = True
            
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found 


---------------------------------------------------------------------------------------------

## Recursive binary search

def rec_bin_search(arr,ele):
    
    if len(arr) == 0:
        return False
    
    else:
        
        mid = len(arr)//2
        
        if arr[mid] == ele:
            return True
        
        else:
            
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            else:
                return rec_bin_search(arr[mid+1:],ele)






--------------------------------------------------------------------------------------------

##Bubble Sort
def bubble_sort(arr):
    
    for n in range(len(arr)-1,0,-1):
        for k in  range(n):
            
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] =temp


---------------------------------------------------------------------------------------

## Selection sort

def selection_sort(arr):
    
    for fillslot in range(len(arr)-1,0,-1):
        
        positionOfMax = 0
        
        for location in range(1,fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
                
        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

---------------------------------------------------------------------------------------
## Insertion Sort

def insertion_sort(arr):
    for i in range (1,len(arr)):
        
        currentValue = arr[i]
        position = i
        
        while position > 0 and arr[position-1] > currentValue:
            
            arr[position] = arr[position-1]
            position = position - 1
            
        arr[position] = currentValue

-----------------------------------------------------------------------------------------

##Shell sort

def shell_sort(arr):
    
    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        for start in range(sublistcount):
            
            gap_insertion_sort(arr,start,sublistcount)
            
        sublistcount = sublistcount//2

-----------------------------------------------------------------------------------------

def gap_insertion_sort(arr,start,gap):
    
    for i in range(start+gap,len(arr),gap):
        
        currentvalue = arr[i]
        position = i
        
        while position >= gap and arr[position - gap] > arr[position]:
            
            arr[position] = arr[position-gap]
            position = position - gap
            
        arr[position] = currentvalue
---------------------------------------------------------------------------------------

## Merge Sort

def merge_sort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr)//2
        
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
                
            k += 1
                
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

------------------------------------------------------------------------------------------

## Quick sort

def quick_sort(arr):
    
    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):
    
    if first<last:
        
        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)


def partition(arr,first,last):
    
    pivotvalue = arr[first] 

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp


    return rightmark