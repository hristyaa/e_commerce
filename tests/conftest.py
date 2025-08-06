import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def first_category():
    return Category(
        name='Парогенераторы',
        description='Парогенератор изменит Ваше представление об уходе за одеждой',
        products=[
            Product('Braun 770x', '2000Вт, 180г/м', 28000, 14),
            Product('Tefal ultra R124', '1800Вт, 175 г/м', 24500, 4)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name='Фены',
        description='Современные фены не портят волосы повышенной температурой, а сушат мощным потоком воздуха',
        products=[
            Product('Babyliss 114', 'White, 2200W', 5600, 2),
            Product('Tefal 457', 'Black, 2000W', 4500, 8),
            Product('Vitek 880', 'Blue, 1800W', 2399.99, 7)
        ]
    )


@pytest.fixture
def product():
    return Product('Tefal 457', 'Black, 2000W', 4999.99, 8)