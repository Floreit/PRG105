"""""
def sum(n, z):

    sum = n









def main():
    print()
    n = [1,2,3,4,5,6,7,8,9,10]
    sum(n, 1)






main()
"""

# range sum


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# get sum of indeces 2 - 5
    my_sum = range_sum(numbers, 1, 5)
    print('The sum of items 2 through 5 is:', my_sum)


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)
main()


