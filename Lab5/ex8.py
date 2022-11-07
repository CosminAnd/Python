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

