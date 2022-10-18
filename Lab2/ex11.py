def ex11 (list=[()]):
    list.sort(key=lambda x: x[1][2]) #al treilea caracter din al doilea elem al tuplei
    return list


print(ex11([('abc', 'bcd'), ('abc', 'zza')]))