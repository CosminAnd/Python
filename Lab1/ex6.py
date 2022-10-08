def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:  # start:end:step
        return True
    return False


x = int(input())
print(is_palindrome(x))
