def ex1(a, b):
    set_a = set(a)
    set_b = set(b)
    listt = []
    listt.append(set_a | set_b)  # reuniune

    listt.append(set_a & set_b)  # intersectie

    listt.append(set_a.difference(set_b))

    listt.append(set_b.difference(set_a))
    return listt


a = [1, 2, 3, 4, 8]
b = [5, 6, 7, 8]
print(ex1(a, b))
