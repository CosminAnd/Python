def is_palindrome(x):
    x= str(x)
    return x == x[::-1]

def ex7(list):
    count = 0
    max_palindrom = 0
    for i in list[::-1]:
        if is_palindrome(i):
            count+=1
            if(i > max_palindrom):
                max_palindrom = i
    return (count, max_palindrom)

print(ex7([121, 333, 41234, 5567888, 9009]))

