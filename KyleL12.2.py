def sum(n):
    if n == 0:
        return 0
    print(n)
    return n + sum(n - 1)

def main():
    sum(5)


main()
