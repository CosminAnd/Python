from itertools import zip_longest


def ex10(*lists):
    tupl = zip_longest(*lists, fillvalue=None)  #pentru cazul in care listele nu au aceeasi lungime
    return list(tupl)


x = [1, 2, 3]
y = [5, 6, 7]
z = ["a", "b", "c", "d"]
print(ex10(x, y, z))

"""
https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length?fbclid=IwAR3VBEeZEw_ua7R0X4crd_lac7E4_64Q0PQOdjr0dCt5lJMHSl5tYzlVvlU
"""