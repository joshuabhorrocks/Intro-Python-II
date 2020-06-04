# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = []

    def __str__(self):
        return f"Location: {self.name}. Description: {self.description}. Items: {self.items_in_room}"

    def add_items(self, *item):
        self.items_in_room = [x for x in item]