"""
def ex6(input_list):
    res = []
    list_of_odd_numbers = []  # impare
    list_of_even_numbers = []  # pare
    for element in input_list:
        if element % 2:
            list_of_odd_numbers.append(element)
        else:
            list_of_even_numbers.append(element)
    for i in range(len(list_of_even_numbers)):
        res.append((list_of_even_numbers[i], list_of_odd_numbers[i]))

    return res
"""


def ex6(input_list):
    list_of_odd_numbers = [x for x in input_list if x % 2 == 1]  # impare
    list_of_even_numbers = [x for x in input_list if x % 2 == 0]  # pare
    return list(zip(list_of_even_numbers, list_of_odd_numbers))


print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
