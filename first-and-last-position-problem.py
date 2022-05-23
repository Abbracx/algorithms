'''
Given a sorted array of integers arr and integer target,
find the index of the first and last position of target in arr.
if target cant be found in arr return  [-1,-1].
T(n) = O(n)
S(n) = O(1)
   
'''

def first_and_last(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            start = i 
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


arr = [2,4,5,5,5,5,5,7,9,9]
result = first_and_last(arr, 5)
print(result)