s1 = input("Enter string:")
s2 = ""

for c in s1:
    if c.isupper():
        s2 = s2 + '_'
        s2 = s2 + c.lower()
    else:
        s2 = s2 + c
else:
    s2 = s2[1:]  # se pune un "_" la inceput, se elimina
    print(s2)
