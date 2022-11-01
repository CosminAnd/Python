import os


def ex2(dir, fis):
    try:
        fd = open(fis, "w")
        for f in os.listdir(dir):
            if os.path.isfile(f) and (f.startswith("a") or f.startswith("A")):
                fd.write(os.path.abspath(f) + os.linesep)
    except Exception as e:
        print(str(e), type(e))


ex2(".", "ex2.txt")
