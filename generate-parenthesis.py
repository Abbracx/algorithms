'''
Given an integer n, 
generate all the valid combinations of n pairs of parentheses.
'''

def is_valid(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0