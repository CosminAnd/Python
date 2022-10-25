def loop(mapping):
    visited=[]
    current = 'start'
    rez= set()
    while True:
        if current in visited:
            return rez
        visited.append(current)
        current = mapping[current]
        rez.add(current)


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))