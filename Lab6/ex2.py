import re


def ex2(regex, text, x):
    rez = []
    for i in re.findall(regex, text):
        if len(i) == x:
            rez.append(i)
    return rez


print(ex2(r"\w+", "text, ana, are mere", 3))
