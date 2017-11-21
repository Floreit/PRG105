# OfficeFurniture class, set and get mutators
class OfficeFurniture:
    category = " "
    material = " "
    length = 0
    width = 0
    height = 0
    price = 0

    def __init__(self):
        category = self.category
        material = self.material
        length = self.length
        width = self.width
        height = self.height
        price = self.price

    def set_category(self, category):
        self.category = category

    def set_material(self, material):
        self.material = material

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_price(self, price):
        self.price = price

    def get_category(self):
        return self.category

    def get_material(self):
        return self.material

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_price(self):
        return self.price
    # Returns information for the user to know what they just selected
    def return_information(self):
        print("Category: ", self.category)
        print("Material: ", self.material)
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Height: ", self.height)
        print("Price: ", self.price)

# Desk subclass of OfficeFurniture set and get mutetators


class Desk(OfficeFurniture):
    location_of_drawers = " "
    number_drawers = 0

    def __init__(self):
        location_of_drawers = self.location_of_drawers
        number_drawers = self.number_drawers

    def set_location_of_drawers(self, location):
        self.location_of_drawers = location

    def set_number_drawers(self, number):
        self.number_drawers = number

    def get_location_of_drawers(self):
        return self.location_of_drawers

    def get_number_drawers(self):
        return self.number_drawers
    # upgraded Return information to include the new selections for desk
    def return_information(self):
        print("Category: ", self.category)
        print("Material: ", self.material)
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Height: ", self.height)
        print("Price: ", self.price)
        print("Number Of Drawers: ", self.number_drawers)
        print("Location Of Drawers: ", self.location_of_drawers)

# Main to call and set everything, then get a call on what was selected
def main():
    table = OfficeFurniture()
    desk = Desk()
    table.set_category("Table")
    table.set_material('Wood')
    table.set_length(60)
    table.set_width(10)
    table.set_height(15)
    table.set_price(120)

    table.return_information()
    print(" ")
    desk.set_category("Desk")
    desk.set_material("Wood")
    desk.set_length(20)
    desk.set_width(30)
    desk.set_height(15)
    desk.set_price(200)
    desk.set_location_of_drawers("sides")
    desk.set_number_drawers(4)

    desk.return_information()

# Run Main
main()

