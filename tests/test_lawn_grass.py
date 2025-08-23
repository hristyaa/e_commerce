import pytest


def test_lawn_grass_init(product_lawn_grass_1):
    """Проверка инициализации класса LawnGrass"""
    assert product_lawn_grass_1.name == "Газонная трава"
    assert product_lawn_grass_1.description == "Элитная трава для газона"
    assert product_lawn_grass_1.price == 500.0
    assert product_lawn_grass_1.quantity == 20
    assert product_lawn_grass_1.country == "Россия"
    assert product_lawn_grass_1.germination_period == "7 дней"
    assert product_lawn_grass_1.color == "Зеленый"


def test_lawn_grass_add(product_lawn_grass_1, product_lawn_grass_2):
    """Проверка сложения товаров из одного класса"""
    assert product_lawn_grass_1 + product_lawn_grass_2 == 16750.0


def test_lawn_grass_add_error(product_lawn_grass_1):
    """Проверка сложения товаров из разных классов"""
    with pytest.raises(TypeError):
        assert product_lawn_grass_1 + 10000


def test_lawn_grass_add_error_1(product_lawn_grass_1, product_smartphone_1):
    """Проверка сложения товаров из разных классов (смартфона и травы газонной)"""
    with pytest.raises(TypeError):
        assert product_lawn_grass_1 + product_smartphone_1
