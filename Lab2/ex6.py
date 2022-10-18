def ex_6(*lists, x: int):
    reunited_lists = []
    rez = set() #no dupplicates
    for i in lists:
        reunited_lists += i
    for i in reunited_lists:
        if reunited_lists.count(i) == x:
            rez.add(i)
    return list(rez)

print(ex_6([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x=2))