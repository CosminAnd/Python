import re


def ex3(text, list_of_regex):
    for i in list_of_regex:
        rez = re.findall(i, text)
        if not len(rez) == 0:
            return rez


print(ex3("ana 1 mere 2 ceva, dada, %%%", [r"\d", r"\w+"]))


def ex3_v2(text, list_of_regex):
    rez = dict()
    for a in list_of_regex:
        rez[a] = re.findall(a, text)

    return rez


print(ex3_v2("ana 1 mere 2 ceva, dada, %%%", [r"\d", r"\w+"]))
