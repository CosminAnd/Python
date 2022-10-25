def ex9(*positions, **arguments): # ** -> operator pt a specifica tratarea ca dictionar
    count = 0
    for p in positions:
        if p in arguments.values():
            count += 1
    return count

print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))