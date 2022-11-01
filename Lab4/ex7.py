import os
import pprint


def ex7(path):
    try:
        if os.path.isdir(path):
            raise Exception("Path-ul este un director")
        else:
            return {
                "full_path": os.path.abspath(path),
                "file_size": os.path.getsize(path),
                "file_extension": os.path.splitext(path)[-1][1:],
                "can_read": os.access(path, os.R_OK),
                "can_write": os.access(path, os.W_OK),
            }
    except Exception as e:
        print(str(e), type(e))


pprint.pp(ex7("main.txt"))

"""
https://docs.python.org/3/library/pprint.html
"""
