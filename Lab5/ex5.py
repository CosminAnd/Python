import numbers

"""
# pentru fiecare elemnet al listei se verifica tipul: daca este dictionare se cauta numerele printre chei si valori
def ex5(input_list):
    res = []
    for element in input_list:
        print(type(element))
        if type(element) == dict:
            for key, value in element.items():
                if isinstance(key, numbers.Number):
                    res.append(key)
                if isinstance(value, numbers.Number):
                    res.append(value)
        elif type(element) == list or type(element) == set:
            for i in element:
                if(isinstance(i, numbers.Number)):
                    res.append(i)
        else:
            if isinstance(element, numbers.Number):
                res.append(element)

    return res
"""


def ex5(input_list):
    res = []
    for element in input_list:
        if isinstance(element, numbers.Number):
            res.append(element)
    return res


print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
