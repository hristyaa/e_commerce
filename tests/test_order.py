from src.order import Order


def test_order_init(product):
    """Тестированеи инициализации класса Order"""
    order1 = Order(product, 5)
    assert order1.product.name == "Tefal 457"
    assert order1.product.price == 4999.99
    assert order1.quantity == 5


def test_order_str(product_smartphone_1):
    """Тест строкового отображения класса Order"""
    order = Order(product_smartphone_1, 5)
    assert str(order) == 'В заказе "Iphone 15" в количестве 5 шт'


def test_order_cost_product(product_lawn_grass_1):
    """Тест на подсчет стоимости товаров в заказе"""
    order = Order(product_lawn_grass_1, 2)
    assert order.cost_order == 1000.0
