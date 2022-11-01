import os


def callback(exception):
    print(str(exception), type(exception))


def ex6(target, to_search):
    if os.path.isfile(target):
        try:
            if to_search in open(target, "r").read():
                return [os.path.abspath(target)]
        except Exception as e:
            callback(e)
    try:
        if not os.path.isdir(target):
            raise ValueError(target + ' este un path invalid pentru un fisier sau un director')
        to_return = []
        for root, directories, files in os.walk(target):
            for file_name in files:
                try:
                    if to_search in open(os.path.join(root, file_name), "r").read():
                        to_return.append(os.path.abspath(os.path.join(root, file_name)))
                except Exception as e:
                    callback(e)
        return to_return
    except Exception as e:
        callback(e)

# exemplu fisier
# print(ex6("test", "ana"))

# exemplu director
# print(ex6(".", "ana"))

# exemplu path invalid
# print(ex6('d:aa', 'ana'))
