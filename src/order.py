# from src.products import Product
from src.base_order import BaseOrder


class Order(BaseOrder):

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        """Строковое отображение класса Order"""
        return f'В заказе "{self.product.name}" в количестве {self.quantity} шт'

    @property
    def cost_order(self):
        """Итоговая стоимость товаров в заказе"""
        return self.product.price * self.quantity


# product1 = Product('Телефон', 'Смартфон', 1000, 16)
#
# order1 = Order(product1, 4)
#
# print(order1.product)
# print(order1.quantity)
# print(order1.cost_order)
# print(order1)
