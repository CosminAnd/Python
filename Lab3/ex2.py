def ex2 (string):
    dic = {}
    for i in sorted(string):
        dic.setdefault(i, string.count(i))
    print(dic)


ex2("Ana has apples.")