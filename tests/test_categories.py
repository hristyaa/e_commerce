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
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 3
