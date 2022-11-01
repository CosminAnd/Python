import os


def ex5(target, to_search):
    if os.path.isfile(target):
        if to_search in open(target, 'r').read():
            return [os.path.abspath(target)]
    elif os.path.isdir(target):
        rez = list()
        for root, directories, files in os.walk(target):
            rez += [os.path.abspath(os.path.join(root, file_name)) for file_name in files if
                    os.access(os.path.join(root, file_name), os.R_OK) and to_search in
                    open(os.path.join(root, file_name), "r").read()]
            return rez
    else:
        raise ValueError(target + ' este un path invalid pentru un fisier sau un director')

# exemplu fisier
# print(ex5("test", "ana"))

# exemplu director
# print(ex5(".", "ana"))

# exemplu path invalid
# print(ex5('d:aa', 'ana'))


"""
https://www.geeksforgeeks.org/python-os-access-method/
"""