'''
Given an array of integers arr and an
integer k, find the kth largest element.

1 <= k <= arr

complexity:
T(n,k) = (k-1) * 2n + n
T(n,k) = 2kn - n = O(kn)
'''

def kth_largest_element(arr, k):
    return sorted(arr)[-k]


# T(n,k) = (k-1) * 2n + n
# T(n,k) = 2kn - n = O(kn)
def kth_largest_element2(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)


# T(n,k) = O(nlogn) + O(1) = O(nlogn)
def kth_largest_element3(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n - k]


arr = [4,2,9,7,5,6,7,1,3]
k = 4

result = kth_largest_element3(arr, k)

print(result)

