class Items:
    def __init__(self, gold):
        self.gold = gold

    def set_gold(self, gold):
        self.gold = gold

    def add_gold(self, gold):
        self.gold = self.gold + gold

    def sub_gold(self, gold):
        self.gold = self.gold - gold

    def get_gold(self):
        return self.gold


def main():
    items = Items(0)
    condition = 1
    print("You find yourself inside of a abandoned mineshaft, naked, not even a loin to cover yourself \n"
          "You hear a mixture of screaming, of pain, fear, and pleasure, coming from 3 different locations")
    print("You come across 3 pathways, each leading to one of the 3 screams you hear, which pathway will you choose?")
    primary_choice = int(input("1) Path of pain \n2) Path of fear \n3) Path of pleasure\n"))

    while condition != 0:
        # Pathway of pain
        if primary_choice == 1:
            print(
                "As you walk down the pathway of pain, you run into a naked man, whom is missing an arm and leg, \n"
                "clutching onto a bag of gold coins muttering to himself, Just a little more before i can get out \n"
                "You sit here staring at the dying man wondering what to do")
            choice_aa = int(input(
                "1) Do you attack the man and take his bag of gold under the assumption that you will need this to get out?\n"
                "2) Do you ignore the muttering fool and move on towards the screams of pain?\n"
                "3) Do you wait patently for the man to die before you take his bag of gold?\n"))
            if choice_aa == 1:
                print(
                    "You chose to attack the unarmed naked man with nothing but your fist, but as you approach the\n"
                    "delirious dying man, you are confronted with a naked woman armed with a spear,\n"
                    "its the dying mans wife,\n"
                    "she realized your plan and she promptly stabs you, and returns to her dying husband,\n"
                    "you lay on the ground bleeding to death, regretting the choices you made, not just here but in life\n"
                    "overall")
                print("Game Over")
                condition = 0
            elif choice_aa == 2:
                print(
                    "You ignore the dying fool and continue down the pathway, as you look back you see a naked woman\n"
                    "armed with a spear approaching the dying man, she kneels down and hugs him, you think to yourself\n"
                    "that it was a good idea not to attack the dying man\n"
                    "You continue down your path, the more time passes the more the screams get louder,\n"
                    "you eventually come across a skeleton with a bag of gold larger than the dying man you passed up,\n"
                    "lucky!", items.add_gold(50))
                # Insert new if statement for one more path involving combat

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
                condition = 1
            else:
                print("Please enter 1-3 any other options will be ignored")

        # Pathway of fear
        elif primary_choice == 2:
            print("test")
        # Pathway of pleasure
        elif primary_choice == 3:
            print("Test")

        else:
            print("Please enter a number between 1 and 3, all else will repeat this message")
            primary_choice = int(input("1) Path of pain \n2) Path of fear \n3) Path of pleasure\n"))


main()
