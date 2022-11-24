import re


def ex1(input_text):
    return re.findall(r"\w+", input_text)


text = input("Give a text: ")
print(ex1(text))

"""
https://www.guru99.com/python-regular-expressions-complete-tutorial.html#2
"""
