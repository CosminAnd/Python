import sys
import os


def ex4():
    directory_path = sys.argv[1]
    return sorted({os.path.splitext(f)[-1][1:] for f in os.listdir(directory_path) if
                   os.path.isfile(f) and os.path.splitext(f)[-1].startswith(".")})

def ex_4():
    directory_path = input("Dati un input: ")
    return sorted({os.path.splitext(f)[-1][1:] for f in os.listdir(directory_path) if
                   os.path.isfile(f) and os.path.splitext(f)[-1].startswith(".")})


print(ex4())
# print(ex_4())
