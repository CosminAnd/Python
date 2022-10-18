def div_by_x(string, x, flag):
    rez= set()
    if flag:
        for c in string:
            if ord(c)%x == 0:
                rez.add(c)
    else:
        for c in string:
            if ord(c)%x != 0:
                rez.add(c)

    rez = list(rez)
    return rez


#print(div_by_x("test", 2, False))

def ex8 (x=1, strings=[], flag =True ):
    rez = []
    for string in strings:
        rez.append(div_by_x(string, x, flag))
    return rez

print(ex8(2,["test", "hello", "lab002"], False))

