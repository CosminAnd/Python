def number(text):
    i = 0
    str_len = len(text)
    while i < str_len:
        if text[i].isdigit():
            first_number = ""
            while i < str_len and text[i].isdigit():
                first_number += text[i]
                i += 1
            else:
                print(int(first_number))
            break
        i += 1
    else:
        print(text + "\nhas no numbers")


t = input("Enter text: ")
print(number(t))
