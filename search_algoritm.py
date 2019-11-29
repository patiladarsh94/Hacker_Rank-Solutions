
#Search Algorith implementation
'''
Linear Search

    Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    If x matches with an element, return the index.
    If x doesn’t match with any of elements, return -1.'''

import math
def linear_search(Search_list,search_element):

    for i in range (0,len(Search_list)-1):
        if Search_list[i]==search_element:
            return i
    return -1
  

'''
Binary Search      
We basically ignore half of the elements just after one comparison.
    Compare x with the middle element.
    If x matches with middle element, we return the mid index.
    Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
    Else (x is smaller) recur for the left half.'''

def binary_search(Search_list,search_element,low,high):
    if high>=low:
        mid=(low+high)//2
        if search_element > Search_list[mid]:
            return binary_search(Search_list,search_element,mid+1,high)
        elif search_element < Search_list[mid]:
            return binary_search(Search_list,search_element,low,mid-1)
        else:
            return Search_list.index(search_element)
    else:
        return -1


'''
Jump Search
For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0], 
arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear search operation
 from the index km to find the element x.

Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). 
Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the
block size to be jumped is 4.'''

def jump_search(Search_list,search_element):
    
    length=len(Search_list)
    jump=math.sqrt(length)
    prev=0
    while (Search_list[int(min(jump,length)-1)]<search_element):
        prev=jump
        jump+=math.sqrt(length)
        if prev>=length:
            return -1
    while prev<=length:
        if Search_list[int(prev)]==search_element:
            return int(prev)
        else:
            prev+=1
    return -1

if __name__ == '__main__':
    Search_list=[ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
    search_element=55
    low=0
    high=len(Search_list)-1
    jump=3
    result=jump_search(Search_list,search_element)
    if result==-1:
        print("Element not found in Search_list")
    else:
        print("Element is present at index {}".format(result))
