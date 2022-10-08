def vowles(string):
    count = 0
    for char in string:
        for vowel in "aeiouAEIOU":
            if char == vowel:
                count += 1
    return count


s = input("Enter a string:\n")
print("String ", s, " has ", vowles(s), " vowels")
