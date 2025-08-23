from src.products import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация класса Smartphone (наследник класса Product)"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сумма полной стоимости товаров на складе"""
        if type(other) is Smartphone:
            cost_products = self.price * self.quantity + other.price * other.quantity
            return cost_products
        else:
            raise TypeError
