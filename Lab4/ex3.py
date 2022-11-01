import os
import pprint


def ex3(my_path):
    if os.path.isfile(my_path):
        fd = open(my_path, 'r')
        line = fd.read()
        return line[-20::]
    extensions_set = set()
    extensions = list()
    rez = list()
    if os.path.isdir(my_path):
        for root, dir, files in os.walk(my_path):
            for file_name in files:
                if os.path.isfile(os.path.join(root, file_name)):
                    extension = os.path.splitext(str(file_name))[1][1:]
                    extensions_set.add(extension)
                    extensions.append(extension)
        for extension in extensions_set:
            rez.append((extension, extensions.count(extension)))
        return sorted(rez, key=lambda x: x[1], reverse=True)


pprint.pp(ex3("."))

"""
https://docs.python.org/3/library/pprint.html
"""
