import os


def ex1(path):
    try:
        rez = set()
        for f in os.listdir(path):
            if os.path.isfile(f) and os.path.splitext(f)[-1].startswith("."):
                rez.add(os.path.splitext(f)[-1][1:])
        rez = list(rez)
        return sorted(rez)
    except Exception as e:
        return str(e), type(e)


print(ex1(".eeqw"))
