from utils import process_item

#Ex1 b)
if __name__ == "__main__":
    while True:
        x = input("Enter a input: ")
        if x == 'q':
            exit()
        try:
            x = int(x)
            print(process_item(x))
        except Exception as e:
            print(str(e), type(e))
