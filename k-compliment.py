def find_compliment(arr, target):
    i = 0
    j = len(arr) - 1
    arr = sorted(arr)
    possible_pairs = []

    while( i < j ):
        sum = arr[i] + arr[j]
        if sum == target:
            possible_pairs.append([arr[i], arr[j]])
            i, j = i+1, j-1
        elif sum < target:
            i += 1
        else:
            j -= 1
    return len(possible_pairs) and possible_pairs

arr = [2,4,1,3,5,6,7]
target = 5

print(find_compliment(arr, target))