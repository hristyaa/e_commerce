def test_categories_init(first_category, second_category):
    assert first_category.name == 'Парогенераторы'
    assert first_category.description == 'Парогенератор изменит Ваше представление об уходе за одеждой'
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
