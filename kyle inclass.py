import random


class Coin:
    def __init__(self):
        self.__side_up = 'heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__side_up = "heads"
        else:
            self.__side_up = 'tales'

    def get_side_up(self):
        return self.__side_up


coin = Coin()
heads = 0
tails = 0
for x in range(50):
    coin.toss()
    if coin.get_side_up() == "heads":
        heads = heads + 1
    else:
        tails = tails + 1

print("The number of times tails has been called: ", tails, "The number of times heads has been called is: ", heads)
