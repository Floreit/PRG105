# function to do the recursion
def get_sum(piece):

    if len(piece) == 0:
        return 0
    else:

        return piece[0] + get_sum(piece[1:])

# main function
def main():
    numbers = [1, 2, 3, 4, 5]
    output = get_sum(numbers)
    print(output)
# calling main
main()
