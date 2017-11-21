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

    def set_chair(self, material):
        self.material = material

    def set_table(self, length):
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


class Desk(OfficeFurniture):
    location_of_drawers = " "
    number_drawers = 0
    def __init__(self):
        location_of_drawers = self.location_of_drawers
        number_drawers = self.number_drawers
