def generate_fibonacci():
    return_list = [0, 1]
    for i in range(2, 1000):
        return_list.append(return_list[i - 2] + return_list[i - 1])
    return return_list[0:1000]


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs):
    fibonacci_sequence = generate_fibonacci(1000)
    try:
        if "filters" in kwargs.keys():
            for f in kwargs["filters"]:
                fibonacci_sequence = list(filter(f, fibonacci_sequence))
        if "offset" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[kwargs["offset"]:]
        if "limit" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[:kwargs["limit"]]
    except Exception as e:
        print("Error at processing:", e)
    return fibonacci_sequence


print(
    process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    )
)