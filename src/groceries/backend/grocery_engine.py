"""Main backend object"""
import yaml
from os import path

from .groceries import GroceryItem, Groceries


class GroceryEngine:
    def __init__(self):
        groceries_path = path.join(path.dirname(__file__),"default_groceries.yaml")
        base_groceries = yaml.load(open(groceries_path, "r"), yaml.Loader)
        base_groceries = sum([[GroceryItem(g["name"], cat["category"]) for g in cat["elements"]] for cat in base_groceries], [])
        self.grocery_list = Groceries(base_groceries)
    