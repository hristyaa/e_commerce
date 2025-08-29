from src.base_order import BaseOrder
# from src.smartphone import Smartphone
# from src.lawn_grass import LawnGrass
from src.exceptions import ZeroQuantityProduct
from src.products import Product


class Category(BaseOrder):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация класса Category"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Строковое отображение класса Category"""
        count_product = 0
        for product in self.__products:
            count_product += product.quantity

        return f"{self.name}, количество продуктов: {count_product} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product):
        """Добавление товаров в категорию"""
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise ZeroQuantityProduct("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantityProduct or ValueError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров в категории"""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0


# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
# print(category1.middle_price())
#
# category2= Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         []
#     )
# print(category2.middle_price())

# print(category1)
#
# print(category1.products)

# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 0)
# except ValueError as e:
#     print(f"Ошибка при создании товара: {e}")
#     product4 = None
# category1.add_product(product4)

# print(category1.products)
# print(category1.product_count)
#
# product5 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
# category1.add_product(product5)
# print()
# print(category1.products)
# product6 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
# category1.add_product(product6)
# print()
# print(category1.products)
# product7 = 'dlfkld'
# category1.add_product(product7)
#
# print()
# print(category1.products)
#
# print(Category.products)
# print(category1)
#
