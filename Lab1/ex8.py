def bits_counter(x):
    x=bin(x)
    return x.count("1")

x=input()
x=int(x)

print("The number has: ", bits_counter(x), " bits with value 1")