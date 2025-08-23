from src.products import Product


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация класса LawnGrass (наследник класса Product)"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сумма полной стоимости товаров на складе"""
        if type(other) is LawnGrass:
            cost_products = self.price * self.quantity + other.price * other.quantity
            return cost_products
        else:
            raise TypeError
