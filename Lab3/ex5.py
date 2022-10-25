def validate_dict(set_of_tuples, dict):
    for rule in set_of_tuples:
        value = dict.get(rule[0])  # valoarea pentru cheia 'rule[0]'
        if value is None:  # cheia nu se gaseste in dictionar
            return False
        if not value.startswith(rule[1]) or not value.endswith(rule[3]) or not rule[2] in value or value.startswith(
                rule[2]) or value.endswith(rule[2]):
            return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
