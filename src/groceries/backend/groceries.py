"""Implementation of grocery items: single object that can enter a grocery list"""

from collections import UserDict


class GroceryItem:
    """Grocery item: single object that can enter a grocery list"""

    def __init__(self, name="Item", category="Misc", needed=False):
        assert isinstance(name, str)
        self.name = name
        self.category = category
        self.need = needed
    
    def is_needed(self):
        return self.need

    def needed(self):
        self.need = True

    def not_needed(self):
        self.need = False

    def add_to_grocery_list(self):
        """Add to the grocery list: set needed to true"""
        self.needed()

    def buy(self):
        """Buy: remove from grocery list by setting needed to False"""
        self.not_needed()

    def __str__(self):
        return self.name


class Groceries(UserDict):
    """List of groceries"""

    def __init__(self, groceries):
        assert all([isinstance(g, GroceryItem) for g in groceries])
        groceries_dict = dict([(g.name, g) for g in groceries])
        super(Groceries, self).__init__(groceries_dict)

    def reset(self):
        for key in self:
            self[key].not_needed()

    def add_item_to_grocery_list(self, item):
        self[item].add_to_grocery_list()

    def add_items_to_grocery_list(self, items):
        for item in items:
            self.add_item_to_grocery_list(item)

    def to_list(self):
        return list(self.values())
    
    def going_shopping(self):
        shopping_list = []
        for item in self.values():
            if item.is_needed():
                shopping_list.append(item)
        return list(shopping_list)
        
    def done_shopping(self, items):
        for item in items:
            self[item].buy()
        
            
