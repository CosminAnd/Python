import re
import pprint


def ex4(path, attrs):
    rez = []
    f = open(path, "r")
    data = f.read()
    reg = r"(<(\w+)"
    for key, value in attrs.items():
        reg += " {key}=\"{value}\"".format(key=key, value=value)
    reg += r">[^</\2>]*</\2>)"
    for i in re.findall(reg, data):
        rez.append(i[0])

    return rez


pprint.pp(ex4("test.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
