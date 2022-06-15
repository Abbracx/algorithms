def is_palindrome(value):
    if type(value) != 'string':
        return str(value)[::-1] == str(value)
    if not value.strip(): return False
    return value[::-1] == value
    

print(is_palindrome('apple'))
print(is_palindrome(1221))
print(is_palindrome('ommo'))
print(is_palindrome(' '))