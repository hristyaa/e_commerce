import json
import os

from src.categories import Category
from src.products import Product


def read_json_file(filepath):
    """Функция для чтения json-файла."""
    path = os.path.abspath(filepath)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_objects_from_json(data):
    """Функция для создания объектов классов из файла JSON."""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            category["products"] = products
        categories.append(Category(**category))
    return categories


data_json = read_json_file("../data/products.json")
categories_data = create_objects_from_json(data_json)
print(categories_data[0].name)
print(categories_data[0].products)
