def operations(a, b):
    set_1 = set(a)
    set_2 = set(b)
    return list(set_1 | set_2), list(set_1 & set_2), list(set_1.difference(set_2)), list(set_2.difference(set_1))
                #reunion             intersection           a-b                             b-a

a=[1,2,3,4]
b=[5,6,7,8]
print(operations(a,b))