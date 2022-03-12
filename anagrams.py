'''
Two strings are anagrams if they are made up of same characters with same frequencies.
'''

def is_anagram(s1, s2):

    if len(s1) != len(s2): return False

    freq1 = {}
    freq2 = {}

    #calculate frequesncies of characters both in s1 and s2
    for char in s1:
        if char in freq1.keys():
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    for char in s2:
        if char in freq2.keys():
            freq2[char] =+ 1
        else:
            freq2[char] = 1

    # match frequencies for char in freq1 and freq2
    for key in freq1.keys():
        if key not in freq2.keys() or freq1[key] != freq2[key]:  return False
    return True

'''
Two anagrams have the same lexicographical sorted string.
e.g: 
sorted(salesman) == aelmnss
sorted(nameless) == aelmnss
'''
def isAnagram(s1, s2):
    if len(s1) != len(s2): return False
    return sorted(s1) == sorted(s2)

print(is_anagram('danger','garden'))
print(isAnagram('danger','garden'))
