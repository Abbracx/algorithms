def rm_par(combination):
    stack = []
    cleaned = ''
    for par in combination:
        if par == '(':
            stack.append(par)
        else: 
            if par == ')':
                stack.pop()
            elif len(stack) == 0:
                cleaned += par
    return cleaned


print(rm_par('abcd(e(fg)h)ijklm'))
