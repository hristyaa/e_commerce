import pytest

from src.products import Product


def test_categories_init(first_category, second_category):
    assert first_category.name == "Парогенераторы"
    assert first_category.description == "Парогенератор изменит Ваше представление об уходе за одеждой"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_categories_products_property(first_category):
    assert first_category.products == (
        "Braun 770x, 28000 руб. Остаток: 14 шт.\n" "Tefal ultra R124, 24500 руб. Остаток: 4 шт.\n"
    )


def test_categories_add_product(first_category, product):
    """Тест на увеличение кол-ва продуктов при добавлении товара"""
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 3


def test_categories_str(second_category):
    """Тест строкового отображения класса Category"""
    assert str(second_category) == "Фены, количество продуктов: 17 шт."


def test_categories_add_product_smartphone(first_category, product_smartphone_1, product, product_lawn_grass_1):
    """Проверка на добавление в категорию смартфонов, травы газонной или других продуктов"""
    first_category.add_product(product_smartphone_1)
    assert first_category.products_in_list[-1].name == "Iphone 15"
    first_category.add_product(product)
    assert first_category.products_in_list[-1].name == "Tefal 457"
    first_category.add_product(product_lawn_grass_1)
    assert first_category.products_in_list[-1].name == "Газонная трава"
    assert first_category.products_in_list[-3].name == "Iphone 15"
    assert first_category.products_in_list[-2].name == "Tefal 457"


def test_categories_add_product_error(first_category, second_category):
    """Проверка на ошибку при добавлении в категорию любого объекта вместо продукта или его наследников"""
    with pytest.raises(TypeError):
        first_category.add_product(2)
        first_category.add_product("Утюг")
        first_category.add_product(second_category)


def test_middle_price(second_category, category_without_products):
    """Проверка определения среднего ценника товаров в категории"""
    assert second_category.middle_price() == 4166.66
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, second_category):
    assert len(second_category.products_in_list) == 3

    product_add = Product("Tefal 457", "Black, 2000W", 4999.99, 8)
    second_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    with pytest.raises(ValueError):
        product_add = Product("Tefal 457", "Black, 2000W", 4999.99, 0)
        second_category.add_product(product_add)
