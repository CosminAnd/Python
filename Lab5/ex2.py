anonymous_function = lambda *args, **kwargs: sum(kwargs.values())


def my_function(*args, **kwargs):
    return sum(kwargs.values())


print(anonymous_function(1, 2, c=3, d=4))
print(my_function(1, 2, c=3, d=4))
