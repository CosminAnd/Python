def is_vowel(c):
    return c in "AEIOUaeiou"


# Ex 3 with function

def all_vowels(s):
    list_of_vowels = []
    for c in s:
        if is_vowel(c):
            list_of_vowels.append(c)
    return list_of_vowels


print(all_vowels("Programming in Python is fun"))

# Ex 3 with anonymous function
anonymous_function = lambda s: [c for c in s if is_vowel(c)]

print(anonymous_function("Programming in Python is fun"))


# Ex 3 with list comprehensions
def all_vowels_v3(s):
    return [c for c in s if c in "AEIOUaeiou"]


print(all_vowels_v3("Programming in Python is fun"))

# Ex 3 with filtter
def all_vowels_v4(s):
    result = filter(lambda s: is_vowel(s), s)
    return list(result)

print(all_vowels_v4("Programming in Python is fun"))
