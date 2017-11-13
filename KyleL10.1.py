class PersonalData:
    name = ' '
    address = " "
    age = 0.0
    phone = ' '

    def __init__(self):
        name = ' '
        address = " "
        age = 0.0
        phone = ' '

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    def set_name(self, n):
        self.name = n

    def set_address(self, a):
        self.address = a

    def set_age(self, ag):
        self.age = ag

    def set_phone(self, p):
        self.phone = p


def main():

    kyle = PersonalData()
    rebecca = PersonalData()
    alex = PersonalData()

    kyle.set_name("kyle")
    kyle.set_address("1234 idk drive")
    kyle.set_age(30)
    kyle.set_phone("847-123-4567")
    rebecca.set_name("rebecca")
    rebecca.set_address("5678 idc drive")
    rebecca.set_age(29)
    rebecca.set_phone("815-456-7890")
    alex.set_name("alex")
    alex.set_address("9012 idwk drive")
    alex.set_age(28)
    alex.set_phone("815-758-9443")

    print("name:", kyle.get_name(), "address:", kyle.get_address(), "age:", kyle.get_age(), "Phone:", kyle.get_phone(), sep=' ')
    print("name:", rebecca.get_name(), "address:", rebecca.get_address(), "age:", rebecca.get_age(), "Phone:", rebecca.get_phone(), sep=' ')
    print("name:", alex.get_name(), "address:", alex.get_address(), "age:", alex.get_age(), "Phone:", alex.get_phone(), sep=' ')




main()
