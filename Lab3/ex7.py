def operations(set1, set2, op):
    stringg = str(str(set1) + " " + op + " " + str(set2))
    rez = set()
    if op == '|':
        rez = set1 | set2
        return stringg, rez
    elif op == '&':
        rez = set1 & set2
        return stringg, rez
    else:
        rez = set1 - set2
        return stringg, rez


def ex7(*sets):
    dictionary = dict()
    for i in range(len(sets)-1):
        for j in range(i+1, len(sets)):
            key, value = (operations(sets[i], sets[j], '|'))
            dictionary.setdefault(key, value)

            key, value = operations(sets[i], sets[j], '&')
            dictionary.setdefault(key, value)

            key, value = operations(sets[i], sets[j], '-')
            dictionary.setdefault(key, value)

            key, value = operations(sets[j], sets[i], '-')
            dictionary.setdefault(key, value)
    for key, value in dictionary.items():
        print(key, ":",  value)

ex7({1, 2}, {2, 3})

