def fibo(n):
    Fibo = list()

    if n > 0:
        Fibo.append(1)
    if n > 1:
        Fibo.append(1)
    for i in range(2, n):
        Fibo.append(Fibo[i - 1] + Fibo[i - 2])

    return Fibo

x = int(input("Enter a value: "))
print(fibo(x))

