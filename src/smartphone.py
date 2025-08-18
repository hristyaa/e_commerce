from src.products import Product

class Smartphone(Product):

    def __init__(self, name, description, efficiency, model, memory, color, price, quantity):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self. memory = memory
        self. color = color

