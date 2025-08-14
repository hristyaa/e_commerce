import pytest


def test_product_iterator(product_iterator):
    """Тест итерации по товарам, которые хранятся в категории"""
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Babyliss 114"
    assert next(product_iterator).name == "Tefal 457"
    assert next(product_iterator).name == "Vitek 880"
    with pytest.raises(StopIteration):
        next(product_iterator)
