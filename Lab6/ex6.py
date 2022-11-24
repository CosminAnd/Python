import re


def ex6(input_text):
    r = re.split(r"[^a-zA-Z0-9]", input_text)
    rez = ""
    for word in r:
        aux = ""
        if re.match(r"[aeiouAEIOU].*[aeiouAEIOU]$", word):
            for i in range(0, len(word)):
                if i % 2 == 1:
                    aux = aux + "*"
                else:
                    aux = aux + word[i]
        else:
            aux = word
        rez += aux + " "
    return rez


print(ex6("Ana are mere si alte chestii"))
