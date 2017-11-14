
def message(n):
    if n > 0:
        message(n - 1)
        print(n)


def main():
    x = int(input("please enter a number"))
    message(x)

main()
