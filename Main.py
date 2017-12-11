# importing random to be used in the combat and dice roll
import random

# class to hold the players gold, sword, and shield information, allows for setting, getting, values, adding and subbing values,
# of gold, sword, and shield


class Items:

    def __init__(self, gold, sword, shield):
        self.gold = gold
        self.sword = sword
        self.shield = shield

    def set_gold(self, gold):
        self.gold = gold

    def add_gold(self, gold):
        self.gold = self.gold + gold

    def sub_gold(self, gold):
        self.gold = self.gold - gold

    def get_gold(self):
        return self.gold

    def set_sword(self, sword):
        self.sword = sword

    def set_shield(self, shield):
        self.shield = shield

    def get_sword(self):
        return self.sword

    def get_shield(self):
        return self.shield

# Roll function for the gambling using a list to hold 2 variables from the while loop then adding them together then returning them


def roll():
    result = []

    x = 2
    while x != 0:
        cycle = random.randint(1, 11)
        result.append(cycle)
        x = x - 1
    end_result = result[0] + result[1]
    return end_result

# combat roll function that takes the items sword and shield as calls and adds points to the overall point


def combat(sword, shield):
    temp_holder = [0, 0]
    result = random.randint(1, 6)

# adding points if they have a sword1
    if sword == 1:
        temp_holder.insert(0, 2)
# adding points if they have a shield
    if shield == 1:
        temp_holder.insert(1, 2)

    random_result = temp_holder[0] + temp_holder[1]
    for num in temp_holder:
        random_result += num
    random_result = random_result + result
    return random_result

# main function where all the magic happens


def main():
    items = Items(0, 0, 0)
    condition = 1

    print("You find yourself inside of a abandoned mineshaft, naked, not even a loin to cover yourself \n"
          "You hear a mixture of screaming, of pain, fear, and pleasure, coming from 3 different locations")
    print("You walk down the pathway you took, you hear screams of pain in the distance, pondering to yourself what it\n"
          " is you are about to run into")

    print(
        "As you walk down the pathway, you run into a naked man, whom is missing an arm and leg, \n"
        "clutching onto a bag of gold coins muttering to himself, Just a little more before i can get out \n"
        "You sit here staring at the dying man wondering what to do")
    choice_aa = int(input(
        "1) Do you attack the man and take his bag of gold under the assumption that you will need this to get out?\n"
        "2) Do you ignore the muttering fool and move on towards the screams of pain?\n"
        "3) Do you wait patently for the man to die before you take his bag of gold?\n"))
    primary_loop = 1
    while primary_loop != 0:

            # dead end route
            if choice_aa == 1:
                print(
                    "You chose to attack the unarmed naked man with nothing but your fist, but as you approach the\n"
                    "delirious dying man, you are confronted with a naked woman armed with a spear,\n"
                    "its the dying mans wife,\n"
                    "she realized your plan and she promptly stabs you, and returns to her dying husband,\n"
                    "you lay on the ground bleeding to death, regretting the choices you made, not just here but in life\n"
                    "overall")
                print("Game Over")
                primary_loop = 0
                # Correct route
            elif choice_aa == 2:
                print(
                    "You ignore the dying fool and continue down the pathway, as you look back you see a naked woman\n"
                    "armed with a spear approaching the dying man, she kneels down and hugs him, you think to yourself\n"
                    "that it was a good idea not to attack the dying man\n"
                    "You continue down your path, the more time passes the more the screams get louder,\n"
                    "you eventually come across a skeleton with a bag of gold larger than the dying man you passed up,\n"
                    "lucky!", items.add_gold(50))
                print(
                            "You are approached by a shady looking man in rags, the man asks you if you\n"
                            "wish to buy a sword for 50 gold coins, a shield for 50 gold coins,\n"
                            "or both for a discount of 75 gold coins")
                while condition != 0:
                    # setting the var end to get random generated number, using sword and shield to add points to that number
                    end = combat(items.get_sword(), items.get_shield())
                    print("While you debate what you wish to buy, the man in rags informs you of a group of armed thugs ahead,\n"
                          " and that you should definitely arm yourself up before proceeding, your options are as follows")
                    choice_ab = int(input("1) for sword\n2) for shield\n3) for both\n4) if you wish to spend 5 gold,\n"
                                          "roll some dice and win 50 gold"))
                    # Game over sword only choice
                    if choice_ab == 1 and items.get_gold() >= 50:
                        items.set_sword(1)
                        if items.get_gold() < 50:
                            print("you have wasted all of your gold coins based on your bad luck that landed you in this\n"
                                  "place in the first place, so now your broke, no armor or weapons, all you got to your\n"
                                  "name is your first and your horrible luck, you dash forward in hopes of finding better\n"
                                  "luck, it does not, murphy just smiles at your misfortune as you squandered all of your\n"
                                  "hope, and now, as if to put you out of your misery, find yourself surrounded by rats\n"
                                  "lots of rats, large starving rats, they jump onto you, biting you, but you are unable\n"
                                  "to do anything about it and are eaten alive")
                        # Game over if winning the combat roll
                        if end >= 6:
                            print("You bought yourself a sword, too cheap to buy the shield as well, you set off to find a way\n"
                                  "out, as you walk you hear laughter in the distance, 3 guys are huddling around each other,\n"
                                  "in between the 3 men is a body of a dead man and female, none of them are paying attention\n"
                                  "to you, so you decide to strike the first man in the throat from behind, pull it out and\n"
                                  "manage to connect the slashing of your hard earned sword into the unfortunate souls neck\n"
                                  "as you try to get your sword out of the neck of the previous person, the third man manages\n"
                                  "to get a decent slash onto you stretching the entirety of your chest, you kill the third man\n"
                                  "before collapsing to the ground, struggling to stay awake, you eventually pass away from blood\n"
                                  "loss")
                            condition = 0
                            primary_loop = 0
                        # Game over if losing the combat roll
                        elif end < 6:
                            print("You got your sword, and set out to find a way out, you run and run until you suddenly stop,\n"
                                  "a very large fishing net has been thrown onto you and you cannot move, the more you struggle\n"
                                  "the more the barbs dig into your skin as you hear laughter from the 3 men approaching you,\n"
                                  "they proceed to methodically stab you over and over with a spear until you lose consciousness")
                            condition = 0
                            primary_loop = 0
                        # Shield choice
                    elif choice_ab == 2 and items.get_gold() >= 50:
                        items.set_shield(1)
                        # Game over choice for the shield winning combat roll
                        if end >= 6:
                            print("you decide to buy the shield, you run through the pathway until you come across a person who\n"
                                  "is taking a leak, you realize this is one of the thugs the man in rags before was talking about\n"
                                  "so you decide to take your shield, and bash it over his head until he stops moving, you take\n"
                                  "a step back, only to feel a sharp pain in your back, the poor sod whose head you turned into\n"
                                  "a bloody mess's friends, have come to see what the commotion was, and in the process stabbed\n"
                                  "you to death")
                            condition = 0
                            primary_loop = 0
                        # Game over shield losing combat roll
                        if end < 6:
                            print("With your shining new shield you start running towards what you thought was light\n"
                                  "when you reached this magical light, you realize that it was merely an artificial light\n"
                                  "on top of a prison looking complex, you see arrows flying your way which is blocked\n"
                                  "by your shield, you hear footsteps to your side, you see around 6 people in heavy\n"
                                  "armor surrounding you, they quickly subdue you, take your shield away and toss you\n"
                                  "in the prison where you spend the rest of your life doing hard labor")
                            condition = 0
                            primary_loop = 0

                    elif choice_ab == 3 and items.get_gold() >= 75:
                        items.set_sword(1)
                        items.set_shield(1)
                        # Game over sword and shield won combat roll

                        if end >= 6:
                            print(
                                "You manage to scrape by and buy both the sword and shield, neat, you go down the pathway a bit\n"
                                "before you come across a giant spider, being an arachnophobe your entire life, you decide that this is\n"
                                "not the pathway you will be taking, turn around, but unfortunately, you ran into some more spiders\n"
                                "around this point, at this point you let go of all senses and defecate yourself, all while\n"
                                "the spiders stab you over and over until you black out")
                        condition = 0
                        primary_loop = 0
                        # Game over sword and shield lost combat roll
                        if end < 6:
                            print("You won gambling, now its time to gamble your life in your attempt to get out of this\n"
                                  "place, filled with energy, you run down this pathway with hope filling your eyes\n"
                                  "only to come across a giant wall in your way, you ponder how to get through this\n"
                                  "your sword and shield are useless in this position until you can figure out how\n"
                                  "to get over this giant wall, you eventually decide to take your frustration out\n"
                                  "on some oranges as you wrack your brain trying to find a way through, while \n"
                                  "mercilessly pounding on this orange, it randomly explodes thrusting you\n"
                                  "into a pit filled with spikes, oops")
                            condition = 0
                            primary_loop = 0

                            # Gambling option to be able to afford one or the other

                    elif choice_ab == 4:
                        print("You decide to test your luck and gamble some of your 'hard earned' gold in order to afford both\n"
                              "the shield and sword ")
                        if roll() >= 7:
                            items.add_gold(50)
                            print("You hit the jack pot and made out with 50 gold, lucky!")
                        if roll() < 7:
                            items.sub_gold(5)
                            print("You just lost 5 gold, better luck next time")
                    else:
                            print("Either you entered the incorrect number, or you do not have enough gold for the selection\n")

            # Dead end choice
            elif choice_aa == 3:
                print(
                    "You decide to wait for the man to die first before stealing his gold, but while waiting you see a\n"
                    "naked woman with a spear approaching, she spots you, stares at you for a moment before charging at\n"
                    "you full speed, spear readied, you turn 180 and run as fast as you can but all those years of\n"
                    "eating hamburgers and doughnuts are finally starting to catch up to you, speaking of that,\n"
                    "you feel a burning sensation in your lower abdomen,\n"
                    "her spear has pierced through you, as she pulls the spear out you can hear her berate you for trying\n"
                    "to harm her husband. ")
                print("Game over")
                primary_loop = 0

            else:
                print("Please enter 1-3 any other options will be ignored")
                choice_aa = int(input(
                                        "1) Do you attack the man and take his bag of gold under the assumption that you will need this to get out?\n"
                                        "2) Do you ignore the muttering fool and move on towards the screams of pain?\n"
                                        "3) Do you wait patently for the man to die before you take his bag of gold?\n"))


main()
