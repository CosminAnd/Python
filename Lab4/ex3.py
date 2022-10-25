import os

def ex3(my_path):
    if os.path.isfile(my_path):
        fd = open(my_path, 'r')
        line = fd.read()
        return line[-20::]
    extensions = set()
    if os.path.isdir(my_path):
        # trebuie terminat aici
        for root, dir, file in os.walk(my_path):
            if os.path.isfile(file):
                extensions.add(os.path.splitext(file)[1])
        print(extensions)






print(ex3("main.txt"))