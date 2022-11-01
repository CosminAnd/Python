import os


def ex8(dir_path):
    try:
        if os.path.isfile(dir_path):
            raise Exception("path is file, not dir")
        return [os.path.abspath(f) for f in os.listdir(dir_path) if os.path.isfile(f)]
    except Exception as e:
        print(str(e), type(e))


print(ex8("."))
