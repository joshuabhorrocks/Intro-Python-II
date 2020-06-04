# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player():
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom

class Interact(Player, Room):
    def __init__(self, inventory, item, currentRoom):
        super().__init__(currentRoom)
        self.inventory = []
        self.item = item

    # Search Room
    def search_room(self):
        if len(self.currentRoom.items_in_room) > 0:
            for x in self.currentRoom.items_in_room:
                print(f"A {self.item.name} is nearby. It looks like {self.item.description}.")
        else:
            print("You look around but find nothing useful")

    # Get Item
    def get_item(self):
        if self.items_in_room is not None:
            for x in self.items_in_room:
                self.inventory.append(self.item)
                print(f"You picked up: {self.item.name}")
        else:
            print("There's no item by that name in your inventory.")

    # Drop Item
    def drop_item(self):
        if self.inventory is not None:
            for x in self.inventory:
                self.inventory.remove(self.item.name)
                print(f"You have discarded: {self.item.name}")
        else:
            print("There's no item by that name in your inventory.")
