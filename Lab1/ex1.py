def find_gcd(x, y):
    while y:
        r = x % y
        x = y
        y = r

    return x


l = [int(x) for x in input("Enter values: ").split()]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)
