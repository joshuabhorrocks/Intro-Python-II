# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player:
    def __init__(self, currentRoom, inventory):
        self.currentRoom = currentRoom
        self.inventory = []

    # Search Room
    def search_room(self):
        if len(self.currentRoom.item_list()) >= 1:
            for x in self.currentRoom.item_list():
                print(f"A {x} is nearby.")
            return True
        else:
            print("You look around but find nothing useful")
            return False

    # Get Item
    def get_item(self):
        if self.currentRoom.items_in_room is not None:
            for x in self.currentRoom.items_in_room:
                self.inventory.append(x)
                self.currentRoom.items_in_room = 0
                print(f"You picked up: {x.name}")
        else:
            print("There's no item by that name in your inventory.")

    def search_inventory(self):
        return self.inventory

    
    # Drop Item
    def drop_item(self):
        if self.inventory is not None:
            for x in self.inventory:
                self.inventory.remove(x)
                self.currentRoom.items_in_room = 0
                print(f"You have discarded: {x.name}")
        else:
            print("There's no item by that name in your inventory.")
