# Ex8 a)
def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(functions):
    function_string = """
def new_function(*args, **kwargs):
    print("Arguments are:", *args)
    print("Key arguments are:", **kwargs)
    return functions(*args,**kwargs)"""
    # print(function_string)
    globals()["functions"] = functions
    exec(function_string, globals())
    return new_function


augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))


# Ex8 b)
def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    function_string = """
def new_function(number):
    return 2*functions(number)"""
    # print(function_string)
    globals()["functions"] = function
    exec(function_string, globals())
    return new_function


augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))


# Ex8 c)
def add_numbers(a, b):
    return a + b
