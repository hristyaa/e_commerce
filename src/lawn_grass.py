from src.products import Product

class LawnGrass(Product):

    def __init__(self, name, description, country, germination_period, color, price, quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

