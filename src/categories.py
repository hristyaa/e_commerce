# from src.products import Product
class Category:
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


    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_str

    def add_product(self, product):
        '''Добавление товаров в категорию'''
        self.__products.append(product)
        Category.product_count += 1


# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
# print(category1.products)
# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# category1.add_product(product4)
# print(category1.products)
# print(category1.product_count)
#
# print(Category.products)


