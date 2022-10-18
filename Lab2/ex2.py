def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in (2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def ex_2(vect):
    rez=list()
    for i in vect:
        if is_prime(i):
            rez.append(i)
    return rez

print(ex_2([3, 76, 1234, 83, 24 ,987, 45, 77, 9376, 435, 61, 123]))
