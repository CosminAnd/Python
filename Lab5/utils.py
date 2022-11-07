#Ex1 a)
def is_prime(x):
    if x == 2:
        return True
    if x < 2:
        return False
    if x % 2 == 0:
        return False
    for i in (2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def process_item(x):
    while not is_prime(x + 1):
        x += 1
    return x + 1


if __name__ == "__main__":
    try:
        x = int(input("Enter a number: "))
        print(process_item(x))
    except Exception as e:
        print(str(e), type(e))
