import pytest

from src.categories import Category
from src.lawn_grass import LawnGrass
from src.product_iterator import ProductIterator
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_category():
    return Category(
        name="Парогенераторы",
        description="Парогенератор изменит Ваше представление об уходе за одеждой",
        products=[
            Product("Braun 770x", "2000Вт, 180г/м", 28000, 14),
            Product("Tefal ultra R124", "1800Вт, 175 г/м", 24500, 4),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Фены",
        description="Современные фены не портят волосы повышенной температурой, а сушат мощным потоком воздуха",
        products=[
            Product("Babyliss 114", "White, 2200W", 5600, 2),
            Product("Tefal 457", "Black, 2000W", 4500, 8),
            Product("Vitek 880", "Blue, 1800W", 2399.99, 7),
        ],
    )


@pytest.fixture
def product():
    return Product("Tefal 457", "Black, 2000W", 4999.99, 8)


@pytest.fixture
def product_2():
    return Product("Vitek 880", "Blue, 1800W", 2399.99, 7)


@pytest.fixture
def dict_product():
    return {"name": "Tefal 457", "description": "Black, 2000W", "price": 5999.99, "quantity": 4}


@pytest.fixture
def dict_product_price_is_lower():
    return {"name": "Tefal 457", "description": "Black, 2000W", "price": 3999.99, "quantity": 3}


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)


@pytest.fixture
def product_smartphone_1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_products():
    return Category(
        name="Фены",
        description="Современные фены не портят волосы повышенной температурой, а сушат мощным потоком воздуха",
        products=[],
    )
