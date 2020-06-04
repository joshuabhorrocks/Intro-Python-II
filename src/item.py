# Initializing class for items

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"A {self.name} is nearby. It looks like {self.description}."