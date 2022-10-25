def equals(dict1, dict2, depth):
    if type(dict1) == type(dict2):
        if type(dict1) is dict:
            same = True
            differences = []
            for label1, label2 in zip(sorted(dict1.keys()), sorted(dict2.keys())):
                if label1 != label2:
                    same = False
                    differences.append((label1, label2, "depth = " + str(depth), "different keys"))
                    continue
                is_equal = equals(dict1[label1], dict2[label1], depth + 1)
                if not is_equal[0]:
                    same = False
                    differences.append(is_equal[1])
            else:
                return same, differences
        if dict1 != dict2:
            return False, [(dict1, dict2, "depth = " + str(depth), "are not equal")]
        else:
            return True, []
    else:
        return False, [(dict1, dict2, "depth = " + str(depth), "different type")]


def ex3(dict1: dict, dict2: dict):
    return equals(dict1, dict2, 0)

print(ex3(
    {'a': {'b': 0}, 's': (2, 3), '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1},
    {'a': {'a': 3}, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
))
