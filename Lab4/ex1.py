import os

def ex1 (path):
    return sorted({os.path.splitext(f)[1] for f in os.listdir(path)
                   if os.path.isfile(f) and os.path.splitext(f)[-1].startswith(".")})

print(ex1(os.path.join(".")))