def compose(notes, moves, start):
    rez = [notes[start]]
    for index in moves:
        start += index
        if start >= len(notes):
            start -= len(notes)
        if start < 0:
            start = len(notes) + start
        rez.append(notes[start])
    return rez


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2
print(compose(notes, moves, start))