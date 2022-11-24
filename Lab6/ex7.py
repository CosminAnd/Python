import re


def is_bisect(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def control_number(cnp):
    constant = "279146358279"
    sum = 0
    for i in range(0, 12):
        sum += int(cnp[i]) * int(constant[i])
    r = sum % 11
    if r == 10:
        r = 1
    return r == int(cnp[12])


def ex7(cnp):
    year = 0
    r = re.compile('[1-9][0-9]{2}(0[0-9]|1[0-2])((0[1-9]|[1-2][0-9])|3[0-1])[0-9]{6}')
    # verificare numar de caractere
    if not r.match(cnp):
        return False
    first_number = int(cnp[0])
    if first_number == 1 or first_number == 2:
        year = 1900 + int(cnp[1] + cnp[2])
    elif first_number == 3 or first_number == 4:
        year = 1800 + int(cnp[1] + cnp[2])
    elif first_number == 5 or first_number == 6:
        year = 2000 + int(cnp[1] + cnp[2])
    month = int(cnp[3] + cnp[4])
    day = int(cnp[5] + cnp[6])
    sector = int(cnp[7] + cnp[8])
    secvential_number = int(cnp[9] + cnp[10] + cnp[11])
    # verificare luna
    if month > 12 or month < 1:
        return False
    # verificare zile in functie de luna
    if month == 2:
        if is_bisect(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    else:
        if day < 1 or day > 30:
            return False
    if sector not in range(1, 53):
        return False
    if secvential_number not in range(1, 1000):
        return False
    if not control_number(cnp):
        return False
    return True


if ex7(input("Type a cnp: ")):
    print("CNP valid")
else:
    print("CNP invalid")


"""
https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)
"""

