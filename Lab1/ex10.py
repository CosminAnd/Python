def num_of_space(text):
    num = 0
    text = str(text)
    return len(text.split())


text = input("Enter a text: ")
print(num_of_space(text))
