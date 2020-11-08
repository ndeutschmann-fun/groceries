"""Main backend object"""
import yaml
from os import path

from .groceries import GroceryItem, Groceries


class GroceryEngine:
    def __init__(self):
        groceries_path = path.join(path.dirname(__file__),"default_groceries.yaml")
        base_groceries = yaml.load(open(groceries_path, "r"), yaml.Loader)
        base_groceries = [GroceryItem(**g) for g in base_groceries]
        self.grocery_list = Groceries(base_groceries)

