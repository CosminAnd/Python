def is_letter(c):
    if c >= 'a' and c <= 'z':
        return True
    return False


def most_common_letter(string):
    string = str.lower(string)
    letter = ""
    number = 0
    for i in string:
        if is_letter(i):
            if string.count(i) > number:
                letter = i
                number = string.count(i)
    return letter


string = input()
print(most_common_letter(string))
