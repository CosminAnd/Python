def ex6(listt):
    return len(set(listt)), len(listt) - len(set(listt))


print(ex6([1, 2, 3, 4, 4, 4, 5, 8, 9]))
