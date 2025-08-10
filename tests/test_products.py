from unittest.mock import patch

from src.products import Product


def test_products(product):
    assert product.name == "Tefal 457"
    assert product.description == "Black, 2000W"
    assert product.price == 4999.99
    assert product.quantity == 8


def test_price_property(product):
    assert product.price == 4999.99


def test_price_setter(capsys, product):
    """Тест на изменение цены товара"""
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = -147
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = 147
    assert product.price == 147


def test_new_product(dict_product):
    """Тест на добавление товара по параметрам товара из словаря"""
    new_product = Product.new_product(dict_product)
    assert new_product.name == "Tefal 457"
    assert new_product.description == "Black, 2000W"
    assert new_product.price == 5999.99
    assert new_product.quantity == 4


def test_new_product_in_list_products(dict_product, second_category):
    """Тест при добавлении товара с одинаковым названием, цена нового выше старой"""
    list_products = second_category.products_in_list
    new_product = Product.new_product(dict_product, list_products)
    assert new_product.name == "Tefal 457"
    assert new_product.description == "Black, 2000W"
    assert new_product.price == 5999.99
    assert new_product.quantity == 12


@patch("builtins.input", return_value="y")
def test_new_product_in_list_products_price_is_lower_y(mock_input, dict_product_price_is_lower, second_category):
    """Тест при добавлении товара с одинаковым названием, цена нового ниже старой, согласие на снижение цены"""
    list_products = second_category.products_in_list
    new_product = Product.new_product(dict_product_price_is_lower, list_products)

    assert new_product.name == "Tefal 457"
    assert new_product.description == "Black, 2000W"
    assert new_product.price == 3999.99
    assert new_product.quantity == 11


@patch("builtins.input", return_value="n")
def test_new_product_in_list_products_lower_price_n(mock_input, dict_product_price_is_lower, second_category):
    """Тест при добавлении товара с одинаковым названием, цена нового ниже старой, отказ от снижения"""
    list_products = second_category.products_in_list
    new_product = Product.new_product(dict_product_price_is_lower, list_products)

    assert new_product.name == "Tefal 457"
    assert new_product.description == "Black, 2000W"
    assert new_product.price == 4500
    assert new_product.quantity == 11


@patch("builtins.input", return_value="dfvd")
def test_new_product_in_list_products_lower_price_any_input(mock_input, dict_product_price_is_lower, second_category):
    """
    Тест при добавлении товара с одинаковым названием,
    цена нового ниже старой, отказ от снижения (любой ввод, кроме 'y')
    """
    list_products = second_category.products_in_list
    new_product = Product.new_product(dict_product_price_is_lower, list_products)

    assert new_product.name == "Tefal 457"
    assert new_product.description == "Black, 2000W"
    assert new_product.price == 4500
    assert new_product.quantity == 11
