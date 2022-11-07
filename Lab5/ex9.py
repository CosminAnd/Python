import pprint


def ex9(pairs):
    res = []
    for pair in pairs:
        first, second = pair
        d = dict()
        d["sum"] = first + second
        d["prod"] = first * second
        d["pow"] = first ** second
        res.append(d)
    return res


pprint.pp(ex9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
