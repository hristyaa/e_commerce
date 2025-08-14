# from src.categories import Category


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое отображение класса Product"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, dict_product, list_products=None):
        """Добавление товара по параметрам товара из словаря"""
        if list_products is None:
            list_products = []
        name = dict_product["name"]
        description = dict_product["description"]
        price = dict_product["price"]
        quantity = dict_product["quantity"]
        for product in list_products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                elif price < product.price:
                    user_input = input(
                        f"Текущая цена товара {product.name} - {product.price} руб. Понизить цену?(y/n)\n"
                    ).lower()
                    if user_input == "y":
                        product.price = price

                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


# new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5}, [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 4),
#          Product("Iphone 15", "512GB, Gray space", 210000.0, 8)])
# print(new_product.name)
# print(new_product.description)
# print(new_product.price)
# print(new_product.quantity)
