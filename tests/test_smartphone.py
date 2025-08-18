import pytest


def test_smartphone_init(product_smartphone_1):
    """Проверка инициализации класса Smartphone"""
    assert product_smartphone_1.name == "Iphone 15"
    assert product_smartphone_1.description == "512GB, Gray space"
    assert product_smartphone_1.price == 210000.0
    assert product_smartphone_1.quantity == 8
    assert product_smartphone_1.efficiency == 98.2
    assert product_smartphone_1.model == "15"
    assert product_smartphone_1.memory == 512
    assert product_smartphone_1.color == "Gray space"


def test_smartphone_add(product_smartphone_1, product_smartphone_2):
    """Проверка сложения товаров из одного класса"""
    assert product_smartphone_1 + product_smartphone_2 == 2114000.0


def test_smartphone_add_error(product_smartphone_1):
    """Проверка сложения товаров из разных классов"""
    with pytest.raises(TypeError):
        assert product_smartphone_1 + 10000


def test_smartphone_add_error_1(product_lawn_grass_1, product_smartphone_1):
    """Проверка сложения товаров из разных классов (смартфона и травы газонной)"""
    with pytest.raises(TypeError):
        assert product_lawn_grass_1 + product_smartphone_1
