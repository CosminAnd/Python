import re
import os


def ex8(path, regex):
    rez = []
    try:
        for root, dir, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if re.match(regex, file_path) and re.match(regex, open(file_path, 'r').read()):
                    rez.append(">>" + file_path)
                elif re.match(regex, file_path) or re.match(regex, open(file_path, 'r').read()):
                    rez.append(file)
    except Exception as e:
        print(e)
    return rez


print(ex8(".", ".*.*"))
